import os

BASEDIR = os.path.dirname(os.path.abspath(__file__))


class BaseConfig:
    EQUIPMENT_PATH = "../../data/equipment.json"
    # EQUIPMENT_PATH = os.path.join(os.path.dirname(BASEDIR), "data/equipment.json")
