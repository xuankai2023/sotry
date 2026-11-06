---
name: novel-style-urban-daily
description: 生成市民日常、王安忆式城市生活质感的小说总纲和中纲。Use only when the user explicitly asks for 王安忆式 or 市民日常总纲.
disable-model-invocation: true
---

# Novel Style: Urban Daily Texture

## Style Promise

不喊命运，写日程。

人物的命运藏在每天重复的路线里：几点起锅、几点接人、去哪家菜摊、衣服晾哪一排、谁先占厨房、谁睡客厅帘后。

## Scope

- Use the style as a way of seeing, not as sentence-level imitation.
- For non-00后三代 requests, do not import 周晓宁、林倩、周桂芳 or existing project scenes; build new carriers from the user's material.
- If the user asks for 中纲 / 部分总结：转 `novel-mid-outline`。本 skill 只交全书看法。

## Outline Rules

1. Start from a daily route: bedroom → kitchen → market → school gate → work unit → dinner table.
2. Let routine reveal power: who repeats the work owns the family rhythm.
3. Use dense but ordinary objects: enamel cup, passbook, plastic bag, basin, towel, schoolbag, stool.
4. Conflict should come from schedule collision, not speeches.
5. Women are not symbols; they are managers of time, food, money, shame, and waiting.
6. The ending should show a changed routine, not a declared lesson.

## For 00后三代

Dominant carrier: 周桂芳.

Her outline should be built from:

- six o'clock pot
- seven o'clock porridge
- market bargaining
- clothes on the balcony
- afternoon school gate
- evening news volume
- plastic stool outside the iron gate

The child changes when he no longer follows the household route. He turns from kitchen and doorway toward bedroom and screen.

## Avoid

- abstract "时代变迁"
- summary of social policy
- sentimental grandmother praise
- listing snacks without showing who bought, hid, washed, or forbade them

## Output Shape

For 总纲, name:

- the main room
- the daily route
- which routine gets broken
- who loses power when the routine breaks
- what new routine replaces it
