---
name: novel-master-outline
description: 生成发人深省、非烂俗剧情、来源于真实生活观察的中文长篇小说大师式总纲，并写出全书思想、人物性格变化、背景变化与人物志。Use when the user asks for 全书总纲、主线、脑图、六部骨架、文章大师写法. 中纲转 novel-mid-outline；人物志细节转 novel-character-craft；写正文转 novel-prose-from-outline。
---

# Novel Master Outline

## Role

本 skill 只做全书总纲、六部走向和大章骨架。先整体后局部：总纲必须先写出思想、人物开篇→终局会变什么、主场背景会变什么。单场三栏见 `novel-thought-ground`。性格怎么变必须按 `novel-character-change` 写成合同，不要事后补一行心情。  
用户要中纲 / 部分总结 / 部纲：转 `novel-mid-outline`。  
写具体大章纲、场卡、亲朋谁进门：转 `novel-chapter-structure`，再走对应 `novel-chapter-*`。写完整正文转 `novel-prose-from-outline`。不要在这里写具体场卡或正文。八个 `novel-style-*` 也不要改。

总纲里的人必须按 `novel-character-craft` 写成人物志：身世、缺口、爱的办法、伤人的同一办法、手、嘴、年段门。只有欲望四个字，总纲不算齐。00 后三代默认同见该 skill 的 `sandai-cast.md` 与 `番茄/00hou-sandai/中纲/人物志/`。

写到「人物变化」时，必须打开 `../novel-character-change/SKILL.md`，按它的总纲模板交：主变、压变场面、各部一寸、终局只差一寸、可见证据。00 后三代对照见该 skill 的 `sandai-arcs.md`。

## Entry Contract

先判定任务，不要一上来重写全书：

1. **新书总纲**：先收题材、主角、主场、核心矛盾，再写一份总纲。
2. **现有总纲修订**：先读已落盘总纲，只修用户点名的问题；不因格式不齐重开整本。
3. **00 后三代现行书**：先读 `番茄/00hou-sandai/README.md`、`story-bible.md`、`总纲-大师写法.md`。这本已认总纲，不另起一份；只在用户明确要求补总纲栏位时，按已定骨头补思想 / 人物变化 / 背景变化，不改冻结矩阵。

交付前必须说清楚当前属于哪一种。若用户只说“写总纲”，默认交**总纲**，不顺手往下拆中纲、场卡或正文。

## Core Rule

先写总的，细的先别写。

不要把资料库、事件年表、人物画像索引直接改成小说大纲。真正能开写的大纲只回答：

1. 这是谁的书？
2. 困住人物的主场是什么？
3. 哪几件事发生后关系回不去？
4. 主角最后看懂了什么？

如果用户明确要求中纲 / 部分总结，转 `novel-mid-outline`。如果用户明确要求细纲 / 把场卡拆成拍，转 `novel-fine-outline`（场卡未齐先 `novel-chapter-structure`）。没有明确要求时，只交总纲。

## Novel Features Checklist

小说不是资料整理。任何总纲至少要具备这些特征：

1. **人物欲望**: 主角必须想要一件具体东西，不是只代表一代人。
2. **内在缺口**: 每个主要人物都有未被满足的伤口，这个伤口会扭曲他们的爱。
3. **外部压力**: 钱、房、班、学校、门口、亲戚眼光必须真实压住人物。
4. **不可逆场面**: 每个关键场面之后，关系回不到原样。
5. **因果推进**: 事件必须导致人物改变做法，不能只是年份顺排。性格怎么变，按 `novel-character-change` 锁主变和压变场面。
6. **生活质感**: 物件必须被人拿、洗、藏、付钱、修理、等待，不能只是时代标签。
7. **潜台词**: 最重要的话常常不说出口，转成夹菜、收钱、关门、洗碗声。
8. **精神余波**: 结尾不能只解决情节，要留下读者会继续想的问题。

If any feature is missing, revise before delivering.

## Theme Standard

主题必须发人深省，不要网上烂大街剧情。

发人深省不是把道理说大，而是让读者在一个具体家庭里看见自己躲不开的问题。主题必须同时满足：

- 没有纯坏人；每个人的错都来自一种自认为正当的爱、怕、亏欠或生存办法。
- 冲突不能靠误会、吵架、绝症、出轨、车祸、暴富、重生、打脸反转推动。
- 结尾不能靠原谅、和解、忏悔、团圆照、主角成功来解决一切。
- 主角最后得到的不是爽感，而是更难的分辨力：看懂爱里混着债、保护里混着控制、牺牲里混着索取。
- 读者读完应能说出一句刺人的问题，而不是一句鸡汤答案。

For the 00后三代小说, the theme is:

> 他们都在爱孩子，但没有一个人只是在爱孩子。每一代人都把自己没被满足的那一部分，放到下一个孩子身上。

This theme is the north star. Do not replace it with generic "三代亲情", "时代变迁", "00后成长", or "父母不易".

## Life Source Standard

艺术来源于生活。大纲必须先从真实生活的观察里长出来，再上升成主题；不能先想一个道理，再找事件证明它。

Every major outline must include life evidence:

- A lived object: something handled, paid for, folded, washed, hidden, repaired, or waited beside.
- A lived routine: what repeats every day or every week until it becomes fate.
- A lived contradiction: a person does one useful thing, and that same useful thing hurts someone.
- A lived silence: what nobody says because saying it would break the family surface.
- A lived consequence: a small household choice changes how people stand, speak, spend, wait, or avoid each other later.

For 00后三代, prefer these life sources:

- 门口: who waits, who arrives late, who pretends not to mind.
- 灶台: who feeds, who decides water temperature, who says "瘦了".
- 纸: leave slips, receipts, passbooks, school notices, contact books.
- 钱: who gives, who collects, who says it is "for later".
- 手: who reaches first, who withdraws, who washes bowls loudly, who fixes the bicycle pad.
- 房间: who can close a door, who sleeps behind a curtain, who owns no room but occupies the routine.

If the outline cannot point to these ordinary details, it is probably an idea essay, not a novel.

## Anti-Generic Sources

To avoid online cliche, look for material that is slightly inconvenient, mixed, or unflattering:

- The loving person also benefits from being needed.
- The victim also learns a small strategy that later hurts others.
- The correct idea is spoken by someone who cannot practice it.
- The wrong method really works for a while.
- The kindest action leaves a debt.
- The family avoids the real sentence by discussing food, money, routes, or school.

For 00后三代, do not flatten the story into "old vs new." Grandma's old method must sometimes save the day. Mother's new method must sometimes become control. The child's escape must be both survival and loss.

## Mastery Standard

大师式不是把每个细节都压满意义。总纲必须给后续正文留下生活自然流动的空间。

写总纲时同时锁三件事：

- **思想深度**：人物的爱里有缺口、证明、债或自救，不是纯亲情。
- **生活呼吸**：每部至少有能让日子先成立的温暖、好用、好玩或安稳时刻，代价可以延后，不要每个动作立刻被解释成控制。
- **方法隐形**：物件链要服务人物，不要让读者看出作者在机械安排「纸、碗、门、听筒」。

如果总纲只会把每个物件都写成证据、每个场面都写成伤害，后续正文会过密、过硬。必须补一类场面：人物确实被照顾、确实得到一点快乐或安全，但这份好处在后文慢慢露出代价。

## Use These Project Sources

For the 00后三代小说 project, read as needed:

- `番茄/00hou-sandai/story-bible.md`
- `番茄/00hou-sandai/风格总纲/00-索引.md`
- `番茄/00hou-sandai/总纲-大师写法.md`
- `content-intelligence/research/events-00后儿童视角/00-索引.md`
- `content-intelligence/research/events-00后父母视角/00-索引.md`
- `content-intelligence/research/events-00后爷爷奶奶视角/`
- `content-intelligence/research/personas/00-索引.md`
- `content-intelligence/research/personas-00后祖辈/00-索引.md`
- `番茄/00hou-sandai/中纲/人物志/`
- `../novel-character-craft/SKILL.md`
- `../novel-character-change/SKILL.md`

Do not use `tools/storygen-skill-src/samples/linglinghou-decade-one/research/` as the main spine unless the user explicitly switches to a news-braid novel. For the family novel, news stays outside the window.

## Style Routing

If the user asks for different writing styles or literary schools, use or reference these project skills:

- `novel-style-family-realism`: 家庭现实主义。Default for the 00后三代小说; life pressure, ordinary rooms, no melodrama.
- `novel-style-urban-daily`: 市民日常 / 王安忆式。Use when the user wants dense city texture, routines, women, rooms, markets, laundry, work units.
- `novel-style-psychological-debt`: 心理债务 / 张爱玲式。Use when the user wants love-as-debt, family calculation, cold details, emotional ledgers.
- `novel-style-restrained-hands`: 克制留白 / 汪曾祺式。Use when the user wants quiet prose, hands, tools, food, few words, tenderness without explanation.
- `novel-style-labor-social`: 劳动社会现实 / 路遥式。Use when the user wants class pressure, work, money, dignity, long endurance.
- `novel-style-critical-realism`: 批判现实 / 鲁迅式。Use when the user wants structural coldness, "for your own good" as power, no moralizing.
- `novel-style-cold-absurd`: 冷叙荒诞 / 余华式。Use when the user wants pain told plainly, ordinary cruelty, absurd fate, restraint.
- `novel-style-warm-growth`: 温柔成长但不鸡汤。Use when the user wants warmer mass-readable fiction, limited repair, no forced reconciliation.

Do not mix all styles at once. Pick one dominant style and at most one shadow style.

## Workflow

### 1. Reduce The Material

Turn catalogs into one pressure system:

- Pick 1 protagonist.
- Pick 2–3 real dramatic carriers.
- Pick 1 main location.
- Pick 5–7 irreversible events.
- Cut anything that is only period texture.

Also cut anything that is only online-drama bait:

- villain grandma / enlightened mother / victim child
- poor-but-inspiring success arc
- sudden reconciliation through one big speech
- nostalgia object parade
- public news used to force tears
- "原来大家都是为我好" ending

For the 00后三代小说 default:

- Protagonist: 周晓宁, 2000-born child.
- Carriers: 周晓宁 / 林倩 / 周桂芳.
- Mirrors: 赵玉梅, 周建军, 钱厚德, 周志刚.
- Location: 江州单位老楼 and its doorway.
- Spine: 满月酒 → 第一把勺 → 听筒 → 抢勺 → 留下 → 晚托散场 → 成年回看.

### 1.5. Read Before Writing

写新书总纲，至少要有一个可验证的生活来源；没有素材时先向用户要一句真实处境，或用用户已给材料提炼，不凭空堆时代标签。

修 00 后三代总纲时，按这个顺序读：

1. `番茄/00hou-sandai/README.md` 的当前冻结与结构尺度
2. `番茄/00hou-sandai/story-bible.md` 的已锁家庭、脊柱和世界规则
3. `番茄/00hou-sandai/总纲-大师写法.md` 的人物骨头、总结构和结尾
4. 需要补人物时再读 `../novel-character-craft/SKILL.md`
5. 需要补性格变化时再读 `../novel-character-change/SKILL.md`

只读能支撑本次修订的文件。不要为了“更专业”重新打开全书矩阵做六维复核。

### 2. Write The Master Outline

写「三个真正扛戏的人」之后、「六个不可逆场面」前后，打开 `novel-character-change`，把性格变化合同写进「人物变化」。不可逆场面必须至少压一个扛戏的人的主变。

Use this structure:

```markdown
# [Title] · 总纲（大师写法）

## 一句话
[one sharp sentence]

## 这本书真正写什么
[not the topic, but the human wound]

## 主场
[one place with 5–7 concrete objects]

## 三个真正扛戏的人
### [Person]
按 `novel-character-craft` 的人物志写，不要四行标签：
- 身世（到开篇为止，压选择）
- 此刻要什么 / 真正护什么
- 爱的办法 / 伤人的同一办法
- 手（3） / 嘴（常说、不说、句长）
- 年段门（本章以后才能说的句子列出来）

## 另外的人怎么用
[mirrors only; do not turn every persona into a main line]
每人至少：身世一寸、手、嘴、不要抢走发动机。

## 六个不可逆场面
### 1. [Scene]
[what happens, whose relationship changes, why it cannot be undone]

## 总结构
[4–6 large movements, no chapter list]

## 结尾
[what the protagonist understands, without judging everyone]

## 全书思想
[一句刺人的问题，不要「三代亲情 / 时代变迁」。00 后三代默认北星见 Theme Standard。]

## 人物变化 / 性格变化
按 `novel-character-change` 写，不要一行心情。扛戏的人写满，中圈可短：
- 开篇性格（手 / 嘴 / 办法）
- 主变（只选一种）：加硬 / 裂缝 / 换物 / 嘴缩 / 手收 / 误认 / 长出
- 核心办法始终是
- 压变的不可逆场面（2–4 个，只点名）
- 各部一寸（不碰的部写「本部分不碰」）
- 终局只许差的一寸 + 可见证据
- 不许完成 / 不许变成
- 压在哪一句思想上
不许写完弧光，不许「他成长了」。栏位见该 skill 的 `template.md`。

## 背景变化
主场谁有权、哪几样东西换位置或换用法、门口/灶/纸的规矩怎样挪。要看得见。

## 大师式写法的约束
[what to see and omit, not style imitation]
```

### 2.5. Add Depth Before Adding Detail

Depth is not more events. Depth is a sharper contradiction.

Before writing or revising the outline, force every main character through this ladder:

1. What do they say they want?
2. What wound are they actually protecting?
3. How does their love help the protagonist?
4. How does the same love damage the protagonist?
5. What small action proves this contradiction without explaining it?
6. What does the protagonist learn to do in order to survive that love?
7. Which ordinary life detail makes this impossible to fake?

For the 00后三代小说 default:

- 周晓宁 is not simply "loved by three generations"; he is trained to read adults before he can read himself.
- 林倩 is not simply "busy mother"; she uses receipts and education spending as proof that she was not absent.
- 周桂芳 is not simply "grandmother who loves feeding"; she turns the child into a second chance to prove she is still useful.
- The deeper question is not "who raised the child?" but "who borrowed the child to repair their own缺口?"

If a paragraph can be replaced by "体现时代 / 表现亲情 / 三代冲突", it is too shallow.

### 2.55. Add Breath Before Adding More Weight

深度已经成立时，不要继续加物件和伤口。先问：

1. 这部 / 这章有没有一场让读者看见人物的办法真的有用？
2. 有没有一个孩子或老人能暂时舒服、好玩、安心的时刻？
3. 这个温暖是否先不被作者解释，等后文再露出代价？
4. 是否连续三场都在用纸、账、门、碗证明同一个主题？
5. 哪一场可以少一个象征物，多一个普通动作？

过门：读者必须先相信这些人真的会过日子、真的彼此有用，后面的压迫和错过才有重量。

### 2.6. Anti-Cliche Gate

Before delivering an outline, run this gate and revise until every answer is concrete:

1. What is the tempting cliche?
2. How does this outline refuse it?
3. Which character is both right and wrong at the same time?
4. Which loving action causes real damage?
5. Which scene would become cheap if explained too much?
6. What does the ending leave unresolved?
7. Which detail could only come from lived life, not from a trending topic?

For 00后三代:

- Cliche: "老人落后、父母焦虑、孩子受害."
- Refusal: 老人确实救了这个家，也确实训练了孩子察言观色；母亲确实花钱补位，也确实让孩子替她还童年债；孩子确实被爱，也确实学会逃离爱.
- Unresolved ending: 晓宁理解了他们，但不替他们结案。他开始写，是为了把自己从债里分出来, not to forgive everyone.

### 3. Apply Master Thinking, Not Mimicry

Do not imitate sentences. Use each writer as a way of seeing:

- 王安忆: daily schedule, rooms, markets, laundry, women turning fate into routine.
- 张爱玲: receipts, favors, food, debt inside love.
- 汪曾祺: hands, tools, few words, tenderness without explanation.
- 鲁迅: the cold edge inside "for your own good"; no moral lecture.
- 路遥: labor, money, unit, household pressure dragging people forward.

Avoid naming these writers in every section unless the user asks. Let their thinking shape the outline.

### 4. Quality Gate

Reject or revise any outline if:

- It reads like a year-by-year list.
- It has more than 3–4 main dramatic carriers.
- A scene's purpose is only "体现时代" or "表现亲情".
- The outline states a theme before showing the life detail that created it.
- The objects are only nostalgic labels, not things people handle, pay for, hide, wash, repair, or wait beside.
- The theme can be summarized as a common online trope, e.g. "原生家庭伤害", "父母皆祸害", "老人无私奉献", "孩子逆袭".
- The plot relies on big melodramatic incidents instead of small irreversible household choices.
- The protagonist does not face an irreversible change.
- The ending is only a summary or a judgment.
- It cannot answer: who wants what, who stops them, what cannot return?
- 主要人物没有身世来路，或身世只是履历表。
- 主要人物可以互换对白而不别扭。
- 用性格类型词代替手和嘴。
- 没有全书思想，或思想是口号。
- 没有人物开篇→终局变化，或变化只写心情。
- 性格变化没有主变、没有压变场面，或两人合同对调后仍成立。
- 没有主场背景变化，或背景只写年代标签。
- 全书只有伤害和证明，没有让爱真实成立的日常好处。
- 物件链过于整齐，读者能看出作者在用每样东西点题。

## Delivery Gate

交付总纲前，按这个顺序自检并补齐：

1. **故事能动**：谁想要什么，谁挡住，哪几次之后回不去。
2. **人能认**：遮掉姓名，三个扛戏的人仍能靠手、嘴、身世一寸分开。
3. **变化能见**：人物变化不是心情词，必须落到手、嘴、路线、物件用法。
4. **背景会挪**：主场里谁有权、谁能进门、谁能关门、哪样东西换了位置。
5. **思想不喊**：主题先从生活后果里出来，再写成刺人的问题。
6. **没有跳层**：没有正式正文、没有完整场卡、没有新矩阵。

若缺其中一项，先修总纲，不把问题推给中纲或正文。

## 00后三代 Novel Defaults

Keep these unless the user changes them:

- Engine: 三代家庭线, not news braid.
- Father: in-city work absence, not long-distance Guangdong migrant.
- News: TV sound only, not plot engine.
- Milk: daily can / water temperature / imported label only, no public scandal chapter.
- POV: third-person limited rotation; adult first-person only in epilogue.
- Scope: first write 总纲；六部与 18 大章骨架、具体场卡只在用户明确要求后继续；完整正文转 `novel-prose-from-outline`。

## Output Style

Write concise Chinese Markdown. Prefer scenes, objects, and choices over explanation.

Use short paragraphs. Do not create large tables unless comparing sources is the deliverable.

Never end with a generic "可以继续优化". If follow-up is useful, name the exact next artifact, e.g. "下一步可拆 6 部 18 大章骨架" or "下一步可为目标大章补 5–7 张因果场卡".
