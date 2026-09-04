# Source Registry

Use this registry to decide where content intelligence can come from before writing.

## Event And Hotness Sources

### General Chinese Hot Lists

- DailyHotApi: multi-platform hot list aggregation, useful for Weibo, Baidu, Zhihu, Toutiao, IT news, 36Kr, The Paper, and other public signals.
- TrendRadar: useful if a future self-hosted monitor needs keyword filtering, RSS support, AI summaries, and push notifications.
- RSSHub: useful for turning public sites into RSS sources when a direct API is unavailable.

### 今日头条

- DailyHotApi `toutiao` source: use as a hot-list signal when available.
- Apify Toutiao Scraper: use when structured fields such as rank, hot value, category, thumbnail, topic URL, and collected time are needed.
- Public Toutiao pages: use only when accessible without login and without bypassing anti-scraping.

### 小红书

- SpiderHubs Xiaohongshu hot list API: use when an API key is available.
- Just One API Xiaohongshu keyword suggestions and note search: use when an API key is available.
- NewRank / 新红数据: use for professional Xiaohongshu data analysis when subscribed.
- Public web search: fallback when no API key exists.
- User-provided screenshots, exported notes, or manual observations: highest reliability when they come from the user's own account.

## Image Sources

### Preferred

- User-owned photos, screenshots, designs, and generated images.
- Generated covers, knowledge cards, comparison cards, and diagrams created specifically for this account.

### Public Libraries

- Pexels: good default for free commercial photos/videos; supports `locale=zh-CN`.
- Unsplash: strong photographic quality; use with attribution when possible.
- Pixabay: useful for photos, vectors, and illustrations.
- Wikimedia Commons: useful for historical, scientific, cultural, and public-reference articles; check each file's license.

## Fallback Rules

- If platform-specific APIs are unavailable, use public web search and record sources manually in `references/sources/`.
- If image rights are unclear, mark the image as `reference only` and create a replacement plan.
- If a hot-list item lacks a reliable source, treat it as a topic signal, not as a factual source.
- For sensitive areas, require a high-reliability source before drafting: finance, health, policy, education, eldercare, and legal claims.

## Record Destination

- Event records: `materials/events/`
- Raw notes: `materials/raw-notes/`
- Public source records: `references/sources/`
- Benchmark teardowns: `references/benchmarks/`
- Image plans: `assets/image-plans/`
- Cover plans: `assets/cover-plans/`
- Layout structures: `assets/layouts/`
