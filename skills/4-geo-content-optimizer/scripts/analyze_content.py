#!/usr/bin/env python3
"""
Analyze content for GEO citation readiness.
"""

import argparse
import json
import re
import sys
from pathlib import Path


class ContentAnalyzer:
    """Analyze content for GEO optimization."""
    
    def __init__(self, content):
        self.content = content
        self.text_only = re.sub(r'<[^>]+>', '', content)
        self.words = self.text_only.split()
        self.sentences = re.split(r'[.!?]+', self.text_only)
        self.lines = content.split('\n')
        
        self.scores = {
            'direct_answer': 0,
            'entity_rich': 0,
            'structured_format': 0,
            'fact_dense': 0,
            'faq_formatted': 0,
            'definition_clarity': 0,
            'authoritative_voice': 0,
            'scannable': 0
        }
        self.issues = []
        self.suggestions = []
    
    def analyze(self):
        """Run all analyses."""
        self._check_direct_answer()
        self._check_entity_rich()
        self._check_structured_format()
        self._check_fact_dense()
        self._check_faq_formatted()
        self._check_definition_clarity()
        self._check_authoritative_voice()
        self._check_scannable()
        
        total_score = sum(self.scores.values())
        max_score = len(self.scores) * 10
        
        return {
            'overall_score': total_score,
            'max_score': max_score,
            'percentage': round((total_score / max_score) * 100),
            'grade': self._get_grade(total_score, max_score),
            'dimension_scores': self.scores,
            'word_count': len(self.words),
            'issues': self.issues,
            'suggestions': self.suggestions
        }
    
    def _get_grade(self, score, max_score):
        """Convert score to letter grade."""
        pct = score / max_score
        if pct >= 0.9: return "A+"
        if pct >= 0.8: return "A"
        if pct >= 0.7: return "B"
        if pct >= 0.6: return "C"
        if pct >= 0.5: return "D"
        return "F"
    
    def _check_direct_answer(self):
        """Check if content leads with direct answer."""
        if len(self.sentences) < 2:
            self.issues.append("Content too short to analyze")
            return
        
        first_sentence = self.sentences[0].strip()
        first_words = first_sentence.lower().split()
        
        # Check for throat-clearing phrases
        weak_openers = ['in', 'as', 'while', 'although', 'today', 'recently', 'many', 'some']
        if any(first_sentence.lower().startswith(w) for w in weak_openers):
            self.issues.append("Weak opening - starts with filler phrase")
            self.suggestions.append("Start with direct answer, not 'In today's world...'")
            self.scores['direct_answer'] = 3
        else:
            # Check for definition or direct statement
            if ' is ' in first_sentence or ' are ' in first_sentence or ' means ' in first_sentence:
                self.scores['direct_answer'] = 8
            else:
                self.scores['direct_answer'] = 5
                self.suggestions.append("First sentence should define or directly answer the topic")
    
    def _check_entity_rich(self):
        """Check for named entities."""
        # Simple entity detection (capitalized words that aren't sentence starters)
        text_lower = self.text_only.lower()
        
        # Check for brand/product mentions in first 100 words
        first_100 = ' '.join(self.words[:100])
        
        # Count potential entities (simplified)
        capitalized = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', self.text_only)
        entities = [e for e in capitalized if len(e) > 2]
        
        entity_density = len(entities) / len(self.words) if self.words else 0
        
        if entity_density >= 0.02:  # 1 entity per 50 words
            self.scores['entity_rich'] = 9
        elif entity_density >= 0.01:
            self.scores['entity_rich'] = 6
            self.suggestions.append(f"Add more named entities (brands, products, people). Current density: {entity_density:.1%}")
        else:
            self.scores['entity_rich'] = 3
            self.issues.append("Too few named entities")
            self.suggestions.append("Include specific brand names, products, and people in your content")
    
    def _check_structured_format(self):
        """Check for headers and structure."""
        h2_count = len(re.findall(r'^##\s+', self.content, re.MULTILINE))
        h3_count = len(re.findall(r'^###\s+', self.content, re.MULTILINE))
        
        # Expected headers for content length
        expected_h2 = max(2, len(self.words) // 400)
        
        if h2_count >= expected_h2:
            self.scores['structured_format'] = 9
        elif h2_count >= expected_h2 // 2:
            self.scores['structured_format'] = 6
            self.suggestions.append(f"Add more H2 headers. Target: {expected_h2}, Current: {h2_count}")
        else:
            self.scores['structured_format'] = 3
            self.issues.append("Insufficient header structure")
            self.suggestions.append("Use H2 headers every 300-400 words to break up content")
        
        if h3_count < h2_count and h2_count > 3:
            self.suggestions.append("Consider adding H3 subsections for better hierarchy")
    
    def _check_fact_dense(self):
        """Check for data points and statistics."""
        # Look for numbers that appear to be statistics
        percentages = len(re.findall(r'\d+%', self.content))
        years = len(re.findall(r'20\d{2}', self.content))
        currency = len(re.findall(r'\$[\d,]+', self.content))
        large_numbers = len(re.findall(r'\d{3,}', self.content))
        
        data_points = percentages + years + min(currency, 5) + min(large_numbers // 2, 5)
        
        # Target: 3-5 data points per 500 words
        target = len(self.words) / 500 * 4
        
        if data_points >= target:
            self.scores['fact_dense'] = 9
        elif data_points >= target / 2:
            self.scores['fact_dense'] = 6
            self.suggestions.append(f"Add more data points (percentages, dates, statistics). Target: {int(target)}, Current: {data_points}")
        else:
            self.scores['fact_dense'] = 3
            self.issues.append("Content lacks data density")
            self.suggestions.append("Include specific numbers, dates, and statistics to support claims")
    
    def _check_faq_formatted(self):
        """Check for FAQ format."""
        faq_patterns = [
            r'\*\*Q:\s*',  # **Q: format
            r'\*\*Question:\s*',  # **Question: format
            r'^\*\*[^*]+\?\*\*',  # **Question?** format
            r'##\s*Frequently Asked',  # FAQ section
            r'##\s*FAQ'  # FAQ section
        ]
        
        faq_count = 0
        for pattern in faq_patterns:
            faq_count += len(re.findall(pattern, self.content, re.IGNORECASE))
        
        if faq_count >= 3:
            self.scores['faq_formatted'] = 10
        elif faq_count >= 1:
            self.scores['faq_formatted'] = 6
            self.suggestions.append("Add more FAQ-formatted Q&A blocks (target: 3-5)")
        else:
            self.scores['faq_formatted'] = 2
            self.issues.append("No FAQ format detected")
            self.suggestions.append("Convert key points to FAQ format with explicit Q&A")
    
    def _check_definition_clarity(self):
        """Check for definition blocks."""
        # Look for bold definitions
        definition_patterns = [
            r'\*\*[^*]+\*\*:\s*[^*]+is',  # **Term**: ... is
            r'\*\*[^*]+\*\*\s*refers to',  # **Term** refers to
            r'\*\*[^*]+\*\*\s*means',  # **Term** means
        ]
        
        definitions = 0
        for pattern in definition_patterns:
            definitions += len(re.findall(pattern, self.content))
        
        if definitions >= 2:
            self.scores['definition_clarity'] = 9
        elif definitions >= 1:
            self.scores['definition_clarity'] = 6
            self.suggestions.append("Add more definition blocks for key terms")
        else:
            self.scores['definition_clarity'] = 3
            self.issues.append("No definition blocks found")
            self.suggestions.append("Define key terms on first use using **Term**: Definition format")
    
    def _check_authoritative_voice(self):
        """Check for hedging language."""
        hedging_phrases = [
            'might be', 'could be', 'may be', 'possibly', 'probably',
            'some experts', 'it seems', 'arguably', 'to some extent',
            'in our opinion', 'we believe', 'we think'
        ]
        
        content_lower = self.text_only.lower()
        hedging_count = sum(content_lower.count(phrase) for phrase in hedging_phrases)
        
        # Normalize by word count
        hedging_rate = hedging_count / len(self.words) if self.words else 0
        
        if hedging_rate < 0.001:  # Less than 1 per 1000 words
            self.scores['authoritative_voice'] = 9
        elif hedging_rate < 0.003:
            self.scores['authoritative_voice'] = 6
            self.suggestions.append("Reduce hedging language ('might', 'could', 'probably')")
        else:
            self.scores['authoritative_voice'] = 3
            self.issues.append("Too much hedging language")
            self.suggestions.append("Use declarative statements. Replace 'might be' with 'is'")
    
    def _check_scannable(self):
        """Check for scannable formatting."""
        bullet_lists = len(re.findall(r'^[\s]*[-*]\s+', self.content, re.MULTILINE))
        numbered_lists = len(re.findall(r'^[\s]*\d+\.\s+', self.content, re.MULTILINE))
        tables = len(re.findall(r'\|.*\|.*\|', self.content))
        bold_text = len(re.findall(r'\*\*[^*]+\*\*', self.content))
        
        # Paragraph length check
        paragraphs = [p for p in self.content.split('\n\n') if p.strip()]
        long_paragraphs = sum(1 for p in paragraphs if len(p.split()) > 100)
        
        scannable_elements = bullet_lists + numbered_lists + tables * 3
        
        if scannable_elements >= 5 and long_paragraphs == 0:
            self.scores['scannable'] = 9
        elif scannable_elements >= 3:
            self.scores['scannable'] = 6
            if long_paragraphs > 0:
                self.suggestions.append(f"Break up {long_paragraphs} long paragraphs (>100 words)")
        else:
            self.scores['scannable'] = 3
            self.issues.append("Content not scannable")
            self.suggestions.append("Use bullet lists, numbered lists, and tables to break up text")


def output_markdown(report):
    """Format report as markdown."""
    lines = [
        f"# GEO Content Analysis Report\n",
        f"**Overall Score**: {report['overall_score']}/{report['max_score']} ({report['grade']})\n",
        f"**Word Count**: {report['word_count']}\n",
        "## Dimension Scores\n"
    ]
    
    for dim, score in report['dimension_scores'].items():
        bar = '█' * (score // 2) + '░' * (5 - score // 2)
        lines.append(f"- **{dim.replace('_', ' ').title()}**: {score}/10 {bar}")
    
    if report['issues']:
        lines.append("\n## Issues\n")
        for issue in report['issues']:
            lines.append(f"- ❌ {issue}")
    
    if report['suggestions']:
        lines.append("\n## Suggestions\n")
        for suggestion in report['suggestions']:
            lines.append(f"- 💡 {suggestion}")
    
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description="Analyze content for GEO optimization")
    parser.add_argument("file", help="Content file to analyze")
    parser.add_argument("--format", choices=["json", "md", "markdown"], default="md", help="Output format")
    parser.add_argument("--score-only", action="store_true", help="Output only the score")
    
    args = parser.parse_args()
    
    # Read content
    try:
        with open(args.file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)
    
    # Analyze
    analyzer = ContentAnalyzer(content)
    report = analyzer.analyze()
    
    if args.score_only:
        print(report['percentage'])
        return
    
    # Output
    if args.format == "json":
        print(json.dumps(report, indent=2))
    else:
        print(output_markdown(report))


if __name__ == "__main__":
    main()
