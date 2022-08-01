from dataclasses import dataclass


@dataclass
class Armor:
    """Class for armor"""
    name: str
    defence: float
    stamina_per_turn: float

ArmorSchema = marshmallow_dataclass.class_schema(Armor)