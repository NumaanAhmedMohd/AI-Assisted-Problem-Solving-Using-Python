"""analyze_scoring.py

Analyzes job scoring implementations for potential bias and discriminatory patterns.
Performs static analysis of code and dynamic testing with synthetic data.
"""

import ast
import importlib.util
import os
import re
from typing import Dict, List, Any
import random


# Protected attributes to check for
PROTECTED_ATTRIBUTES = {
    'gender', 'age', 'race', 'ethnicity', 'nationality', 'religion',
    'marital_status', 'disability', 'veteran_status', 'name',
    'birth', 'graduation_year'  # proxy for age
}

# Common biased terms in code
BIASED_TERMS = {
    r'\b(he|his|him|she|her)\b',  # gendered pronouns
    r'\b(male|female)\b',
    r'\b(young|old|senior|junior)\b',  # age-related
    r'\b(married|single)\b',
    r'19\d{2}|20\d{2}'  # year patterns that might proxy for age
}


def read_file(path: str) -> str:
    """Read file content."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return ""


def check_ast_for_protected(node: ast.AST) -> List[str]:
    """Walk AST to find usage of protected attributes."""
    findings = []
    
    class Visitor(ast.NodeVisitor):
        def visit_Subscript(self, node):
            # Check dict access: applicant['gender'] or applicant.get('gender')
            if isinstance(node.value, ast.Name):
                if isinstance(node.slice, ast.Constant):
                    key = str(node.slice.value)
                    if key.lower() in PROTECTED_ATTRIBUTES:
                        findings.append(f"Direct access of protected attribute: {key}")
            self.generic_visit(node)
        
        def visit_Call(self, node):
            # Check .get() calls: applicant.get('gender')
            if isinstance(node.func, ast.Attribute) and node.func.attr == 'get':
                if node.args and isinstance(node.args[0], ast.Constant):
                    key = str(node.args[0].value)
                    if key.lower() in PROTECTED_ATTRIBUTES:
                        findings.append(f"Dictionary get() of protected attribute: {key}")
            self.generic_visit(node)
    
    Visitor().visit(node)
    return findings


def static_analysis(src: str) -> List[str]:
    """Perform static analysis of source code."""
    findings = []
    
    # Check for protected attributes in code
    for term in PROTECTED_ATTRIBUTES:
        if re.search(rf'\b{term}\b', src, re.I):
            findings.append(f"Contains protected term: {term}")
    
    # Look for potentially biased language
    for pattern in BIASED_TERMS:
        if re.search(pattern, src, re.I):
            findings.append(f"Contains potentially biased pattern: {pattern}")
    
    # Parse AST for more detailed analysis
    try:
        tree = ast.parse(src)
        findings.extend(check_ast_for_protected(tree))
    except Exception as e:
        findings.append(f"AST analysis error: {e}")
    
    return findings


def generate_synthetic_applicants(n: int = 100) -> List[Dict[str, Any]]:
    """Generate synthetic applicant data for testing."""
    applicants = []
    
    # Demographics for testing bias
    genders = ['male', 'female']
    ages = list(range(25, 65))
    education = ['high_school', 'bachelors', 'masters', 'phd']
    names_male = ['John', 'Michael', 'David', 'James', 'Robert']
    names_female = ['Mary', 'Jennifer', 'Lisa', 'Sandra', 'Michelle']
    
    for _ in range(n):
        gender = random.choice(genders)
        names = names_male if gender == 'male' else names_female
        
        applicant = {
            'name': random.choice(names),
            'gender': gender,
            'age': random.choice(ages),
            'years_experience': random.randint(0, 25),
            'education_level': random.choice(education),
            'technical_assessment_score': random.uniform(60, 100),
            'projects_completed': random.randint(0, 20),
            'communication_score': random.uniform(60, 100),
            'marital_status': random.choice(['single', 'married']),
            'graduation_year': random.randint(1980, 2023)
        }
        applicants.append(applicant)
    
    return applicants


def analyze_scoring_function(module_path: str):
    """Analyze a scoring function for bias."""
    print(f"\nAnalyzing {os.path.basename(module_path)}:")
    
    # Static analysis
    src = read_file(module_path)
    findings = static_analysis(src)
    if findings:
        print("\nStatic analysis findings:")
        for f in findings:
            print(f"- {f}")
    else:
        print("\nNo issues found in static analysis.")
    
    # Dynamic analysis with synthetic data
    try:
        spec = importlib.util.spec_from_file_location("module", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Handle both simple function and class-based scorer
        if hasattr(module, 'score_applicant'):
            scorer = module.score_applicant
        elif hasattr(module, 'ApplicationScorer'):
            scorer = module.ApplicationScorer(['python', 'sql']).score_applicant
        else:
            raise AttributeError("No scoring function or class found")
        
        # Generate synthetic data
        applicants = generate_synthetic_applicants(100)
        
        # Analyze scores by protected attributes
        scores_by_gender = {'male': [], 'female': []}
        scores_by_age = {'under_40': [], 'over_40': []}
        
        for a in applicants:
            score = scorer(a)
            scores_by_gender[a['gender']].append(score)
            age_group = 'under_40' if a['age'] < 40 else 'over_40'
            scores_by_age[age_group].append(score)
        
        # Calculate average scores by group
        print("\nDynamic analysis results:")
        for gender, scores in scores_by_gender.items():
            avg = sum(scores) / len(scores)
            print(f"Average score for {gender}: {avg:.1f}")
        
        for age_group, scores in scores_by_age.items():
            avg = sum(scores) / len(scores)
            print(f"Average score for {age_group}: {avg:.1f}")
            
    except Exception as e:
        print(f"\nError in dynamic analysis: {e}")


if __name__ == '__main__':
    # Analyze both implementations
    analyze_scoring_function('biased_scoring.py')
    analyze_scoring_function('fair_scoring.py')