"""inclusive_greetings.py

Provides inclusive greeting functionality that respects all gender identities.
Uses gender-neutral language by default and allows custom honorifics.
"""

from typing import Optional
from dataclasses import dataclass
from enum import Enum, auto


class HonorificPreference(Enum):
    """Represents user's honorific preference."""
    NEUTRAL = auto()  # Uses Mx. or no honorific
    SPECIFIED = auto()  # Uses user-specified honorific
    NONE = auto()  # Uses no honorific


@dataclass
class PersonInfo:
    """Stores person's name and greeting preferences."""
    name: str
    honorific_preference: HonorificPreference = HonorificPreference.NEUTRAL
    preferred_honorific: Optional[str] = None
    use_honorific: bool = True

    @classmethod
    def create(cls, name: str, **kwargs):
        """Factory method for common cases."""
        return cls(
            name=name,
            honorific_preference=kwargs.get('honorific_preference', HonorificPreference.NEUTRAL),
            preferred_honorific=kwargs.get('preferred_honorific'),
            use_honorific=kwargs.get('use_honorific', True)
        )


def get_honorific(person: PersonInfo) -> str:
    """Get appropriate honorific based on person's preferences."""
    if not person.use_honorific:
        return ""
    
    if person.honorific_preference == HonorificPreference.NONE:
        return ""
    
    if person.honorific_preference == HonorificPreference.SPECIFIED and person.preferred_honorific:
        return person.preferred_honorific
    
    # Default to gender-neutral honorific
    return "Mx."


def greet_person(person: PersonInfo) -> str:
    """Generate an inclusive greeting for a person.
    
    Args:
        person: PersonInfo object with name and preferences
    
    Returns:
        A greeting string respecting the person's preferences
    
    Examples:
        >>> p1 = PersonInfo.create("Alex")  # Uses neutral honorific
        >>> greet_person(p1)
        'Hello, Mx. Alex! Welcome.'
        
        >>> p2 = PersonInfo.create("Sam", honorific_preference=HonorificPreference.NONE)
        >>> greet_person(p2)
        'Hello, Sam! Welcome.'
        
        >>> p3 = PersonInfo.create("Pat", 
        ...     honorific_preference=HonorificPreference.SPECIFIED,
        ...     preferred_honorific="Dr.")
        >>> greet_person(p3)
        'Hello, Dr. Pat! Welcome.'
    """
    honorific = get_honorific(person)
    name_part = f"{honorific} {person.name}" if honorific else person.name
    return f"Hello, {name_part}! Welcome."


if __name__ == '__main__':
    # Examples of inclusive greetings
    examples = [
        PersonInfo.create("Alex"),  # Uses neutral Mx.
        PersonInfo.create("Sam", honorific_preference=HonorificPreference.NONE),  # No honorific
        PersonInfo.create("Pat", 
                         honorific_preference=HonorificPreference.SPECIFIED,
                         preferred_honorific="Dr."),  # Specified honorific
        PersonInfo.create("Jordan", use_honorific=False)  # No honorific
    ]
    
    print("Inclusive greeting examples:")
    for person in examples:
        print(f"- {greet_person(person)}")