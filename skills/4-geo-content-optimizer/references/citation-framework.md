# GEO Citation Framework

## The Core Principle

AI systems cite content when they:
1. **Trust** the source (authority signals)
2. **Understand** the content (clarity signals)
3. **Find** the specific information needed (retrievability signals)

The GEO Citation Framework optimizes for all three.

## The 8 Citation Signals

### 1. Direct Answer First

**Why it matters**: AI systems extract answers, not read articles. The first sentences are heavily weighted.

**Implementation**:
- Answer the core question in sentence 1
- Provide context in sentence 2
- Expand with details in paragraph 2+

**Example**:

❌ **Weak opening**:
> "In recent years, the field of artificial intelligence has seen tremendous growth. Many companies are now exploring how AI can transform their operations. One area of particular interest is..."

✅ **Strong opening**:
> "Retrieval-Augmented Generation (RAG) is an AI architecture that combines large language models with external knowledge retrieval to produce more accurate, current answers. Unlike standalone LLMs, RAG systems can access up-to-date information from databases, documents, and APIs."

**Checklist**:
- [ ] First sentence answers "what is X?" or "how does Y work?"
- [ ] No throat-clearing ("In today's world...", "As we all know...")
- [ ] Entity named explicitly in first 10 words

---

### 2. Entity-Rich Content

**Why it matters**: AI systems use entity recognition to understand topics and relationships. More entities = better semantic understanding.

**Key Entities to Include**:

| Entity Type | Examples |
|-------------|----------|
| **Brand** | Your company name, product names |
| **People** | Full names with titles/roles |
| **Products** | Specific product names with versions |
| **Technologies** | Frameworks, platforms, protocols |
| **Locations** | Cities, countries (with context) |
| **Organizations** | Partners, competitors, standards bodies |
| **Dates** | Specific dates, not "recently" |
| **Numbers** | Statistics, counts, percentages |

**Implementation**:

❌ **Entity-poor**:
> "Our tool helps teams work better together."

✅ **Entity-rich**:
> "Notion 3.0 helps product teams at Spotify, Figma, and Duolingo collaborate on roadmaps, documentation, and wikis in a unified workspace."

**Entity Density Target**: 1 named entity per 50 words minimum.

---

### 3. Structured Format

**Why it matters**: Structured content helps AI parse information hierarchy and relationships.

**Structural Elements**:

| Element | Use For | GEO Impact |
|---------|---------|------------|
| **H2 headers** | Major sections | High |
| **H3 headers** | Subsections | High |
| **Bullet lists** | Related items | Medium |
| **Numbered lists** | Sequential steps | Medium |
| **Tables** | Comparisons, data | High |
| **Blockquotes** | Key statements | Medium |
| **Bold text** | Important terms | Low |

**Header Best Practices**:
- Every 300-500 words should have a header
- Headers should be descriptive (not "Introduction" but "What is GEO?")
- Use sentence case or title case consistently

---

### 4. Fact-Dense Content

**Why it matters**: AI systems prioritize factual, verifiable information.

**Types of Facts to Include**:

| Type | Example |
|------|---------|
| **Statistics** | "According to Gartner, 70% of enterprises..." |
| **Dates** | "Released in March 2024, the new model..." |
| **Specific numbers** | "Processes 10,000 requests per second" |
| **Named sources** | "Research from Stanford HAI shows..." |
| **Comparisons** | "3x faster than the previous version" |

**Citation Format**:
- Inline: "According to [Source], X% of..."
- Parenthetical: "X% of users prefer Y (Source, 2024)"
- Footnote-style for longer lists

**Warning**: Don't include facts without sources. AI systems check for source credibility.

---

### 5. FAQ Formatting

**Why it matters**: FAQ format matches how AI systems answer questions directly.

**Structure**:
```markdown
## Frequently Asked Questions

**Q: [Exact question users ask]?**

A: [Direct, comprehensive answer that could stand alone]
```

**Best Practices**:
- Match question phrasing to actual search queries
- Answer should be complete (can be extracted without context)
- Include 2-5 FAQs per page minimum
- Place FAQs near the bottom or in a dedicated section

**Question Sources**:
- "People also ask" from Google
- AnswerThePublic query data
- Customer support tickets
- Sales call questions

---

### 6. Definition Clarity

**Why it matters**: AI systems use definitions to disambiguate and categorize content.

**Definition Block Format**:

```markdown
**[Term]**: [Category] that [unique differentiator].

**Example**:
**Large Language Model (LLM)**: A type of artificial intelligence system that uses deep learning to understand, generate, and manipulate human language.
```

**Placement**:
- First mention of key term
- Before using the term in explanations
- In a dedicated "Key Terms" section for complex topics

---

### 7. Unique Data

**Why it matters**: AI systems prioritize original sources over recycled content.

**Types of Unique Data**:

| Type | Value |
|------|-------|
| **Original research** | Surveys, studies, experiments |
| **First-hand accounts** | Case studies, interviews |
| **Proprietary data** | Usage statistics, performance metrics |
| **Expert insights** | Unique perspectives from practitioners |
| **Timely updates** | Breaking news, recent developments |

**How to Signal Uniqueness**:
- "Our analysis of 1M websites shows..."
- "In our 2024 customer survey..."
- "Based on interviews with 50 CTOs..."
- "Internal data from our platform..."

---

### 8. Authoritative Voice

**Why it matters**: AI systems assess confidence and authority in language.

**Hedging vs. Declarative**:

| Hedging (Weak) | Declarative (Strong) |
|----------------|----------------------|
| "might be" | "is" |
| "could potentially" | "does" |
| "some experts believe" | "research demonstrates" |
| "it seems that" | [remove] |
| "is often considered" | "is recognized as" |
| "may help" | "improves" |

**Exceptions**: It's okay to hedge when:
- Discussing future predictions
- Addressing uncertainty in research
- Comparing subjective preferences

**Authoritative Phrases**:
- "Data shows..."
- "Research demonstrates..."
- "Analysis reveals..."
- "Evidence indicates..."
- "Studies confirm..."

---

## The Citation Funnel

Not all content gets cited. The funnel looks like:

```
All Content (100%)
    ↓
AI-Accessible (30%) — crawlable, not blocked
    ↓
AI-Readable (10%) — clear structure, no ambiguity
    ↓
AI-Trustworthy (5%) — authoritative, sourced, factual
    ↓
AI-Citable (1%) — matches query, direct answer, entity-rich
```

The GEO framework moves content down this funnel.

---

## Measuring Success

### Leading Indicators (Weeks 1-4)
- Content audit scores improving
- Page structure following framework
- Entity density increasing

### Lagging Indicators (Months 2-6)
- Brand mentions in AI responses
- "According to [Your Brand]" citations
- Traffic from AI platforms (if trackable)

### Tracking Brand Mentions

Manual check:
1. Ask ChatGPT/Claude/Perplexity about your topic
2. Note if/when your brand is cited
3. Track over time

Automated (advanced):
- Use Perplexity API to query your topic area
- Monitor for brand mentions
- Log citation context

---

## Common Anti-Patterns

❌ **Marketing speak**: "Revolutionary game-changing solution"  
✅ **Factual**: "Cloud-based project management tool"

❌ **Vague claims**: "Many companies use our product"  
✅ **Specific**: "Used by 10,000+ companies including Stripe, Shopify, and Notion"

❌ **Self-referential**: "Our blog post explains..."  
✅ **Standalone**: "This guide covers..."

❌ **Jargon without definition**: "Implement the CQRS pattern"  
✅ **Accessible**: "Command Query Responsibility Segregation (CQRS): separate read and write operations"

❌ **Wall of text**: 500 words without headers  
✅ **Scannable**: Headers every 200-300 words, lists for related items