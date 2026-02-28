#!/usr/bin/env python3
"""
Optimize content for GEO citation readiness.
"""

import argparse
import re
import sys
from datetime import datetime


class ContentOptimizer:
    """Optimize content for AI citation."""
    
    def __init__(self, content, content_type='article'):
        self.original = content
        self.content_type = content_type
        self.changes = []
    
    def optimize(self):
        """Apply all optimizations."""
        content = self.original
        
        # Apply optimizations based on content type
        if self.content_type == 'article':
            content = self._optimize_article(content)
        elif self.content_type == 'product':
            content = self._optimize_product(content)
        elif self.content_type == 'faq':
            content = self._optimize_faq(content)
        elif self.content_type == 'landing':
            content = self._optimize_landing(content)
        elif self.content_type == 'about':
            content = self._optimize_about(content)
        
        # Universal optimizations
        content = self._add_structure(content)
        content = self._improve_scannability(content)
        content = self._remove_hedging(content)
        
        return {
            'original': self.original,
            'optimized': content,
            'changes': self.changes,
            'word_count_original': len(self.original.split()),
            'word_count_optimized': len(content.split())
        }
    
    def _optimize_article(self, content):
        """Optimize article content."""
        # Ensure strong opening
        lines = content.split('\n')
        if lines:
            first_line = lines[0]
            if first_line.startswith('#'):
                # Has title, check second paragraph
                pass
            else:
                self.changes.append("Added H1 title placeholder - please customize")
        
        self.changes.append("Article optimization: Ensure lead paragraph answers the core question directly")
        self.changes.append("Article optimization: Add FAQ section with 3-5 questions if not present")
        
        return content
    
    def _optimize_product(self, content):
        """Optimize product page content."""
        self.changes.append("Product optimization: Lead with one-sentence product definition")
        self.changes.append("Product optimization: Include specifications in table format")
        self.changes.append("Product optimization: Add comparison with alternatives")
        return content
    
    def _optimize_faq(self, content):
        """Optimize FAQ content."""
        self.changes.append("FAQ optimization: Ensure answers are comprehensive (50-150 words)")
        self.changes.append("FAQ optimization: Add data points to answers")
        return content
    
    def _optimize_landing(self, content):
        """Optimize landing page content."""
        self.changes.append("Landing optimization: Lead with clear value proposition")
        self.changes.append("Landing optimization: Include specific benefits with data")
        self.changes.append("Landing optimization: Add social proof with names/companies")
        return content
    
    def _optimize_about(self, content):
        """Optimize about page content."""
        self.changes.append("About optimization: Include founding date and story")
        self.changes.append("About optimization: List key milestones with dates")
        self.changes.append("About optimization: Include customer names and metrics")
        return content
    
    def _add_structure(self, content):
        """Add/improve header structure."""
        # Count existing headers
        h2_count = len(re.findall(r'^##\s+', content, re.MULTILINE))
        
        words = len(content.split())
        expected_h2 = max(2, words // 400)
        
        if h2_count < expected_h2:
            self.changes.append(f"Structure: Consider adding {expected_h2 - h2_count} more H2 headers")
        
        return content
    
    def _improve_scannability(self, content):
        """Improve formatting for scannability."""
        # Check for long paragraphs
        paragraphs = [p for p in content.split('\n\n') if p.strip()]
        long_paragraphs = sum(1 for p in paragraphs if len(p.split()) > 100)
        
        if long_paragraphs > 0:
            self.changes.append(f"Scannability: Break up {long_paragraphs} long paragraphs (>100 words)")
        
        # Check for lists
        bullet_count = len(re.findall(r'^[\s]*[-*]\s+', content, re.MULTILINE))
        if bullet_count < 3 and len(paragraphs) > 5:
            self.changes.append("Scannability: Convert related items to bullet lists")
        
        return content
    
    def _remove_hedging(self, content):
        """Identify hedging language."""
        hedging_patterns = [
            (r'\bmight be\b', 'is'),
            (r'\bcould be\b', 'is'),
            (r'\bprobably\b', ''),
            (r'\barguably\b', ''),
            (r'\bto some extent\b', ''),
            (r'\bin our opinion\b', ''),
        ]
        
        found_hedging = []
        for pattern, _ in hedging_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            found_hedging.extend(matches)
        
        if found_hedging:
            unique = set(found_hedging)
            self.changes.append(f"Voice: Replace hedging language: {', '.join(unique)}")
        
        return content


def generate_changelog(changes):
    """Generate a changelog from optimization changes."""
    lines = ["# Optimization Changelog\n"]
    
    categories = {}
    for change in changes:
        cat = change.split(':')[0]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(change.split(':', 1)[1].strip() if ':' in change else change)
    
    for cat, items in categories.items():
        lines.append(f"## {cat}")
        for item in items:
            lines.append(f"- {item}")
        lines.append("")
    
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description="Optimize content for GEO")
    parser.add_argument("file", help="Content file to optimize")
    parser.add_argument("--type", choices=["article", "product", "faq", "landing", "about"],
                       default="article", help="Content type")
    parser.add_argument("--output", "-o", help="Output file (default: stdout)")
    
    args = parser.parse_args()
    
    # Read content
    try:
        with open(args.file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)
    
    # Optimize
    optimizer = ContentOptimizer(content, args.type)
    result = optimizer.optimize()
    
    # Generate output
    output_lines = [
        "# Optimized Content\n",
        result['optimized'],
        "\n" + "="*60 + "\n",
        generate_changelog(result['changes']),
        "\n" + "="*60 + "\n",
        f"**Word Count**: {result['word_count_original']} → {result['word_count_optimized']}"
    ]
    
    output = '\n'.join(output_lines)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"Optimized content saved to: {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
