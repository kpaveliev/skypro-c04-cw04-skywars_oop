from assets.heroes.hero import Hero
from assets.skills.skill import Skill


class PowerfulThrust(Skill):
    """Special skill"""
    name: str = 'Мощный укол'
    damage: float = 15
    stamina_required: float = 5

    def skill_effect(self, user: Hero, target: Hero):
        target.max_health -= self.damage
        return f'{user.name} uses {self.name} and inflict {self.damage} to {target.name}'