---
name: novel-style-restrained-hands
description: 生成克制留白、汪曾祺式手艺与日常温情的小说总纲和中纲。Use when the user asks for 汪曾祺式、留白、克制、手艺、饭桌、工具、少说话但有情的大纲.
---

# Novel Style: Restrained Hands

## Style Promise

少解释，多看手。

这种风格不把情感说满。人物的爱在修车、盛汤、洗碗、削铅笔、绑棉垫、把碗放正里。

## Scope

- Use the style as a way of seeing, not as sentence-level imitation.
- For non-00后三代 requests, do not import 周晓宁、林倩、周桂芳 or existing project scenes; build new carriers from the user's material.
- If the user asks for 中纲, first write the 总纲 shape, then split into 4-6 large movements. Do not write chapter-level beats unless explicitly asked.

## Outline Rules

1. Every main emotion should have a hand action.
2. Let tools carry character: bicycle bell, wrench, bowl, passbook, pencil knife, stool.
3. Dialogue must be short. If a sentence can be replaced by an action, use the action.
4. Do not name the wound too early; let repetition reveal it.
5. Sadness should be light on the page and heavy after reading.
6. End with an object slightly changed in meaning.

## For 00后三代

Dominant carriers: 钱厚德 / 周志刚, with 周桂芳's hands as support.

Useful scenes:

- 外公绑车后座棉垫.
- 爷爷把碗放回孩子面前.
- 奶奶洗碗洗得很响.
- 孩子把门关上 but leaves the light under the door.

This style works best for a restrained version of the whole outline. If the user asks for a specific chapter, route to `novel-chapter-restrained-hands`.

## Avoid

- explaining "他其实很爱"
- emotional speeches
- turning silence into coldness only
- adding decorative pastoral prose

## Output Shape

For 总纲, include:

- which hands carry the book
- which object changes meaning
- which sentence is deliberately not said
- what the reader understands through omission
