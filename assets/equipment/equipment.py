import json
from typing import List

from assets.equipment.armor import ArmorSchema, Armor
from assets.equipment.equipment_data import EquipmentData
from assets.equipment.weapon import WeaponSchema, Weapon
from config import BaseConfig


class Equipment:
    """Interface to communicate with the Unit"""

    def __init__(self, filename: str):
        self.filename = filename
        self.equipment: EquipmentData = self._create_equipment()

    def _create_equipment(self) -> EquipmentData:
        """Create EquipmentData from json file"""
        with open(self.filename, encoding='utf-8') as file:
            data = json.load(file)

            return EquipmentData(
                    weapons=WeaponSchema(many=True).load(data['weapons']),
                    armor=ArmorSchema(many=True).load(data['armors']))

    def get_weapon(self, weapon_name: str) -> Weapon:
        """Get Weapon by name"""
        for weapon in self.equipment.weapons:
            if weapon.name == weapon_name:
                return weapon

    def get_weapon_names(self) -> List[Weapon]:
        """Get list of all available weapons (names)"""
        return [weapon.name for weapon in self.equipment.weapons]

    def get_armor(self, armor_name: str) -> Armor:
        """Get Armor by name"""
        for armor in self.equipment.armor:
            if armor.name == armor_name:
                return armor

    def get_armor_names(self) -> List[Armor]:
        """Get list of all available armor (names)"""
        return [armor.name for armor in self.equipment.armor]


if __name__ == '__main__':
    equipment = Equipment(BaseConfig.EQUIPMENT_PATH)
    print(equipment.equipment)
    print(equipment.get_weapon('топорик'))
    print(equipment.get_armor('кожаная броня'))
    print(equipment.get_weapon_names())
    print(equipment.get_armor_names())
