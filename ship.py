from enum import Enum


class ShipType(Enum):
    fishing = "peche"
    transportation = "transport"
    tourist = "tourist"

class Propulsion(Enum):
    gas = "gas"
    elect = "electrique"
    

class Ship:
    @staticmethod
    def getTypes():
        return [
            ShipType.fishing.value,
            ShipType.transportation.value,
            ShipType.tourist.value,
        ]
    
    @staticmethod
    def getPropultion():
        return [
        Propulsion.gas.value,
        Propulsion.elect.value,
        ]
    


