from __future__ import annotations
from abc import ABC

from assets.equipment import Armor, Weapon
from assets.classes import UnitClass


class BaseUnit(ABC):
    """Base class for units"""

    def __init__(self, name: str, unit_class: UnitClass, weapon: Weapon, armor: Armor):
        self.name = name
        self.unit_class = unit_class
        self.health_points: float = unit_class.max_health
        self.stamina_points: float = unit_class.max_stamina
        self.weapon = weapon
        self.armor = armor
        self.skill_used: bool = False

    # def equip_weapon(self, weapon: Weapon) -> str:
    #     """Equip unit with the Weapon passed"""
    #     self.weapon = weapon
    #     return f"{self.name} is equipped with the weapon - {self.weapon.name}"
    #
    # def equip_armor(self, armor: Armor) -> str:
    #     """Equip unit with the Armor passed"""
    #     self.armor = armor
    #     return f"{self.name} is equipped with the armor - {self.armor.name}"

    def _calculate_damage(self, target: BaseUnit) -> float:
        """Calculate total attack points - weapon + attack_modifier"""

        # Calculate damage and defence
        damage = self.weapon.calculate_damage() * self.unit_class.attack_modifier
        defence = self.armor.defence if self.stamina_points >= self.armor.stamina_per_turn else 0

        # Change states
        self.stamina_points -= self.weapon.stamina_per_hit
        target.stamina_points -= self.armor.stamina_per_turn
        target.health_points -= round(damage, 1) - round(defence, 1)

        if target.health_points < 0:
            target.health_points = 0

        return round(damage, 1)

    def attack(self, target: BaseUnit) -> str:
        """Attack logic"""

        if self.stamina_points >= self.weapon.stamina_per_hit:
            damage = self._calculate_damage(target)
            if damage > 0:
                return (f"{self.name}, используя {self.weapon.name}, "
                        f"пробивает {target.armor.name} соперника и наносит {damage} урона.")
            return (f"{self.name}, используя {self.weapon.name}, "
                    f"наносит удар, но {self.armor.name} соперника его останавливает.")

        return (f"{self.name} попытался использовать {self.weapon.name}, "
                f"но у него не хватило выносливости.")

    def use_skill(self, target: BaseUnit):
        """Use special skill"""
        if self.skill_used:
            return (f"{self.name} попытался использовать {self.unit_class.skill.name}, "
                    f"но у него не хватило выносливости.")
        self.skill_used = True
        return self.unit_class.skill.use(user=self, target=target)

    # def get_damage(self, damage_inflicted: float):
    #     """Calculate damage"""
    #     self.health -= damage_inflicted - self._calculate_defence()
    #     return
