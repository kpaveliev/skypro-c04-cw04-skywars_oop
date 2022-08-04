from assets.skills import PowerfulThrust, FerociousKick
from assets.classes import UnitClass


WarriorClass = UnitClass(name='Воин', max_health=50.0, max_stamina=25.0, attack_modifier=1.5,
                         stamina_modifier=1.2, armor_modifier=1.0, skill=PowerfulThrust())

ThiefClass = UnitClass(name='Вор', max_health=50.0, max_stamina=25.0, attack_modifier=1.5,
                       stamina_modifier=1.2, armor_modifier=1.0, skill=FerociousKick())

unit_classes = {WarriorClass.name: WarriorClass,
                ThiefClass.name: ThiefClass}
