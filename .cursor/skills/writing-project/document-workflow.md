# Document Workflow

## When to Use

Use for README, 产品说明, PRD, SOP, 教程, 操作手册, 课程讲义, 项目介绍, API 文档, 复盘, 调研报告, 方案, 招商资料, internal docs, and any request where clarity and reuse matter more than marketing tone.

## Intake

Before writing, identify:

- 读者: 新用户、团队成员、客户、老板、开发者、运营、合作方。
- 目标: 让读者理解、执行、决策、验收、复用还是排错。
- 已知材料: 需求、代码、草稿、会议纪要、截图、数据、口头描述。
- 输出形态: README、教程、方案、SOP、报告、FAQ、清单。
- 约束: 长度、语气、必须包含/不能包含的内容。

Ask only when missing information would change the document structure. Otherwise state assumptions and proceed.

## Structure by Document Type

### README / 项目说明

Use:

```markdown
# [项目名]

一句话说明它解决什么问题。

## 适合谁

## 核心能力

## 快速开始

## 使用流程

## 常见问题

## 后续计划
```

### SOP / 操作手册

Use:

```markdown
# [任务] SOP

## 目标

## 适用范围

## 准备材料

## 操作步骤

## 验收标准

## 常见异常与处理

## 记录模板
```

### 教程 / 课程

Use:

```markdown
# [主题]教程

## 你会学到什么

## 前置知识

## 第一步: [动作]

## 第二步: [动作]

## 示例

## 练习

## 常见错误
```

### 方案 / 报告

Use:

```markdown
# [主题]方案

## 结论摘要

## 背景与问题

## 目标

## 方案设计

## 执行计划

## 风险与对策

## 需要确认的问题
```

## Writing Rules

- Start with the reader's job-to-be-done, not the author's background.
- Put the conclusion before detail when the reader needs to decide.
- Put steps before theory when the reader needs to execute.
- Use examples for abstract concepts.
- Use checklists for repeatable work.
- Use warnings only for costly or common mistakes.
- Do not fill gaps with invented facts. Mark TODOs clearly.

## Revision Workflow

When editing an existing document:

1. Preserve useful structure and user-provided facts.
2. Fix unclear hierarchy before polishing sentences.
3. Remove repetition and vague claims.
4. Add missing examples, prerequisites, or acceptance criteria.
5. Return a concise change summary plus the revised document.

## Definition of Done

A document is done when:

- A new reader can identify the purpose within 10 seconds.
- The main action path is unambiguous.
- Headings form a usable outline.
- Examples and edge cases cover likely confusion.
- Open questions are marked instead of hidden.
