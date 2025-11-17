"""biased_loan.py

This file simulates an AI-generated loan approval snippet that uses
protected attributes (gender, name-based heuristics) in its decision logic.
This is intentionally biased to demonstrate detection.
"""

def approve_loan(applicant):
    """Applicant is a dict with keys: name, gender, income, credit_score, debt"""
    score = 0
    # Financial factors (reasonable)
    if applicant.get('income', 0) > 50000:
        score += 30
    score += min(max(applicant.get('credit_score', 0) - 600, 0), 100) / 2
    # Insecure / biased factors
    # Example: small boost for males
    if applicant.get('gender') == 'male':
        score += 5
    # Example: name-based heuristic (very bad) — favors names that sound "traditional"
    if applicant.get('name', '').lower() in ('john', 'michael', 'robert'):
        score += 7
    # Example: reduces score for female unless 'married' flag present
    if applicant.get('gender') == 'female' and not applicant.get('married'):
        score -= 10
    return score >= 50

if __name__ == '__main__':
    samples = [
        {'name': 'John', 'gender': 'male', 'income': 40000, 'credit_score': 680, 'debt': 5000},
        {'name': 'Jane', 'gender': 'female', 'income': 60000, 'credit_score': 720, 'debt': 1000},
    ]
    for s in samples:
        print(s['name'], 'approved?', approve_loan(s))
