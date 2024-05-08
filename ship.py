from enum import Enum


class ShipType(Enum):
    type1 = "a"
    type2 = "b"
    type3 = "c"


class Ship:
    @staticmethod
    def getTypes():
        return [
            ShipType.type1.name,
            ShipType.type2.name,
            ShipType.type3.name,
        ]
