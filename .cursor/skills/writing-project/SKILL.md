---
name: writing-project
description: 中文内容写作总控：判断频道后转到对应 skill，不写正文。Use when the user asks for 总控、走哪条工作流、选账号、频道不清, or mentions 文档/教程/方案/SOP without a more specific skill. Do not use when the user already named 写正文、写中纲、写细纲、写场卡、短故事, or a specific 小红书/今日头条账号方向.
---

# Writing Project

## Role

Act as a senior Chinese writing producer: clarify intent, choose the right workflow, preserve reusable project knowledge, and deliver publishable drafts instead of loose ideas.

用户已点名写正文 / 中纲 / 细纲 / 场卡 / 短故事 / 某账号方向时，直接走对应 skill，不要先读本文件再读 `novel-workflow`。

## Routing

1. **番茄短故事 / 小故事 / 超短篇 / 中短篇 / 千字万金**:
   - 只走 `番茄/短故事/skill/SKILL.md`（`.cursor/skills/fanqie-short-story/` 只做跳转）。工程只在 `番茄/短故事/`。
   - 禁止打开长篇工程，禁止调用任何 `novel-*` skill。
   - 一篇一个完整情绪弧。不要用长篇的场卡、中纲、一天 6000 字日更。
2. **小说 / 长篇 / 番茄长篇 / 章节 / 大纲 / 人设 / 世界观**:
   - 先整体后局部。顺序与节点见 `../novel-workflow/SKILL.md`。工作流 / 思维导图 / 从总纲写到正文 / 更专业 / 场卡合同：先读它。开写前先锁一场能写的合同，不要场序对了就动笔。
   - 00 后三代现行工程：先读 `番茄/00hou-sandai/README.md` 的冻结。大章 1–18 已锁定、全书正文已停；用户没点名，不重写。发布文件用 `日NN.md`，`第X章.md` 只作通读。一本一条风格竖线；已写大章是家庭现实主义，改、续、复核都按这个风格，不用另外七套风格重写。
   - 全书总纲 / 风格总纲 / 六部与大章骨架：`../novel-master-outline/SKILL.md`，再走对应 `../novel-style-*/SKILL.md`。总纲人物必须按 `../novel-character-craft/SKILL.md` 写成人物志。性格变化必须按 `../novel-character-change/SKILL.md` 写成合同。总纲必须写出思想、人物变化、背景变化。不要用它们写场卡或正文。
   - 中纲 / 部分总结 / 部纲 / 这一部怎么收 / 卡文 / 情节漏洞：走 `../novel-mid-outline/SKILL.md`。每次写中纲都要使用到以前的中纲和总纲，结合着写。性格变化：总纲已定以总纲为主，`../novel-character-change/SKILL.md` 为辅。中纲是一部或一段大章的总结，不写场卡，不写正文。
   - 大章纲 / 场卡 / 第X章怎么安排 / 谁上场：该部分中纲宜先齐；再走 `../novel-chapter-structure/SKILL.md`，再走对应 `../novel-chapter-*/SKILL.md`。大章纲必须带本章人物、身世一寸、声音差，以及本章/本场的思想、人物变化、背景变化。
   - 细纲 / 把场卡拆成拍 / 开写前细纲 / 日更怎么切：场卡齐后走 `../novel-fine-outline/SKILL.md`。不写正文，不改场序。不要把细纲写成中纲。
   - 人物、环境、事物描写：先走 `../novel-thought-ground/SKILL.md` 把三栏写出来，再走人物 / 场景 / 物件等 `../novel-material-*/SKILL.md` 或 `../novel-character-craft/SKILL.md`。描写层没有思想与变化，不准拼文章包。
   - 怎么写第X章 / 按架构拼这一篇 / 开写包 / 材料怎么拼进正文 / 某人遇见什么：走 `../novel-article-assemble/SKILL.md`。它只交文章包，不写正式正文，不改冻结矩阵。材料必须打开再登记。文章包必须写清某人遇见什么事，并指回三栏。
   - 写第X章正文 / 写某一场 / 续写 / 扩写章纲为正文 / 修改正文：走 `../novel-prose-from-outline/SKILL.md`。必须打开本部分中纲、本场场卡、本场细纲，按拍写、按日切配额写满；不准只凭文章包或印象开写。中纲未齐先走 `../novel-mid-outline/SKILL.md`；场卡未齐先走 `../novel-chapter-structure/SKILL.md`；细纲未齐先走 `../novel-fine-outline/SKILL.md`。每个发布文件是 `日NN.md`，字数听该书日更（《差不多》7000，00 后 6000）。写后跑计数脚本（字数、模板词、接力复述都要过）、做批注校验并回填 Scene ledger。禁搬门见 `../novel-chapter-prose/cannot-copy.md`。
   - 查重 / 抄袭 / 不能搬 / 下架 / 洗稿：走 `../novel-chapter-prose/cannot-copy.md`。只报风险或改被点名的重合段，不要为了本门去全文改已锁定章。
   - 人物性格 / 身世 / 人物志 / 人设：走 `../novel-character-craft/SKILL.md`。总纲和中纲里的人都必须经这一层，不要只排物件。
   - 性格变化 / 人物弧光 / 开篇到终局会变成什么样：走 `../novel-character-change/SKILL.md`。写总纲或中纲时直接嵌进去，不要事后补心情。
   - 正文语气样本 / 试文风但不进入正式小说：走 `../novel-material-voice-sample/SKILL.md`，不回填正式状态。
   - 心理动作、关系、物件、场景、潜台词、外圈、年代等材料请求：先确认 `../novel-thought-ground/SKILL.md` 三栏，再走对应 `../novel-material-*/SKILL.md`；材料 skill 不排章，不写完整正文。
   - 用户只说「写第X章」时，优先根据上下文判断正文还是章纲；若会改变交付物且上下文无法判断，只问这一项，不连问风格和长度。
   - 另开新故事，或用户明确要求 Braintrust：再读 `../storygen/SKILL.md`。
   - 本 skill 只做中文市场包装和终检，不替代上述 skill。
3. **小红书**:
   - Route to the closest direction-level skill:
     - `../xhs-hot-skincare/SKILL.md` for 精简护肤 / 问题肌避坑.
     - `../xhs-hot-home-living/SKILL.md` for 家居收纳 / 适宠适童智能家.
     - `../xhs-hot-ai-workflow/SKILL.md` for AI 工具 / 职场效率.
     - `../xhs-cold-eldercare/SKILL.md` for 适老化生活 / 父母照护.
     - `../xhs-cold-craft-diy/SKILL.md` for 小众手工 / 拼豆潮玩 DIY.
4. **今日头条**:
   - Route to the closest direction-level skill:
     - `../toutiao-hot-ai-tech/SKILL.md` for AI 科技解读.
     - `../toutiao-hot-consumer-finance/SKILL.md` for 普通人财经 / 消费趋势.
     - `../toutiao-hot-career-education/SKILL.md` for 职场与教育深度.
     - `../toutiao-cold-rural-economy/SKILL.md` for 三农 / 县域经济.
     - `../toutiao-cold-silver-digital/SKILL.md` for 银发数字生活 / 养老政策.
5. **00 后事件卡 / 少年父母祖辈主卡 / T- P- G-**:
   - 2021–2026 三本一起写或优化：走 `../events-00hou-2021-2026/SKILL.md`。一次一年，下一笔等点头。禁止改小说、禁止改 2000–2010 旧库、禁止改 2011–2020 成品。
   - 2011–2020 三本一起写或优化：走 `../events-00hou-2011-2020/SKILL.md`。一次一年，下一笔等点头。禁止改小说、禁止改 2000–2010 旧库。
   - 2000–2010 父母：走 `../events-00hou-parents/SKILL.md`。
   - 2000–2010 祖辈：走 `../events-00hou-grandparents/SKILL.md`。
6. **文档 / 教程 / 项目说明 / SOP / 产品方案**:
   - Read `document-workflow.md`.
   - Prefer clarity, structure, examples, and maintainability over flashy copy.
7. **Mixed or unclear request**:
   - Ask at most one clarifying question if the target channel materially changes the answer.
   - Otherwise infer the channel from keywords and state the assumption briefly.

## Default Workflow

1. **Intake**: identify audience, channel, goal, source material, constraints, target length, and forbidden claims.
2. **Plan**: create a short outline before drafting unless the user explicitly asks for only ideas.
3. **Draft**: write in the target format, with Chinese-native rhythm and concrete examples. Current long-form fiction must follow its scene card and continuity ledger rather than a generic short outline.
4. **QA**: run the checklist in `quality-gates.md`.
5. **Package**: include titles, body, variants, next-step suggestions, or revision notes as appropriate.

## Project Memory

When source facts, brand voice, recurring personas, product details, or long-running story state matter, create or update a nearby working file instead of relying on chat memory:

- `小红书/account-bible.md` for 小红书 account positioning, columns, style rules, and复盘结论.
- `今日头条/account-bible.md` for 今日头条 account positioning, article domains, viewpoint boundaries, and复盘结论.
- `content-brief.md` for one-off platform posts and document projects.
- `番茄/短故事/` for Fanqie short stories（小故事 / 超短 / 中短）。Do not mix with the long novel.
- `番茄/00hou-sandai/story-bible.md` for the current 00后三代 novel.
- A nearby `story-bible.md` only when starting a different fiction project.
- `style-guide.md` when the user repeatedly prefers a tone, structure, or banned expression.

For fiction, treat `番茄/` as the source of truth. For platform content, treat the platform folder as the source of truth:

- 短故事工程: `番茄/短故事/`.
- 长篇小说工程: 现行开写 `番茄/90hou-chabuduo/`；00 后三代 `番茄/00hou-sandai/`（正文已停）。
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

- `../events-00hou-2011-2020/SKILL.md` — 2011–2020 三本事件卡。
- `../novel-workflow/SKILL.md` — 小说先整体后局部的思维导图与节点。
- `platform-playbooks.md` — 小红书 and 今日头条 writing workflows.
- `document-workflow.md` — documentation, tutorials, SOPs, and project docs.
- `quality-gates.md` — final QA checklists and revision loop.
