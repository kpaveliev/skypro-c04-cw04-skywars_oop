from dataclasses import dataclass
from random import uniform

import marshmallow
import marshmallow_dataclass


@dataclass
class Weapon:
    """Class for weapons"""
    name: str
    min_damage: float
    max_damage: float
    stamina_per_attack: float

    class Meta:
        unknown = marshmallow.EXCLUDE

    def calculate_damage(self):
        """Calculate inflicted damage"""
        return uniform(self.min_damage, self.max_damage)


WeaponSchema = marshmallow_dataclass.class_schema(Weapon)
