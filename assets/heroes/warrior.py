from dataclasses import dataclass

from assets.skills import BaseSkill, FerociousKick
from base_hero import BaseHero


@dataclass
class Warrior(BaseHero):
    """Warrior class"""
    name: str = 'Воин'
    max_health: float = 60.0
    max_stamina: float = 30.0
    attack_mod: float = 0.8
    stamina_mod: float = 0.9
    armor_mod: float = 1.2
    skill: BaseSkill = FerociousKick

if __name__ == '__main__':
    warrior = Warrior()
    print(warrior)