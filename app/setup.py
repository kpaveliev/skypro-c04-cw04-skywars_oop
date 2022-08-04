from assets.arena.arena import Arena
from assets.equipment import Equipment
from app.config import BaseConfig
from assets.unit_classes import WarriorClass, ThiefClass


equipment = Equipment(BaseConfig.EQUIPMENT_PATH)

heroes = {
    'player': None,
    'enemy': None
}

unit_classes = {WarriorClass.name: WarriorClass,
                ThiefClass.name: ThiefClass}

arena = Arena()