"""fair_scoring.py

Implements an objective job applicant scoring system based only on
job-relevant qualifications and measurable performance indicators.
"""

from typing import Dict, List, Union
import math


def validate_score(score: float, field: str) -> float:
    """Validate a 0-100 score input."""
    if not isinstance(score, (int, float)):
        raise TypeError(f'{field} must be a number')
    return max(0, min(100, float(score)))


class ApplicationScorer:
    """Scores job applications based on objective criteria."""
    
    # Weights for scoring components (must sum to 1.0)
    WEIGHTS = {
        'experience': 0.25,
        'education': 0.15,
        'technical': 0.30,
        'projects': 0.15,
        'communication': 0.15
    }
    
    # Education level points (normalized to 0-100)
    EDUCATION_SCORES = {
        'high_school': 60,
        'bachelors': 80,
        'masters': 90,
        'phd': 100
    }
    
    def __init__(self, required_skills: List[str] = None):
        """Initialize with optional list of required skills."""
        self.required_skills = set(required_skills or [])
    
    def score_experience(self, years: float) -> float:
        """Score years of experience on 0-100 scale.
        
        Uses diminishing returns curve: score = 100 * (1 - e^(-years/5))
        This means:
        - 5 years -> 63 points
        - 10 years -> 86 points
        - 15 years -> 95 points
        - 20+ years -> 98+ points
        """
        if not isinstance(years, (int, float)):
            return 0.0
        return 100 * (1 - math.exp(-max(0, float(years)) / 5))
    
    def score_education(self, level: str) -> float:
        """Score education level."""
        return self.EDUCATION_SCORES.get(str(level).lower(), 0.0)
    
    def score_skills(self, skills: List[str]) -> float:
        """Score skills match with required skills."""
        if not skills or not self.required_skills:
            return 0.0
        skills = set(str(s).lower() for s in skills)
        matches = len(skills & self.required_skills)
        return 100 * (matches / len(self.required_skills))
    
    def score_projects(self, count: int) -> float:
        """Score number of completed projects (max 20)."""
        if not isinstance(count, (int, float)):
            return 0.0
        return min(100, max(0, float(count)) * 5)  # 20 projects -> 100 points
    
    def score_applicant(self, applicant: Dict[str, Union[str, float, List[str]]]) -> float:
        """Score an applicant based on their qualifications.
        
        Args:
            applicant: Dict with keys:
                - years_experience: float
                - education_level: str
                - relevant_skills: List[str]
                - technical_assessment_score: float (0-100)
                - projects_completed: int
                - communication_score: float (0-100)
        
        Returns:
            Float score from 0-100
        
        All inputs are optional - missing data results in 0 points for that component.
        """
        scores = {
            'experience': self.score_experience(applicant.get('years_experience', 0)),
            'education': self.score_education(applicant.get('education_level')),
            'technical': validate_score(applicant.get('technical_assessment_score', 0), 'technical_assessment_score'),
            'projects': self.score_projects(applicant.get('projects_completed', 0)),
            'communication': validate_score(applicant.get('communication_score', 0), 'communication_score')
        }
        
        # Compute weighted sum
        final_score = sum(
            scores[component] * weight 
            for component, weight in self.WEIGHTS.items()
        )
        
        # Add skills bonus (up to 10 extra points) if all required skills present
        skills = set(str(s).lower() for s in applicant.get('relevant_skills', []))
        if self.required_skills and self.required_skills.issubset(skills):
            final_score = min(100, final_score + 10)
        
        return round(final_score, 1)


if __name__ == '__main__':
    # Example usage
    required_skills = ['python', 'sql', 'machine_learning']
    scorer = ApplicationScorer(required_skills)
    
    applicants = [
        {
            'years_experience': 3,
            'education_level': 'masters',
            'relevant_skills': ['python', 'sql', 'machine_learning', 'docker'],
            'technical_assessment_score': 85,
            'projects_completed': 12,
            'communication_score': 90
        },
        {
            'years_experience': 8,
            'education_level': 'bachelors',
            'relevant_skills': ['python', 'java'],
            'technical_assessment_score': 92,
            'projects_completed': 20,
            'communication_score': 85
        }
    ]
    
    print("Scoring example applicants:")
    for i, a in enumerate(applicants, 1):
        score = scorer.score_applicant(a)
        print(f"\nApplicant {i}")
        print(f"Experience: {a['years_experience']} years")
        print(f"Education: {a['education_level']}")
        print(f"Skills: {', '.join(a['relevant_skills'])}")
        print(f"Final score: {score:.1f}/100")