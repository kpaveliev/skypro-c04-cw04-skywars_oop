from assets.heroes.hero import Hero
from assets.skills.skill import Skill


class FerociousKick(Skill):
    """Special skill"""
    name: str = 'Свирепый пинок'
    damage: float = 12
    stamina_required: float = 6

    def skill_effect(self, user: Hero, target: Hero):
        target.max_health -= self.damage
        return f'{user.name} uses {self.name} and inflict {self.damage} to {target.name}'
