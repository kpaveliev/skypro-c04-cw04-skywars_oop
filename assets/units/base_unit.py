from abc import ABC, abstractmethod

from assets.equipment import Armor, Weapon
from assets.heroes import UnitClass


class BaseUnit(ABC):
    """Base class for units"""

    def __init__(self, name: str, unit_class: UnitClass):
        self.name = name
        self.unit_class = unit_class
        self.health: float = unit_class.max_health
        self.stamina: float = unit_class.max_stamina
        self.weapon: Weapon = None
        self.armor: Armor = None
        self.skill_used: bool = False

    def equip_weapon(self, weapon: Weapon) -> str:
        """Equip unit with the Weapon passed"""
        self.weapon = weapon
        return f"{self.name} is equipped with the weapon - {self.weapon.name}"

    def equip_armor(self, armor: Armor) -> str:
        """Equip unit with the Armor passed"""
        self.armor = armor
        return f"{self.name} is equipped with the armor - {self.armor.name}"

    def _calculate_attack(self, target: BaseUnit) -> float:
        """Calculate total attack points - weapon + attack_modifier"""

        # Calculate damage and defence
        damage = self.weapon.calculate_damage() * self.unit_class.attack_modifier
        defence = self.armor.defence if self.stamina >= self.armor.stamina_per_turn else 0

        # Change states
        self.stamina -= self.weapon.stamina_per_attack
        target.stamina -= self.armor.stamina_per_turn
        target.health -= damage - defence

        return damage

    def attack(self, target: BaseUnit) -> str:
        """Attack logic"""

        if self.stamina >= self.weapon.stamina_per_attack:
            damage = self._calculate_attack(target)
            if damage > 0:
                return f"{self.name} inflict {damage} damage to {target.name} using {self.weapon.name}."
            return f"{self.name} tried to attack {target.name}, but he wasn't able to penetrate {target.name} armor."

        return f"{self.name} tried to use {self.weapon.name}, but he didn't have enough stamina."

    def use_skill(self, target: BaseUnit):
        """Use special skill"""
        if self.skill_used:
            return f"{self.name} tried to use {self.unit_class.skill.name}, but it's already used."
        return self.unit_class.skill.use(user=self, target=target)

    # def get_damage(self, damage_inflicted: float):
    #     """Calculate damage"""
    #     self.health -= damage_inflicted - self._calculate_defence()
    #     return
