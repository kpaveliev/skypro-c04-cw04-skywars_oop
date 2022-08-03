from dataclasses import dataclass

from assets.skills import BaseSkill, PowerfulThrust
from assets.heroes import UnitClass


@dataclass
class Thief(UnitClass):
    """Thief class"""
    name: str = 'Вор'
    max_health: float = 50.0
    max_stamina: float = 25.0
    attack_modifier: float = 1.5
    stamina_modifier: float = 1.2
    armor_mod: float = 1.0
    skill: BaseSkill = PowerfulThrust

if __name__ == '__main__':
    thief = Thief()
    print(thief)
