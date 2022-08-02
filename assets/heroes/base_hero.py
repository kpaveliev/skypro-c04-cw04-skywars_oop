from abc import ABC
from dataclasses import dataclass

from assets.skills import BaseSkill


@dataclass
class BaseHero(ABC):
    """Base class for heroes"""
    name: str
    max_health: float
    max_stamina: float
    attack_mod: float
    stamina_mod: float
    armor_mod: float
    skill: BaseSkill
