# Quality Gates

## Universal QA

Before delivery, check:

- **Intent match**: output solves the user's requested job, not a nearby task.
- **Audience match**: examples, vocabulary, and detail level fit the target reader.
- **Opening strength**: first paragraph gives a reason to continue.
- **Specificity**: concrete scenes, examples, steps, numbers, or criteria replace vague praise.
- **Structure**: headings and paragraph order create a clear reading path.
- **Claims**: factual claims are sourced, user-provided, or framed as assumptions.
- **Action**: ending tells the reader what to do, think, try, comment, or read next.

## Platform QA

### 小红书

- Title creates curiosity or clear value without fake urgency.
- Cover text is short enough to fit on an image.
- Body reads like lived experience or useful guidance, not a press release.
- Each bullet has a point and a payoff.
- Tags match the content and user intent.
- No exaggerated effect claims, fake before/after, medical/financial guarantees, or invented personal experience.

### 今日头条

- Headline matches the actual argument.
- First 200 words establish the event, conflict, or reader benefit.
- Claims and opinions are separated.
- The article has a visible logic chain: fact → interpretation → implication.
- The ending invites discussion without provoking hostility.
- No unsourced accusations, rumor amplification, or misleading certainty.

## Fiction QA

Use after the `storygen` workflow:

- The protagonist has a clear want, obstacle, and pressure.
- Scenes are causal, not just sequential.
- Each scene changes story state.
- Character choices are earned by prior setup.
- World rules and timeline remain consistent.
- Ending resolves the central promise or deliberately reframes it.

## Document QA

- Reader can understand the purpose immediately.
- Required context appears before steps that depend on it.
- Procedures have acceptance criteria.
- Abstract ideas include examples.
- TODOs and assumptions are explicit.
- The document can be reused without reading the chat.

## Revision Loop

If QA fails:

1. Name the top 1-3 problems.
2. Revise structure before polishing language.
3. Recheck the same failed gates.
4. Stop when remaining issues are only taste-level preferences or require new source material.
