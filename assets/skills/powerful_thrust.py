from assets.skills import BaseSkill


class PowerfulThrust(BaseSkill):
    """Special skill"""
    name: str = 'Мощный укол'
    damage: float = 15.0
    stamina_required: float = 5.0

    def _skill_effect(self) -> str:
        self.target.health -= self.damage
        self.user.stamina -= self.stamina_required
        return f'{self.user.name} uses {self.name} and inflict {self.damage} to {self.target.name}'
