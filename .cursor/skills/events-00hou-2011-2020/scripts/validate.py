#!/usr/bin/env python3
"""Validate one year of 2011–2020 T/P/G event cards."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
RESEARCH = REPO / "content-intelligence" / "research"

BOOKS = (
    ("T", RESEARCH / "events-00后少年视角", ("2000", "2003", "2006", "2009")),
    ("P", RESEARCH / "events-00后父母视角-2011-2020", ("1970", "1975", "1980", "1985")),
    ("G", RESEARCH / "events-00后爷爷奶奶视角-2011-2020", ("1940", "1945", "1950", "1955")),
)

HAN = re.compile(r"[\u4e00-\u9fff]")
SCENE_BAN = re.compile(
    r"不写|禁止写成|不是骑手|不是黄袋|不是配送|不是绑卡|不是给你红包|"
    r"不是校门口那盏|不是十四岁的灯|不准对着|去年的嘴"
)
NATIONAL_IN_SCENE = re.compile(r"一千八|2061|1511|56360|4697|全国月均|年平均工资")
AGE_PREFIX = re.compile(r"^\d+\s*岁")
EMPTY_ROLE = re.compile(r"还不是这张卡的付款人|未带孙")


def hanzi(text: str) -> int:
    return len(HAN.findall(text))


def split_cards(text: str, prefix: str, year: int) -> list[str]:
    parts = re.split(rf"\n(?=### {prefix}-{year}-)", text)
    cards = []
    for part in parts[1:]:
        m = re.match(rf"(### {prefix}-{year}-\d+.*?)(?=\n## |\Z)", part, re.S)
        cards.append(m.group(1) if m else part)
    return cards


def scene_of(card: str) -> str:
    m = re.search(r"\n现场[:：](.*?)(?=\n\*\*|\n## |\Z)", card, re.S)
    return m.group(1) if m else ""


def age_cell(card: str, year: str) -> str:
    m = re.search(rf"\|\s*{year}\s*\|\s*([^|]+)\|", card)
    return m.group(1).strip() if m else ""


def check_file(prefix: str, path: Path, year: int, ages: tuple[str, ...]) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"{prefix}: 缺少 {path}"]
    text = path.read_text(encoding="utf-8")
    cards = split_cards(text, prefix, year)
    if not 6 <= len(cards) <= 8:
        errors.append(f"{prefix}: {len(cards)} 张，要 6–8")
    for card in cards:
        title = card.split("\n", 1)[0].strip()
        n = hanzi(card)
        if n < 600 or n > 1000:
            errors.append(f"{title}: {n} 汉字，要 600–1000")
        scene = scene_of(card)
        if not scene.strip():
            errors.append(f"{title}: 没有现场")
        else:
            for pat, label in (
                (SCENE_BAN, "现场有作者禁令"),
                (NATIONAL_IN_SCENE, "现场有全国账"),
            ):
                hit = pat.search(scene)
                if hit:
                    errors.append(f"{title}: {label}「{hit.group(0)}」")
        for age in ages:
            cell = age_cell(card, age)
            if not cell:
                errors.append(f"{title}: 缺 {age} 格")
                continue
            after_age = AGE_PREFIX.sub("", cell)
            after_role = EMPTY_ROLE.sub("", cell)
            if hanzi(after_age) < 2 or (EMPTY_ROLE.search(cell) and hanzi(after_role) < 2):
                errors.append(f"{title}: {age} 格太薄「{cell}」")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="校验 2011–2020 三本事件卡")
    parser.add_argument("year", type=int, help="例如 2014")
    args = parser.parse_args()
    year = args.year
    if year < 2011 or year > 2020:
        print("年份要在 2011–2020", file=sys.stderr)
        return 2

    print(f"REPO {REPO}")
    failed = 0
    for prefix, folder, ages in BOOKS:
        path = folder / f"{year}.md"
        errors = check_file(prefix, path, year, ages)
        if errors:
            failed += 1
            print(f"FAIL {prefix} {path}")
            for err in errors:
                print(f"  - {err}")
        else:
            text = path.read_text(encoding="utf-8")
            cards = split_cards(text, prefix, year)
            counts = [hanzi(c) for c in cards]
            print(f"PASS {prefix} {len(cards)}张 {min(counts)}–{max(counts)} 汉字")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
