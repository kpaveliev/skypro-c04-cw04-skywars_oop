from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from assets.units import BaseUnit


class BaseSkill(ABC):
    """Base class for special skills"""
    name: str = None
    damage: float = 0
    stamina_required: float = 0
    user = None
    target = None

    @abstractmethod
    def _skill_effect(self):
        pass

    def use(self, user: BaseUnit, target: BaseUnit):
        """Use special skill if user has enough stamina"""
        self.user = user
        self.target = target
        if self.user.stamina_points < self.stamina_required:
            return f"{user.name} tried to use {self.name}, but {user.stamina_points} wasn't enough"
        return self._skill_effect()
