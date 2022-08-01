import json
from dataclasses import dataclass, field

from assets.equipment.armor import ArmorSchema
from assets.equipment.equipment_data import EquipmentData
from assets.equipment.weapon import WeaponSchema


@dataclass
class Equipment:
    """Interface to communicate with Hero"""

    def __init__(self, filename: str):
        self.filename = filename
        self._create_equipment()

    def _create_equipment(self):
        with open(self.filename, encoding='utf-8') as file:
            data = json.load(file)
            EquipmentData(
                weapons=WeaponSchema(many=True).load(data['weapons']),
                armor=ArmorSchema(many=True).load(data['armor']))




