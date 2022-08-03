from assets.skills import BaseSkill


class FerociousKick(BaseSkill):
    """Special skill"""
    name: str = 'Свирепый пинок'
    damage: float = 12.0
    stamina_required: float = 6.0

    def _skill_effect(self):
        """Decrease target health and decrease user stamina"""
        self.target.health -= self.damage
        self.user.stamina -= self.stamina_required
        return f'{self.user.name} uses {self.name} and inflict {self.damage} to {self.target.name}'
