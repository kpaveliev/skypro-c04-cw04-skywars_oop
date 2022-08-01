from abc import ABC
from dataclasses import dataclass

from assets.skills.skill import Skill


@dataclass
class Hero(ABC):
    """Base class for heroes"""
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill
