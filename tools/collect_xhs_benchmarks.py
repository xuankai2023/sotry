#!/usr/bin/env python3
"""Collect Xiaohongshu benchmark teardowns through the logged-in Chrome session."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import time
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Direction:
    account: str
    label: str
    query: str
    keywords: tuple[str, ...]
    banned_keywords: tuple[str, ...] = ()


DIRECTIONS = {
    "skincare": Direction(
        account="01-hot-skincare",
        label="护肤 / 成分 / 修护",
        query="敏感肌 屏障修护 面霜 精华 痘肌 护肤成分",
        keywords=("护肤", "成分", "修护", "敏感", "防晒", "面霜", "精华", "屏障", "皮肤"),
    ),
    "home": Direction(
        account="02-hot-home-living",
        label="家居生活 / 收纳 / 装修",
        query="小户型 厨房收纳 衣柜收纳 家政柜 租房改造 收纳尺寸",
        keywords=("家居", "收纳", "装修", "小户型", "好物", "厨房", "卧室", "客厅", "改造"),
    ),
    "ai": Direction(
        account="03-hot-ai-workflow",
        label="AI 工具 / 职场效率",
        query="AI工具 职场效率 图文 清单 教程 Codex skill",
        keywords=("AI", "ai", "Codex", "工具", "办公", "效率", "工作流", "skill", "Agent"),
        banned_keywords=("视频", "短视频", "剪映", "成片", "分镜", "带货", "AI视频", "口播", "脚本到成片"),
    ),
    "eldercare": Direction(
        account="04-cold-eldercare",
        label="养老 / 照护 / 银发生活",
        query="适老化改造 老人看病 陪诊服务 养老补贴 失能老人 居家照护",
        keywords=("养老", "照护", "老人", "护理", "陪诊", "银发", "父母", "长辈", "老年"),
    ),
    "craft": Direction(
        account="05-cold-craft-diy",
        label="手工 / DIY / 教程",
        query="钩针图解 编织图解 附图解 手工 包包 花朵",
        keywords=("手工", "DIY", "diy", "教程", "改造", "手作", "材料", "步骤", "自制", "钩针", "黏土", "纸艺", "编织", "手帐"),
    ),
}


def run_osascript(*scripts: str) -> str:
    command: list[str] = ["osascript"]
    for script in scripts:
        command.extend(["-e", script])
    result = subprocess.run(command, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or f"osascript failed: {result.returncode}")
    return result.stdout.strip()


def set_url(url: str, wait: float = 5.0) -> None:
    escaped = url.replace("\\", "\\\\").replace('"', '\\"')
    run_osascript(
        'tell application "Google Chrome" to activate',
        'tell application "Google Chrome" to if (count of windows) = 0 then make new window',
        f'tell application "Google Chrome" to tell active tab of front window to set URL to "{escaped}"',
    )
    time.sleep(wait)


def exec_js(script: str) -> str:
    escaped = script.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
    return run_osascript(
        f'tell application "Google Chrome" to tell active tab of front window to execute javascript "{escaped}"'
    )


def collect_candidates(direction: Direction, needed: int) -> list[dict[str, str]]:
    url = f"https://www.xiaohongshu.com/search_result?keyword={quote(direction.query)}&type=51"
    set_url(url, wait=6.0)
    # Do not click the "图文" tab here: Xiaohongshu can route focus into the
    # first note card. The hard gate is the per-note video detector below.
    for _ in range(8):
        exec_js('window.scrollTo(0, document.body.scrollHeight); "ok"')
        time.sleep(2.5)
    raw = exec_js(
        """
        JSON.stringify(Array.from(document.querySelectorAll('a[href*="/search_result/"]'))
          .map(a => ({ text: (a.innerText || a.textContent || '').trim(), href: a.href }))
          .filter(x => x.text && x.href && !x.text.includes('首页'))
          .slice(0, 240))
        """
    )
    items = json.loads(raw)
    seen: set[str] = set()
    unique: list[dict[str, str]] = []
    for item in items:
        note_id = note_id_from_url(item["href"])
        key = f"{note_id}:{item['text']}"
        if note_id and key not in seen:
            seen.add(key)
            unique.append(item)
        if len(unique) >= needed:
            break
    return unique


def note_id_from_url(url: str) -> str:
    match = re.search(r"/(?:search_result|explore)/([^?/#]+)", url)
    return match.group(1) if match else ""


def extract_note(url: str) -> dict[str, str]:
    set_url(url, wait=4.5)
    raw = exec_js(
        """
        JSON.stringify({
          title: document.title,
          url: location.href,
          text: document.body.innerText.slice(0, 12000)
        })
        """
    )
    return json.loads(raw)


def parse_note(data: dict[str, str], direction: Direction) -> dict[str, object]:
    text = data.get("text", "")
    title = data.get("title", "").replace(" - 小红书", "").strip()
    is_video = bool(re.search(r"\n倍速\n|\n(?:1080P|2K|4K)[^\n]*高清|00:\d{2,4}:\d{2}", text))
    author = ""
    match = re.search(re.escape(title) + r"\n([^\n]+)\n关注\n" + re.escape(title), text)
    if match:
        author = match.group(1).strip()
    else:
        match = re.search(re.escape(title) + r"\n([^\n]+)\n[\d赞]", text)
        if match:
            author = match.group(1).strip()

    counts_match = re.findall(r"\n说点什么\.\.\.\n([^\n]+)\n([^\n]+)\n([^\n]+)\n发送", text)
    counts = counts_match[-1] if counts_match else ("", "", "")
    comments_match = re.search(r"共 ([^\n]+) 条评论", text)
    comments = comments_match.group(1) if comments_match else counts[2]

    body = ""
    marker = f"关注\n{title}\n"
    start = text.find(marker)
    if start != -1:
        body = text[start + len(marker) :]
        body = re.split(r"\n猜你想搜|\n编辑于|\n共 [^\n]+ 条评论|\n这是一片荒地点击评论", body)[0]
        body = re.sub(r"\s+", " ", body).strip()

    haystack = f"{title} {body}"
    relevant = any(keyword in haystack for keyword in direction.keywords)
    banned_topic = any(keyword in haystack for keyword in direction.banned_keywords)
    complete = len(body) >= 20 and bool(title) and bool(author) and not is_video and not banned_topic
    return {
        "title": title,
        "author": author,
        "url": data.get("url", ""),
        "likes": counts[0],
        "saves": counts[1],
        "comments": comments,
        "body_excerpt": body[:260],
        "text_len": len(text),
        "relevant": relevant,
        "complete": complete,
        "is_video": is_video,
        "banned_topic": banned_topic,
    }


def classify_structure(note: dict[str, object]) -> tuple[str, str]:
    title = str(note["title"])
    body = str(note["body_excerpt"])
    combined = title + body
    if any(token in title for token in ("别", "不要", "避坑", "千万")):
        return "anti-pattern fix", "wrong habit or risk -> explanation -> safer alternative"
    if any(token in title for token in ("清单", "排行榜", "TOP", "工具箱", "必备", "推荐")):
        return "save list", "category -> item -> use case -> save cue"
    if any(token in title for token in ("一张图", "搞懂", "金字塔", "进化图")):
        return "visual taxonomy", "map -> layers/categories -> choice rule"
    if any(token in combined for token in ("步骤", "教程", "怎么", "工作流", "流程")):
        return "workflow tutorial", "pain -> steps -> deliverable -> comment question"
    return "experience share", "scene -> observation -> lesson -> interaction"


def render_markdown(direction: Direction, notes: list[dict[str, object]], excluded: list[dict[str, object]]) -> str:
    today = date.today().isoformat()
    lines = [
        f"# Creator Article Corpus - {today}",
        "",
        f"- Platform: 小红书",
        f"- Direction: {direction.label}",
        f"- Valid samples: {len(notes)}",
        f"- Corpus rule: teardown notes only; source text remains at the linked 小红书 page.",
        "",
        "## Valid Sample Set",
        "",
    ]
    for idx, note in enumerate(notes, 1):
        pattern, structure = classify_structure(note)
        lines.extend(
            [
                f"### {idx:02d}. {note['title']}",
                "",
                f"- Creator: {note['author']}",
                f"- URL: {note['url']}",
                "- Media type: 图文文章",
                f"- Visible metrics: {note['likes']} likes / {note['saves']} saves / {note['comments']} comments",
                f"- Pattern: {pattern}",
                f"- Structure: {structure}",
                f"- Source excerpt: {note['body_excerpt']}",
                f"- Reusable principle: keep the reader's task, blocker, or save reason explicit.",
                f"- Do not copy: exact wording, images, private resources, or unverifiable product claims.",
                "",
            ]
        )
    lines.extend(["## Excluded Samples", ""])
    if excluded:
        for note in excluded:
            if note.get("is_video"):
                reason = "video note"
            elif note.get("banned_topic"):
                reason = "video-generation or video-workflow topic"
            elif not note["relevant"]:
                reason = "not relevant"
            else:
                reason = "too little readable body text"
            lines.append(f"- {note['title']}: {reason}.")
    else:
        lines.append("- None from this run.")
    lines.append("")
    return "\n".join(lines)


def collect_direction(key: str, limit: int, overwrite: bool) -> None:
    direction = DIRECTIONS[key]
    out = ROOT / "小红书" / "accounts" / direction.account / "references" / "benchmarks" / "creator-article-corpus-2026-08-30.md"
    if out.exists() and not overwrite:
        print(f"SKIP existing {out}")
        return

    candidates = collect_candidates(direction, needed=limit * 4)
    valid: list[dict[str, object]] = []
    excluded: list[dict[str, object]] = []
    seen: set[str] = set()
    for candidate in candidates:
        if len(valid) >= limit:
            break
        note_id = note_id_from_url(candidate["href"])
        if note_id in seen:
            continue
        seen.add(note_id)
        try:
            parsed = parse_note(extract_note(candidate["href"]), direction)
        except Exception as exc:  # noqa: BLE001 - keep collection moving.
            print(f"ERROR {key} {candidate['text']}: {exc}", flush=True)
            continue
        if parsed["relevant"] and parsed["complete"]:
            title_key = f"{parsed['title']}::{parsed['author']}"
            if title_key in seen:
                excluded.append(parsed)
                print(f"DROP {key}: duplicate {parsed['title']}", flush=True)
                continue
            seen.add(title_key)
            valid.append(parsed)
            print(f"OK {key} {len(valid):02d}: {parsed['title']}", flush=True)
        else:
            excluded.append(parsed)
            print(f"DROP {key}: {parsed['title']}", flush=True)

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_markdown(direction, valid, excluded), encoding="utf-8")
    print(f"WROTE {out} ({len(valid)} valid)", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("directions", nargs="*", choices=sorted(DIRECTIONS), default=["skincare", "home", "eldercare", "craft"])
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    for key in args.directions:
        collect_direction(key, limit=args.limit, overwrite=args.overwrite)


if __name__ == "__main__":
    main()
