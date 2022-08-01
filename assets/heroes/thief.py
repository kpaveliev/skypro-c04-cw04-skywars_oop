from dataclasses import dataclass

from assets.skills.powerful_thrust import PowerfulThrust
from assets.skills.skill import Skill
from hero import Hero


@dataclass
class Thief(Hero):
    """Base class for heroes"""
    name: str = 'Вор'
    max_health: float = 50.0
    max_stamina: float = 25.0
    attack: float = 1.5
    stamina: float = 1.2
    armor: float = 1.0
    skill: Skill = PowerfulThrust
