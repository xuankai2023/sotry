#!/usr/bin/env python3
"""Count reader-narrative hanzi in 日NN.md (exclude title + 批注).

Also fail low-quality rhythm: template words, echo restatement, even sentence runs.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HAN = re.compile(r"[\u4e00-\u9fff]")
NOT_BUT = re.compile(r"不是[^。\n]{0,16}，是")
CLAUSE_SPLIT = re.compile(r"[。！？；…，,\n]+")
SENT_SPLIT = re.compile(r"[。！？…]+")
PROJECT_DAILY = (
    ("90hou-chabuduo", 7000),
    ("00hou-sandai", 6000),
)

ECHO_MAX = 80
ECHO_RATE_MAX = 0.12
EVEN_RUN_MAX = 5
EVEN_LO, EVEN_HI = 7, 13
LIMITS = {
    "一下": 40,
    "还在": 28,
    "指腹": 12,
    "半寸": 12,
    "空着": 24,
    "掌心": 20,
}


def narrative(text: str) -> str:
    body = re.split(r"\n## 批注", text, maxsplit=1)[0]
    lines = body.splitlines()
    if lines and lines[0].startswith("#"):
        lines = lines[1:]
    return "\n".join(lines)


def hanzi(text: str) -> int:
    return len(HAN.findall(text))


def window(target: int) -> tuple[int, int]:
    return target - 200, target + 200


def guess_daily(path: Path) -> int | None:
    s = str(path.resolve())
    for needle, daily in PROJECT_DAILY:
        if needle in s:
            return daily
    return None


def clauses(text: str) -> list[str]:
    parts = []
    for raw in CLAUSE_SPLIT.split(text):
        piece = "".join(HAN.findall(raw))
        if piece:
            parts.append(piece)
    return parts


def echo_hits(parts: list[str]) -> int:
    hits = 0
    for a, b in zip(parts, parts[1:]):
        if len(a) < 2 or len(b) < 2:
            continue
        top = min(4, len(a), len(b))
        for k in range(top, 1, -1):
            if a[-k:] == b[:k]:
                hits += 1
                break
    return hits


def even_run(text: str) -> int:
    sents = []
    for raw in SENT_SPLIT.split(text):
        n = hanzi(raw)
        if n:
            sents.append(n)
    longest = run = 0
    for n in sents:
        if EVEN_LO <= n <= EVEN_HI:
            run += 1
            longest = max(longest, run)
        else:
            run = 0
    return longest


def stats(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    n = narrative(text)
    parts = clauses(n)
    echoes = echo_hits(parts)
    pairs = max(len(parts) - 1, 1)
    return {
        "path": path,
        "hanzi": hanzi(n),
        "一下": n.count("一下"),
        "还在": n.count("还在"),
        "指腹": n.count("指腹"),
        "半寸": n.count("半寸"),
        "空着": n.count("空着"),
        "掌心": n.count("掌心"),
        "不是A是B": len(NOT_BUT.findall(n)),
        "接力": echoes,
        "切段": pairs,
        "接力比": echoes / pairs,
        "匀句串": even_run(n),
    }


def check_file(row: dict, daily: int | None) -> list[str]:
    errors = []
    n = row["hanzi"]
    name = row["path"].name
    if daily is not None:
        lo, hi = window(daily)
        if n < lo:
            errors.append(
                f"{name}: {n} < {lo}（目标 {daily}）。只补已有拍的走、坐、热、等，"
                "或并成有过程的长句，禁止用接力复述滚字。"
            )
        elif n > hi:
            errors.append(f"{name}: {n} > {hi}（目标 {daily}）。在自然停顿处拆下一个 md。")
    for word, limit in LIMITS.items():
        if row[word] > limit:
            errors.append(f"{name}: 「{word}」{row[word]} > {limit}")
    if row["接力"] > ECHO_MAX:
        errors.append(f"{name}: 接力复述 {row['接力']} > {ECHO_MAX}")
    if row["接力比"] > ECHO_RATE_MAX:
        errors.append(f"{name}: 接力复述占比 {row['接力比']:.1%} > {ECHO_RATE_MAX:.0%}")
    if row["匀句串"] > EVEN_RUN_MAX:
        errors.append(f"{name}: 连续 {row['匀句串']} 句都在 {EVEN_LO}–{EVEN_HI} 字 > {EVEN_RUN_MAX}")
    return errors


def main() -> int:
    p = argparse.ArgumentParser(description="数日更读者叙事汉字，并拦模板词与接力复述")
    p.add_argument("files", nargs="+", type=Path)
    p.add_argument("--daily", type=int, help="单日目标。不写则按路径猜：差不多 7000，00 后 6000")
    p.add_argument("--chapter", type=int, help="整章合计目标，如 21000 / 28000")
    args = p.parse_args()

    rows = []
    errors: list[str] = []
    for f in args.files:
        if not f.exists():
            errors.append(f"缺少 {f}")
            continue
        row = stats(f)
        rows.append(row)
        daily = args.daily if args.daily is not None else guess_daily(f)
        if daily is None and args.chapter is None:
            print(f"{f}: {row['hanzi']}（未识别日更，补 --daily）", file=sys.stderr)
        errors.extend(check_file(row, daily))
        extra = ""
        if daily is not None:
            lo, hi = window(daily)
            extra = f"  窗口 {lo}–{hi}"
        print(
            f"{f.name}\t{row['hanzi']}\t一下 {row['一下']}\t还在 {row['还在']}\t"
            f"指腹 {row['指腹']}\t半寸 {row['半寸']}\t空着 {row['空着']}\t掌心 {row['掌心']}\t"
            f"不是A是B {row['不是A是B']}\t接力 {row['接力']}/{row['切段']} "
            f"({row['接力比']:.1%})\t匀句串 {row['匀句串']}{extra}"
        )

    if not rows:
        print("没有可数的文件", file=sys.stderr)
        return 1

    total = sum(r["hanzi"] for r in rows)
    if len(rows) > 1:
        print(f"合计\t{total}")
    if args.chapter is not None:
        daily = args.daily
        if daily is None:
            dailies = {guess_daily(r["path"]) for r in rows}
            daily = next(iter(dailies)) if len(dailies) == 1 else None
        n = len(rows)
        if daily is not None:
            lo, hi = n * (daily - 200), n * (daily + 200)
        else:
            lo, hi = args.chapter - 200 * max(n, 1), args.chapter + 200 * max(n, 1)
        print(f"整章窗口 {lo}–{hi}（目标 {args.chapter}）")
        if total < lo:
            errors.append(f"整章 {total} < {lo}。未过下限的那一日只补已有拍，禁止接力复述滚字。")
        elif total > hi:
            errors.append(f"整章 {total} > {hi}。超的那一日拆到下一日，不准删已成立的选择。")

    if errors:
        print("未过门：", file=sys.stderr)
        for e in errors:
            print(f"- {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
