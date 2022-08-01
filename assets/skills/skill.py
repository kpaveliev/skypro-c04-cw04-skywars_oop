from abc import ABC, abstractmethod
from dataclasses import dataclass

from assets.heroes.hero import Hero


@dataclass
class Skill(ABC):
    """Base class for skills"""
    name: str
    damage: float
    stamina_required: float

    @abstractmethod
    def skill_effect(self, user: Hero, target: Hero):
        pass

    def use(self, user: Hero, target: Hero):
        """"""
        if user.stamina < self.stamina_required:
            return f"{user.name} tried to use {self.name}, but {user.stamina} wasn't enough"
        return self.skill_effect(user, target)
