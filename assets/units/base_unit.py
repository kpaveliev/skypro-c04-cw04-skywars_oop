from abc import ABC, abstractmethod

from assets.equipment import Armor, Weapon
from assets.heroes import BaseHero


class BaseUnit(ABC):
    """Base class for units"""

    def __init__(self, name: str, unit_class: BaseHero):
        self.name = name
        self.unit_class = unit_class
        self.health: float = unit_class.max_health
        self.stamina: float = unit_class.max_stamina
        self.weapon: Weapon = None
        self.armor: Armor = None
        self.skill_used = False



    def equip_weapon(self, weapon: Weapon):
        return ""

    def equip_armor(self, armor: Armor):
        return ""

    def _total_attack(self):
        return self.weapon.calculate_damage() * self.unit_class.attack

    def

