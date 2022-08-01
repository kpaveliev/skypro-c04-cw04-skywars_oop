from dataclasses import dataclass

from assets.skills.ferocious_kick import FerociousKick
from assets.skills.skill import Skill
from hero import Hero


@dataclass
class Warrior(Hero):
    """Base class for heroes"""
    name: str = 'Воин'
    max_health: float = 60.0
    max_stamina: float = 30.0
    attack: float = 0.8
    stamina: float = 0.9
    armor: float = 1.2
    skill: Skill = FerociousKick
