# 中文写作项目

这个仓库按三条产品线分开：小红书、今日头条、番茄。资料库和写作稿不混放。

## 先看哪

| 你要做什么 | 去哪 |
|---|---|
| 写 00 后三代小说 | [`番茄/00hou-sandai/`](番茄/00hou-sandai/) |
| 查事件卡、人设卡 | [`content-intelligence/research/`](content-intelligence/research/) |
| 写小红书 | [`小红书/`](小红书/) |
| 写今日头条 | [`今日头条/`](今日头条/) |
| 找 skill | [`.cursor/skills/README.md`](.cursor/skills/README.md) |

## 目录

```text
小红书/                      账号、选题、草稿、复盘
今日头条/                    账号、选题、草稿、复盘
番茄/                        小说工程（现行稿）
content-intelligence/        共享资料，不是成品
  research/                  事件库、人设库、提示词、调研
  source-registry.md         平台热度与图源
tools/                       脚本，以及 storygen 上游副本
.cursor/skills/              写作与研究工作流
```

一次性平台选题仍可用根目录的 `content-brief.md`、`style-guide.md`。小说状态只写在 `番茄/00hou-sandai/story-bible.md`，不要再在根目录另开一份。

## 三条线怎么调用

```text
使用 novel-master-outline，按家庭现实主义把 00 后三代总纲往下拆一档。
```

```text
使用 xhs-hot-ai-workflow，给这个账号写一篇笔记：……
```

```text
使用 toutiao-hot-career-education，写一篇 1500 字深度文：……
```

```text
使用 writing-project，把这些素材整理成项目说明。
```

小说总纲、风格分写、中纲，走 `novel-master-outline` 和对应 `novel-style-*`。`storygen` 只在用户明确要求 Braintrust 评审或另开一部新故事时再用。
