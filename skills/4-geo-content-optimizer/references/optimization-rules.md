# Optimization Rules — Complete Reference

## Rule 1: Lead with the Answer

### Principle
The first sentences of your content receive the highest weight from AI systems. Don't waste them.

### The Pattern

**Formula**: [Direct Answer] + [Brief Context] + [Value Promise]

### Examples by Content Type

#### Article Opening

❌ **Weak**:
> Content marketing has evolved significantly over the past decade. With the rise of digital platforms, brands are constantly seeking new ways to reach their audiences. One approach that has gained traction recently...

✅ **Strong**:
> Content marketing generates 3x more leads than traditional marketing at 62% lower cost, according to Demand Metric. Unlike interruptive advertising, content marketing attracts customers by providing valuable information that solves their problems.

**What changed**:
- Immediate statistic (3x, 62%)
- Clear definition
- Named source (Demand Metric)
- Specific comparison

#### Product Page Opening

❌ **Weak**:
> Welcome to our product page. We're excited to introduce you to our latest offering. This product has been designed with our customers in mind...

✅ **Strong**:
> Notion is an all-in-one workspace for notes, tasks, wikis, and databases. Used by 30 million users including teams at Figma, Pixar, and McDonald's, it replaces scattered documents and apps with a single, flexible platform.

**What changed**:
- Product category defined
- Key features listed
- Usage data (30 million)
- Named customers
- Clear value proposition

#### FAQ Answer Opening

❌ **Weak**:
> That's a great question. Many people wonder about this topic. The answer depends on several factors...

✅ **Strong**:
> Yes, you can integrate Slack with over 2,400 third-party apps including Google Drive, Zoom, and Salesforce. The Slack App Directory includes both native integrations and custom workflows built by the community.

**What changed**:
- Direct yes/no answer
- Specific number (2,400)
- Named examples
- Additional context

---

## Rule 2: Add Definition Blocks

### Principle
AI systems categorize content by understanding key entities. Explicit definitions improve categorization accuracy.

### When to Define

| Scenario | Example |
|----------|---------|
| First mention of technical term | "API (Application Programming Interface): ..." |
| Industry jargon | "SaaS (Software as a Service): ..." |
| Your product name | "[Product]: A [category] that [key differentiator]" |
| Abbreviations | "GEO (Generative Engine Optimization): ..." |
| New concepts | "Zero-click search: ..." |

### Definition Formula

**Format**: **[Term]**: [Category] that [unique differentiator/key function].

### Examples

✅ **Good definitions**:

> **Large Language Model (LLM)**: A type of AI system that uses deep learning to understand and generate human language, trained on billions of text examples.

> **Retrieval-Augmented Generation (RAG)**: An AI architecture that combines language models with external knowledge sources to produce more accurate, current answers than standalone models.

> **Figma**: A collaborative design tool that allows multiple users to edit designs simultaneously in the browser, eliminating version control issues.

❌ **Weak definitions**:

> **Figma**: A great design tool that's really popular. *(Vague, no category)*

> **RAG**: Something AI companies use to make answers better. *(No technical precision)*

> **LLM**: Large Language Models are AI models that are large and use language. *(Circular)*

---

## Rule 3: Structure with Headers

### Principle
Headers create an information hierarchy that helps AI parse content structure and relationships.

### Header Hierarchy

```
H1: Page title (one only)
├── H2: Major section
│   ├── H3: Subsection
│   └── H3: Subsection
├── H2: Major section
│   ├── H3: Subsection
│   │   └── H4: Detail (rare)
│   └── H3: Subsection
└── H2: Major section
```

### Header Density

| Content Length | H2 Count | H3 Count |
|----------------|----------|----------|
| 500 words | 2-3 | 2-4 |
| 1000 words | 3-5 | 4-8 |
| 2000 words | 5-8 | 8-15 |

### Header Best Practices

1. **Be Descriptive**: Not "Introduction" but "What is [Topic]?"
2. **Include Keywords**: Help AI categorize
3. **Use Consistent Format**: Sentence case OR Title case
4. **Make Scannable**: Headers alone should tell the story

### Examples

❌ **Weak structure**:
```markdown
# Our Product

We built this product to help people...

It has many features like...

You can use it for...

Many customers have seen...
```

✅ **Strong structure**:
```markdown
# Project Management Software for Remote Teams

## What is [Product]?

### Core Purpose
### Key Differentiators

## Key Features

### Task Management
### Time Tracking
### Team Collaboration
### Reporting & Analytics

## Use Cases

### For Startups
### For Agencies
### For Enterprise

## Customer Results

### Case Study: [Company]
### Case Study: [Company]
```

---

## Rule 4: Convert to FAQ Format

### Principle
FAQ format matches how AI systems answer questions. Content in Q&A format is more likely to be extracted.

### FAQ Placement

| Location | Use When |
|----------|----------|
| Dedicated FAQ page | 10+ questions |
| End of article | 3-5 questions related to topic |
| Product page | Addressing objections |
| Section within content | Clarifying complex topic |

### Question Sources

1. **Google "People also ask"**
2. **AnswerThePublic queries**
3. **Customer support tickets**
4. **Sales call questions**
5. **Forum discussions**
6. **Competitor FAQs**

### Question Quality Criteria

✅ **Good questions**:
- Match actual search queries
- Specific and focused
- Can be answered definitively
- Have search volume

❌ **Weak questions**:
- Too broad ("What is everything?")
- Too specific to one user
- Already answered in main content
- Hypothetical/rare scenarios

### Answer Structure

**Formula**: [Direct answer] + [Explanation] + [Example/Data] + [Link to resource]

### Example FAQ Block

```markdown
## Frequently Asked Questions

**Q: How does [Product] compare to [Competitor]?**

A: [Product] offers 3x faster processing than [Competitor] at 40% lower cost, according to our 2024 benchmark testing. While both tools support basic [function], [Product] includes advanced features like [feature 1] and [feature 2] that [Competitor] lacks. See our [detailed comparison guide] for feature-by-feature analysis.

**Q: What security certifications does [Product] have?**

A: [Product] is SOC 2 Type II certified, GDPR compliant, and maintains ISO 27001 certification. We undergo annual third-party security audits and encrypt all data at rest and in transit. Our security documentation includes penetration test results and compliance reports available to enterprise customers.

**Q: Can I migrate from [Alternative] to [Product]?**

A: Yes, [Product] includes a one-click migration tool for [Alternative] that transfers projects, tasks, and user data in under 10 minutes. Our migration support team handles enterprise migrations personally, with zero downtime guaranteed. Over 5,000 teams have successfully migrated from [Alternative] in 2024.
```

---

## Rule 5: Add Data Points

### Principle
Specific numbers increase credibility and give AI concrete facts to cite.

### Types of Data

| Type | Example | Source |
|------|---------|--------|
| **Statistics** | "72% of enterprises..." | Research firm |
| **Counts** | "Used by 10,000+ companies" | Internal data |
| **Rates** | "Processes 10,000 req/sec" | Benchmark |
| **Comparisons** | "3x faster than..." | Testing |
| **Dates** | "Released March 2024" | Product info |
| **Monetary** | "Starting at $29/month" | Pricing |

### Data Integration Patterns

**Inline citation**:
> According to McKinsey's 2024 AI adoption report, 72% of enterprises have implemented AI in at least one function, up from 55% in 2023.

**Parenthetical**:
> Enterprise AI adoption has accelerated significantly (McKinsey, 2024), with 72% of large companies now using AI in production.

**Data callout**:
```markdown
**Key Statistic**

Organizations using [Product] see:
- 47% reduction in time-to-market
- 3.2x improvement in deployment frequency
- 99.9% uptime SLA
```

### Data Density Targets

| Content Type | Data Points per 500 words |
|--------------|---------------------------|
| Article | 3-5 |
| Product page | 5-10 |
| Case study | 10-15 |
| FAQ | 1-2 per answer |

---

## Rule 6: Entity-First Writing

### Principle
Named entities (brands, people, products, places) help AI understand context and relationships.

### Entity Types to Include

| Type | Priority | Example |
|------|----------|---------|
| **Brand name** | 🔴 Critical | Your company/product |
| **People** | 🟡 High | Authors, executives, experts |
| **Products** | 🟡 High | Your products + competitors |
| **Technologies** | 🟡 High | Frameworks, platforms |
| **Companies** | 🟡 High | Customers, partners |
| **Locations** | 🔵 Medium | Cities, countries |
| **Dates** | 🔵 Medium | Specific timestamps |
| **Numbers** | 🔵 Medium | Statistics, counts |

### Entity Density

**Target**: 1 named entity per 50 words minimum.

**Example calculation**:
- 500-word article → 10+ named entities
- 1000-word article → 20+ named entities

### Entity-First Examples

❌ **Entity-poor** (2 entities in 50 words):
> Our platform helps teams work better. The solution provides many features that improve productivity. Companies can use our tools to collaborate.

✅ **Entity-rich** (8 entities in 50 words):
> Slack, used by 30 million people at companies like IBM, Airbnb, and Shopify, integrates with 2,400+ apps including Google Drive, Zoom, and Salesforce. The platform, launched in 2013 by Stewart Butterfield, supports real-time messaging, file sharing, and video calls.

---

## Rule 7: Remove Hedging

### Principle
AI systems assess confidence. Declarative statements signal authority.

### Hedging Language to Remove

| Hedging Phrase | Replace With |
|----------------|--------------|
| "might be" | "is" |
| "could potentially" | "does" |
| "some experts believe" | "research shows" |
| "it seems that" | [remove] |
| "is often considered" | "is recognized as" |
| "may help" | "improves" |
| "probably" | [remove or specify odds] |
| "in our opinion" | [remove or cite evidence] |
| "arguably" | [remove] |
| "to some extent" | [remove] |

### Before/After Examples

| ❌ With Hedging | ✅ Declarative |
|----------------|----------------|
| "SEO might be important for AI search" | "SEO is essential for AI search visibility" |
| "This tool could potentially improve productivity" | "This tool improves productivity by 34%" |
| "Some studies suggest that content length matters" | "Backlinko's 2024 study of 11.8M pages found average top-ranking content is 1,447 words" |
| "It seems that structured data helps AI understanding" | "Schema.org markup increases AI citation rates by enabling precise entity recognition" |

### When Hedging is OK

1. **Future predictions**: "We expect AI adoption to grow"
2. **Uncertain research**: "Early studies suggest..."
3. **Subjective preferences**: "Many users prefer..."
4. **Legal caution**: Required disclaimers

---

## Rule 8: Format for Scannability

### Principle
AI systems parse structure before content. Scannable formatting improves parsing accuracy.

### Scannable Elements

| Element | Use For | Implementation |
|---------|---------|----------------|
| **Bullet lists** | 3-7 related items | Parallel structure |
| **Numbered lists** | Sequential steps | Imperative verbs |
| **Tables** | Comparisons, data | Clear headers |
| **Bold text** | Key terms, important points | Sparingly |
| **Blockquotes** | Important statements | One per section max |
| **Code blocks** | Technical examples | Syntax highlighting |

### Format Examples

**Bullet list** (parallel structure):
- Increases page load speed by 40%
- Reduces server costs by $500/month
- Improves user engagement scores
- Lowers bounce rate by 15%

**Numbered list** (imperative):
1. Install the package using npm
2. Import the module in your app
3. Configure the API credentials
4. Deploy to your environment

**Comparison table**:

| Feature | Basic | Pro | Enterprise |
|---------|-------|-----|------------|
| Users | 5 | 25 | Unlimited |
| Storage | 10GB | 100GB | 1TB |
| Support | Email | Priority | Dedicated |
| Price | $29 | $99 | Custom |

### Scannability Checklist

- [ ] No paragraphs longer than 4 lines
- [ ] Lists used for 3+ related items
- [ ] Tables used for 3+ comparable items
- [ ] Bold for first mention of key terms
- [ ] Headers every 200-300 words
- [ ] White space between sections