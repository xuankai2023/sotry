# 项目 Skill

按产品线用，不要混调用。用户已点名交付物时，只读那一个 skill，不要先读总控再连环读。

## 进场

自动候选只留给当前会用到的入口。备用风格、旧库、Braintrust 要点名才读（`disable-model-invocation`）。

| 用户要 | 只读 |
|---|---|
| 写正文 / 续写 / 改章节正文 | `novel-prose-from-outline` |
| 写中纲 | `novel-mid-outline` |
| 写细纲 | `novel-fine-outline` |
| 写场卡 / 大章纲 | `novel-chapter-structure` → 现行书再读 `novel-chapter-family-realism` |
| 短故事 | `fanqie-short-story` |
| 某账号方向 | 对应 `xhs-*` / `toutiao-*` |
| 频道不清 / 选账号 | `writing-project` |
| 工作流还缺哪一层 | `novel-workflow` |

00 后冻结和 6000 字日更是 rule，只在 `番茄/00hou-sandai/`（正文日更只在 `正文/`）打开时生效，不要套到《差不多》。

手动点名：7 套备用 `novel-style-*` / `novel-chapter-*`、`storygen`、`events-00hou-parents`、`events-00hou-grandparents`、`xiaohongshu-growth`、`toutiao-growth`。

## 总控

| Skill | 干什么 |
|---|---|
| `writing-project` | 判断类型，再转到对应 skill |

## 番茄短故事

和长篇不要混用。工程在 `番茄/短故事/`。

| Skill | 干什么 |
|---|---|
| `fanqie-short-story` | 入口。正式流程在 `番茄/短故事/skill/SKILL.md` |

## 小说

不要混用。总纲是总纲，章节是章节。先整体后局部，顺序见 `novel-workflow`。短故事不走下面这些 skill。

| Skill | 干什么 |
|---|---|
| `novel-workflow` | 思维导图总控：整体→局部描写→文章落实；每个节点对应下面一个 skill |
| `novel-master-outline` | 全书总纲 / 六部与大章骨架；人物必须写成人物志；必须写思想、性格变化、背景变化 |
| `novel-mid-outline` | 中纲：一部或一段大章的总结；框架、多线、伏笔、人物网、本部分性格进/出、声音、卡点 |
| `novel-style-family-realism` | 现行书默认风格总纲。另外七套要点名才读 |
| `novel-character-craft` | 性格、身世、手、嘴、年段；总纲人物志与大章本章人物 |
| `novel-character-change` | 总纲/中纲直接使用：开篇→终局性格变化骨头；中纲只挪本部分一寸 |
| `novel-chapter-structure` | 区分部、大章、场；规划三圈、因果、状态变化、本章人物；必须写本章思想与人/背景变化 |
| `novel-chapter-family-realism` | 现行书默认场卡/大章纲。另外七套要点名才读 |
| `novel-fine-outline` | 细纲：把已锁场卡按日切开，每拍手 / 物 / 嘴 / 停在；不写正文，不改场序 |
| `novel-thought-ground` | 描写层合同：思想、人物变化、背景变化必须在人/场/物描写时写出来 |
| `novel-article-assemble` | 按已锁架构和材料拼「某人遇见什么」的文章包；必须打开材料、抄三栏；不写正式正文，不改冻结矩阵 |
| `novel-prose-from-outline` | 按照中纲、细纲、场卡写正文；按日切配额写满；必须跑计数脚本、批注校验并回填 Scene ledger |
| `novel-chapter-prose` | 正文质量门与禁搬门；写正文转 `novel-prose-from-outline` |
| `novel-material-*` | 生成特定材料或语气样本；每条须带思想落地三栏；不排章、不写正式完整正文 |
| `storygen` | 用户明确要求 Braintrust 时才读 |

备用章法仍在：`urban-daily` / `psychological-debt` / `restrained-hands` / `labor-social` / `critical-realism` / `cold-absurd` / `warm-growth`。要点名或换书时再读。

一本只走一条风格竖线。现行书按家庭现实主义写。

现行开写《差不多》在 `番茄/90hou-chabuduo/`。00 后三代在 `番茄/00hou-sandai/`，正文已停；用户没点名不要重写。

现行 00 后三代尺度：6 部、18 大章、每章 5–7 场；一房、一钟、一物、一动作约束场，大章承担不可逆。《差不多》：36 大章，一天 7000，普通章 3 日约 21000。

## 研究生产

| Skill | 干什么 |
|---|---|
| `events-00hou-2021-2026` | 2021–2026 少年 / 父母 / 祖辈三本一起写或优化；一次一年 |
| `events-00hou-2011-2020` | 2011–2020 少年 / 父母 / 祖辈三本一起写或优化；一次一年 |
| `events-00hou-parents` | 2000–2010 父母事件卡；要点名 |
| `events-00hou-grandparents` | 2000–2010 祖辈事件卡；要点名 |

## 小红书 / 今日头条

方向级 `xhs-*`、`toutiao-*` 负责对应账号。`xiaohongshu-growth`、`toutiao-growth` 只作方向索引，不写正文。
