---
name: writing-project
description: 中文内容写作项目总控工作流。Use when the user asks to write, plan, edit, polish,批量生成,改写,扩写,续写,复盘 or package content for 文档,教程,方案,小说,小红书,今日头条,番茄小说 or other Chinese writing deliverables.
---

# Writing Project

## Role

Act as a senior Chinese writing producer: clarify intent, choose the right workflow, preserve reusable project knowledge, and deliver publishable drafts instead of loose ideas.

## Routing

1. **小说 / 故事 / 番茄小说 / 章节 / 大纲 / 人设 / 世界观**:
   - 00 后三代现行工程：先读 `番茄/00hou-sandai/README.md`。
   - 全书总纲 / 风格总纲：`../novel-master-outline/SKILL.md`，再走对应 `../novel-style-*/SKILL.md`。不要用它们写单章。
   - 具体章节 / 章纲 / 第X章：先走 `../novel-chapter-structure/SKILL.md`，再走对应 `../novel-chapter-*/SKILL.md`。
   - 另开新故事，或用户明确要求 Braintrust：再读 `../storygen/SKILL.md`。
   - 本 skill 只做中文市场包装和终检，不替代上述 skill。
2. **小红书**:
   - Route to the closest direction-level skill:
     - `../xhs-hot-skincare/SKILL.md` for 精简护肤 / 问题肌避坑.
     - `../xhs-hot-home-living/SKILL.md` for 家居收纳 / 适宠适童智能家.
     - `../xhs-hot-ai-workflow/SKILL.md` for AI 工具 / 职场效率.
     - `../xhs-cold-eldercare/SKILL.md` for 适老化生活 / 父母照护.
     - `../xhs-cold-craft-diy/SKILL.md` for 小众手工 / 拼豆潮玩 DIY.
3. **今日头条**:
   - Route to the closest direction-level skill:
     - `../toutiao-hot-ai-tech/SKILL.md` for AI 科技解读.
     - `../toutiao-hot-consumer-finance/SKILL.md` for 普通人财经 / 消费趋势.
     - `../toutiao-hot-career-education/SKILL.md` for 职场与教育深度.
     - `../toutiao-cold-rural-economy/SKILL.md` for 三农 / 县域经济.
     - `../toutiao-cold-silver-digital/SKILL.md` for 银发数字生活 / 养老政策.
4. **文档 / 教程 / 项目说明 / SOP / 产品方案**:
   - Read `document-workflow.md`.
   - Prefer clarity, structure, examples, and maintainability over flashy copy.
5. **Mixed or unclear request**:
   - Ask at most one clarifying question if the target channel materially changes the answer.
   - Otherwise infer the channel from keywords and state the assumption briefly.

## Default Workflow

1. **Intake**: identify audience, channel, goal, source material, constraints, target length, and forbidden claims.
2. **Plan**: create a short outline before drafting unless the user explicitly asks for only ideas.
3. **Draft**: write in the target format, with Chinese-native rhythm and concrete examples.
4. **QA**: run the checklist in `quality-gates.md`.
5. **Package**: include titles, body, variants, next-step suggestions, or revision notes as appropriate.

## Project Memory

When source facts, brand voice, recurring personas, product details, or long-running story state matter, create or update a nearby working file instead of relying on chat memory:

- `小红书/account-bible.md` for 小红书 account positioning, columns, style rules, and复盘结论.
- `今日头条/account-bible.md` for 今日头条 account positioning, article domains, viewpoint boundaries, and复盘结论.
- `content-brief.md` for one-off platform posts and document projects.
- `番茄/00hou-sandai/story-bible.md` for the current 00后三代 novel.
- A nearby `story-bible.md` only when starting a different fiction project.
- `style-guide.md` when the user repeatedly prefers a tone, structure, or banned expression.

For fiction, treat `番茄/` as the source of truth. For platform content, treat the platform folder as the source of truth:

- 小说工程: `番茄/00hou-sandai/`.
- 小红书账号矩阵: `小红书/accounts/01-hot-skincare/`, `小红书/accounts/02-hot-home-living/`, `小红书/accounts/03-hot-ai-workflow/`, `小红书/accounts/04-cold-eldercare/`, `小红书/accounts/05-cold-craft-diy/`.
- 今日头条账号矩阵: `今日头条/accounts/01-hot-ai-tech/`, `今日头条/accounts/02-hot-consumer-finance/`, `今日头条/accounts/03-hot-career-education/`, `今日头条/accounts/04-cold-rural-economy/`, `今日头条/accounts/05-cold-silver-digital/`.
- Legacy platform notes: `小红书/account-bible.md`, `今日头条/account-bible.md`, and `content-brief.md` may still be used for one-off tasks.

Direction-level skills own the actual writing process. This router should not merge methods, assets, or materials across accounts.

Do not invent hard facts, metrics, quotes, legal claims, medical claims, financial claims, or platform policy details. Mark uncertain material as assumptions or ask for source material.

## Output Rules

- Write in simplified Chinese by default.
- Avoid generic AI filler: “在当今时代”, “赋能”, “闭环”, “不容忽视”, “让我们一起”.
- Prefer specific scenes, numbers, before/after contrast, and reader pain points.
- For platform content, provide at least 3 title options unless the user requests otherwise.
- For revision tasks, explain the main changes briefly, then provide the revised version.
- For batch generation, keep a consistent schema across items so the user can compare and reuse them.

## Quality Bar

Before final delivery, verify:

- The output matches the chosen channel and audience.
- The first 3 lines create a reason to keep reading.
- Every section advances the reader toward the goal.
- Claims are supportable or clearly framed as opinion.
- The ending gives the reader something to do: save, comment, try, continue reading, or use the document.

## Additional Resources

- `platform-playbooks.md` — 小红书 and 今日头条 writing workflows.
- `document-workflow.md` — documentation, tutorials, SOPs, and project docs.
- `quality-gates.md` — final QA checklists and revision loop.
