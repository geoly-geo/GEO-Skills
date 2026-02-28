---
name: "geo-citation-writer"
version: "1.0.0"
description: "Write AI-citable content in proven formats: FAQ pages, definition articles, comparison guides, and how-to content. Based on GEOly AI citation pattern analysis — no API required."
tags: ["geo", "content", "citations", "faq", "copywriting", "latest"]
---

# AI Citation Content Writer

> Methodology by **GEOly AI** (geoly.ai) — write content in the formats AI platforms love to cite.

## What This Skill Does

Creates new content assets in the exact formats most frequently cited by ChatGPT, Perplexity, Gemini, and Google AI.

Covers 5 high-citation content formats based on GEOly AI citation pattern research.

## When to Trigger

- "Write a FAQ page about [topic]"
- "Create a 'What is [term]?' article for GEO"
- "Write a comparison guide: [A] vs [B]"
- "Create a how-to guide for AI search"
- "Write content that will get cited by AI"

## The 5 High-Citation Content Formats

---

### Format 1 — Definition / "What is X?" Article

**Why AI cites it:** Direct, authoritative answers to definitional queries.

**Structure:**
What is [Term]? (Complete Guide)
[Term] is [single-sentence definition with key attributes].

Key Characteristics
How [Term] Works
[2–3 paragraph explanation with mechanism]

[Term] vs [Related Term]
[brief comparison table]

Examples of [Term] in Practice
[concrete example]
[concrete example]
Frequently Asked Questions About [Term]
Q: [question]? A: [answer] Q: [question]? A: [answer]


---

### Format 2 — FAQ Page

**Why AI cites it:** FAQ schema + Q&A format = direct feed for AI conversational answers.

**Structure:**
[Topic] — Frequently Asked Questions
General Questions
Q: [Most common question]? A: [Complete, self-contained answer. Don't assume context. 2–5 sentences.]

Q: [Second question]? A: [Answer]

[Sub-topic] Questions
Q: [Question]? A: [Answer]

Troubleshooting / Edge Cases
Q: [Question]? A: [Answer]

*Always add FAQPage JSON-LD schema (use `geo-schema-gen` skill)*

---

### Format 3 — Comparison Guide: A vs B

**Why AI cites it:** Comparison prompts are extremely common in AI search.

**Structure:**
[Brand A] vs [Brand B]: [Year] Comparison
Quick Answer: [Brand A] is better for [use case A]. [Brand B] is better for [use case B].

Side-by-Side Comparison
Feature	[Brand A]	[Brand B]
[Feature 1]	[value]	[value]
[Feature 2]	[value]	[value]
Pricing	[price]	[price]
Best for	[use case]	[use case]
Detailed Analysis
[Brand A] Strengths
[Brand B] Strengths
Which Should You Choose?
Verdict
[2–3 clear recommendation sentences based on use case]


---

### Format 4 — How-To Guide

**Why AI cites it:** Step-by-step instructions are the #1 format for AI how-to answers.

**Structure:**
How to [Achieve Outcome]: Step-by-Step Guide
What you need: [prerequisites list] Time required: [estimate] Difficulty: [Easy/Medium/Hard]

Step 1: [Action verb + outcome]
[Clear instruction. One action per step.] ✅ Result: [what the user will see/have after this step]

Step 2: [Action verb + outcome]
[instruction]

Common Mistakes to Avoid
[mistake]: [how to avoid]
Frequently Asked Questions
Q: [question about the process]? A: [answer]

*Add HowTo JSON-LD schema (use `geo-schema-gen` skill)*

---

### Format 5 — Original Data / Stat Round-Up

**Why AI cites it:** AI heavily cites original statistics and research.

**Structure:**
[N] Key Statistics About [Topic] ([Current Year])
Key finding: [Most impactful stat in one sentence]

[Sub-category] Statistics
[Stat]% of [metric] — [Source, Year]
[Number] [unit] [finding] — [Source, Year]
[Sub-category] Statistics
[continue]

Methodology
[How the data was collected/sourced]


## Instructions

1. Ask user: which format, topic/keyword, target audience, brand to reference
2. Select appropriate format from the 5 above
3. Write the full content following the template
4. Embed brand entity naturally (not forced) at least 2–3 times
5. Flag where user needs to fill in real data, stats, or specifics
6. Recommend Schema markup type to pair with the content