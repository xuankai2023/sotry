# LangGraph Mapping

This project currently uses Cursor skills and files as a LangGraph-ready state machine. Do not add LangGraph code until the workflow is stable for at least 1-2 weeks of manual runs.

## State Fields

Future LangGraph state can map to these fields:

- `account_id`: direction skill id, such as `xhs-hot-ai-workflow`.
- `account_path`: bound account library path.
- `reader`: target reader and pain.
- `goal`: traffic, follower growth, save rate, discussion, or review update.
- `event_scan`: current events, hot topics, seasonal hooks, and source links.
- `hotness_signal`: timeliness, search rise, discussion value, or platform trend.
- `source_material`: facts, cases, raw notes, references, image references, and assumptions.
- `source_reliability`: high / medium / low rating for each important source.
- `keyword_plan`: core keyword, long-tail terms, and title keyword placement.
- `angle`: selected angle and rejected alternatives.
- `attraction_plan`: title hook, opening hook, retention frame, rhythm hooks, share trigger, and visual packaging.
- `layout_plan`: section order, card/page structure, visual rhythm, and callouts.
- `image_plan`: image count, placement, purpose, caption, source, ownership, and risk.
- `draft`: current draft.
- `review_a_score`: growth/platform reviewer score.
- `review_b_score`: credibility/reader-value reviewer score.
- `arbitration`: pass/fail decision and rewrite target.
- `asset_pack`: reusable titles, cover copy, image prompts, tags, CTAs, layouts, and scripts.
- `record_updates`: files to create or update.

## Node Mapping

- `LoadMemory`: read account bible, reader persona, topic bank, keyword map, calendar, materials, references, assets, and reviews.
- `EventAndHotnessScan`: collect events from local `materials/events/`; if insufficient, use approved hot-list APIs or web search.
- `ResearchAndMaterialCheck`: verify source reliability and flag missing evidence.
- `DirectionFitScoring`: score reader fit, keyword fit, timeliness, visual potential, and risk.
- `AngleSelection`: choose one angle and record rejected alternatives.
- `AttractionPlan`: create hook, opening, structure, rhythm, share trigger, and visual packaging plan.
- `OutlineOrLayoutPlan`: create article/card layout before drafting.
- `Draft`: writer model generates the draft.
- `LayoutAndImagePlan`: prepare image placement, captions, cover concept, and rights status.
- `ReviewerAScore`: platform-growth reviewer.
- `ReviewerBScore`: credibility and reader-value reviewer.
- `ScoreArbitration`: decide pass, rewrite, return to angle, or return to research.
- `RewriteOnceIfNeeded`: bounded rewrite loop.
- `PackageAssets`: extract reusable publishing assets.
- `SaveDraft`: write draft path and update recommendations.
- `AfterPublishReview`: analyze published data.
- `UpdateMemory`: write durable learnings back to files.

## Future Execution Model

1. Scheduled collector runs daily or hourly.
2. Collector writes events and sources into each account library.
3. Direction matcher chooses candidate accounts for each event.
4. Direction skill drafts content.
5. Two reviewers score independently.
6. Human approves before publishing.
7. Published data is added to reviews.
8. UpdateMemory writes durable lessons back to account files.

## Checkpoint Rules

- Human approval is required before publishing.
- Human approval is required before using any image with unclear rights.
- If source reliability is low, the graph must pause or return to research.
- If reviewer disagreement exceeds 15%, the graph must enter arbitration.
- If rewrite fails once, the graph returns to angle or research instead of continuing.
