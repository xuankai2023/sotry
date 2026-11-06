---
name: novel-style-family-realism
description: 生成家庭现实主义小说总纲，以普通家庭压力和长期小选择确定全书方向。Use when the user asks for 家庭现实主义总纲、现实主义家庭小说大纲. 中纲转 novel-mid-outline；场卡转 novel-chapter-family-realism；正文转 novel-prose-from-outline.
---

# Novel Style: Family Realism

## Style Promise

写真实家庭，不写狗血家庭。

家庭现实主义的力气不来自大事故，而来自小选择长期堆出来的关系变形：谁请不出假，谁先端碗，谁收走压岁钱，谁站在门口，谁说没事。

## Scope

- Use the style as a way of seeing, not as sentence-level imitation.
- For non-00后三代 requests, do not import 周晓宁、林倩、周桂芳 or existing project scenes; build new carriers from the user's material.
- If the user asks for 中纲 / 部分总结：转 `novel-mid-outline`。本 skill 只交全书看法。

## Outline Rules

1. Start from one ordinary room, not a big theme.
2. Use money, work, school, food, illness, distance, and relatives as pressure.
3. Every main person must be both useful and harmful.
4. Conflict should be morally mixed: no pure villain, no pure victim.
5. The climax should be a small household event that cannot be undone.
6. The ending should not fully solve the family; it should let the reader understand why nobody could easily do better.

## 思想落地

总纲必须先写出全书思想、人物开篇→终局变化、主场背景变化。中纲转 `novel-mid-outline`。三栏见 `novel-thought-ground`。

## 人物

总纲必须把三个扛戏的人写成人物志，方法转 `novel-character-craft`。00 后三代不要在这里另造性格；用该 skill 的 `sandai-cast.md` 和 `番茄/00hou-sandai/中纲/人物志/`。

大章纲若从本风格往下拆，必须带「本章人物」：本章压到哪一寸身世，手和嘴怎样分开。不要把总纲人物段复制进每一章。

每人既有用又伤人。遮住姓名应仍能认出是谁。

## For 00后三代

Default engine:

> 灶台、纸、门口三种权力把周晓宁养大，也把他训练成一个会看脸色、会说没事、会关门的孩子。

Use these as load-bearing scenes:

- 满月酒: child becomes family evidence.
- 第一把勺: daily care beats purchased care.
- 听筒: love compressed into "吃了没".
- 抢勺: child discovers love has sides.
- 留下: child hears adults decide him.
- 晚托散场: person is collected, heart is not.

## Avoid

- 亲情治愈大团圆
- 老人落后 / 父母焦虑 / 孩子受害 flat triangle
- one big apology solving the book
- period object parade
- using public news as plot engine

## Output Shape

For 总纲, write:

- 一句话
- 真实压力
- 三个扛戏的人
- 六个不可逆场面
- 结尾留下的问题

Do not write chapter-level beats unless explicitly asked.
