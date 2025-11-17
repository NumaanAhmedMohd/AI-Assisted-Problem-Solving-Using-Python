"""analyze_inclusiveness.py

Analyzes code for gendered language and potential inclusivity issues.
"""

import ast
import re
from typing import List, Set


GENDERED_TERMS = {
    # Common gendered honorifics
    r'\b(Mr\.|Mrs\.|Miss|Ms\.)\b',
    
    # Gendered pronouns
    r'\b(he|him|his|she|her|hers)\b',
    
    # Gendered role words
    r'\b(mankind|man|woman|boy|girl|lady|gentleman)\b',
    
    # Binary gender assumptions
    r'\b(male|female)\b',
    r'\b(gender\.lower\(\)\s*==\s*[\'"](?:male|female)[\'"]\b)',
    
    # Common gendered phrases
    r'\b(guys|dude|bro|sis)\b'
}

SUGGESTED_ALTERNATIVES = {
    'Mr./Mrs./Miss/Ms.': 'Mx. or no honorific',
    'he/she': 'they',
    'his/her': 'their',
    'mankind': 'humanity or humankind',
    'guys': 'everyone, folks, or team',
    'male/female': 'Consider if gender is relevant; if needed, allow self-identification'
}


def check_file_for_gendered_language(filename: str) -> List[str]:
    """Scan a file for potentially non-inclusive language."""
    findings = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for gendered terms
        for pattern in GENDERED_TERMS:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                term = match.group(0)
                line_no = content.count('\n', 0, match.start()) + 1
                findings.append(f"Line {line_no}: Found gendered term '{term}'")
        
        # Check for binary gender assumptions in code
        tree = ast.parse(content)
        binary_checker = BinaryGenderChecker()
        binary_checker.visit(tree)
        findings.extend(binary_checker.findings)
        
    except Exception as e:
        findings.append(f"Error analyzing file: {e}")
    
    return findings


class BinaryGenderChecker(ast.NodeVisitor):
    """AST visitor that checks for binary gender assumptions in code."""
    
    def __init__(self):
        self.findings: List[str] = []
    
    def visit_If(self, node):
        """Check if conditions for gender comparisons."""
        # Look for if gender == "male" or similar
        if isinstance(node.test, ast.Compare):
            if isinstance(node.test.left, ast.Name) and node.test.left.id == 'gender':
                self.findings.append(
                    "Found binary gender check (if gender == ...) - "
                    "consider using a more inclusive approach"
                )
        self.generic_visit(node)


def suggest_improvements(findings: List[str]) -> List[str]:
    """Generate improvement suggestions based on findings."""
    suggestions = []
    seen_terms: Set[str] = set()
    
    for finding in findings:
        for term, alternative in SUGGESTED_ALTERNATIVES.items():
            if term.lower() in finding.lower() and term not in seen_terms:
                suggestions.append(f"Consider replacing '{term}' with {alternative}")
                seen_terms.add(term)
    
    return suggestions


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python analyze_inclusiveness.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    print(f"\nAnalyzing {filename} for inclusivity...\n")
    
    findings = check_file_for_gendered_language(filename)
    if findings:
        print("Findings:")
        for f in findings:
            print(f"- {f}")
        
        print("\nSuggestions:")
        for s in suggest_improvements(findings):
            print(f"- {s}")
    else:
        print("No inclusivity issues found!")