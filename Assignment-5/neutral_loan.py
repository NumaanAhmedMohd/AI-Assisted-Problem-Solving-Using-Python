"""neutral_loan.py

Fair loan approval example that uses only non-protected financial features.
Uses a simple scoring function based on income, credit_score, and debt-to-income.
"""

def approve_loan(applicant):
    """Applicant is a dict with keys: income, credit_score, existing_debt"""
    income = applicant.get('income', 0)
    credit = applicant.get('credit_score', 0)
    debt = applicant.get('existing_debt', 0)
    # Debt-to-income ratio
    dti = debt / income if income > 0 else 1.0
    score = 0
    score += max(min((income - 30000) / 1000, 40), 0)
    score += max(min((credit - 550) / 3, 40), 0)
    score -= max(min(dti * 30, 30), 0)
    # Decision threshold
    return score >= 30

if __name__ == '__main__':
    samples = [
        {'income': 40000, 'credit_score': 680, 'existing_debt': 5000},
        {'income': 60000, 'credit_score': 720, 'existing_debt': 1000},
    ]
    for i, s in enumerate(samples, 1):
        print('Applicant', i, 'approved?', approve_loan(s))
