"""biased_scoring.py

This file simulates a biased AI-generated scoring system that incorrectly
uses protected attributes or proxies for discrimination. This is an example
of what to watch for and avoid.
"""

from typing import Dict, List, Union
import re


def score_applicant(applicant: Dict[str, Union[str, float, List[str]]]) -> float:
    """Score a job applicant based on their profile. Shows common biases to avoid.

    Args:
        applicant: Dict with applicant details including potentially discriminatory fields

    Returns:
        A score from 0-100
    """
    score = 0.0
    
    # PROBLEMATIC: Using age as a direct factor
    if 'age' in applicant:
        age = applicant['age']
        if 25 <= age <= 35:  # Age discrimination
            score += 10
        elif age > 50:  # Age penalty
            score -= 15
    
    # PROBLEMATIC: Gender bias
    if applicant.get('gender', '').lower() == 'male':
        score += 5  # Gender discrimination
    
    # PROBLEMATIC: Using name to infer demographics
    name = applicant.get('name', '').lower()
    common_names = {'john', 'michael', 'david', 'james'}
    if name in common_names:
        score += 8  # Name-based bias
    
    # PROBLEMATIC: Proxy for age via graduation year
    grad_year = applicant.get('graduation_year', 0)
    if grad_year > 2020:  # Recent grads preferred
        score += 12
    
    # Some legitimate factors mixed in
    score += min(applicant.get('years_experience', 0) * 2, 30)
    score += min(applicant.get('technical_score', 0), 40)
    
    # PROBLEMATIC: Marital status bias
    if applicant.get('marital_status') == 'married':
        score += 5  # Assumed "stability" bias
    
    # Normalize to 0-100
    return max(0, min(100, score))


def analyze_resume(text: str) -> Dict[str, Union[str, float]]:
    """PROBLEMATIC: Tries to infer protected characteristics from resume text."""
    results = {}
    
    # Trying to guess gender from pronouns (very problematic)
    if re.search(r'\b(he|his|him)\b', text, re.I):
        results['inferred_gender'] = 'male'
    elif re.search(r'\b(she|her|hers)\b', text, re.I):
        results['inferred_gender'] = 'female'
    
    # Trying to guess age from experience (problematic proxy)
    years = len(re.findall(r'\b(19|20)\d{2}\b', text))
    if years > 0:
        results['estimated_experience'] = years * 1.5
    
    return results


if __name__ == '__main__':
    # Example showing bias
    applicants = [
        {
            'name': 'John Smith',
            'age': 32,
            'gender': 'male',
            'years_experience': 8,
            'technical_score': 85,
            'marital_status': 'married',
            'graduation_year': 2015
        },
        {
            'name': 'Maria Garcia',
            'age': 52,
            'gender': 'female',
            'years_experience': 25,
            'technical_score': 90,
            'marital_status': 'single',
            'graduation_year': 1995
        }
    ]
    
    for a in applicants:
        score = score_applicant(a)
        print(f"Applicant: {a['name']}")
        print(f"Score: {score:.1f}")
        print()