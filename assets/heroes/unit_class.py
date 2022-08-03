from abc import ABC
from dataclasses import dataclass

from assets.skills import BaseSkill


@dataclass
class UnitClass(ABC):
    """Base class for unit classes"""
    name: str
    max_health: float
    max_stamina: float
    attack_modifier: float
    stamina_modifier: float
    armor_mod: float
    skill: BaseSkill
