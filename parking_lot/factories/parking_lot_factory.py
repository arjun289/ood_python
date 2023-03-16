from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto


class FeeModelType(Enum):
    MALL = auto()
    STADIUM = auto()
    AIRPORT = auto()


@dataclass
class SpotDefinition:
    """
    Class to define number of spots for different types of vehciles in a
    parking lot. This is used while initlalizing a parking lot.
    """
    motorbikes_scooters: int
    cars_suvs: int
    trucks_buses: int


class ParkingLotFactory(ABC):
    @abstractmethod
    def get_parking_lot(self, spot_defn: SpotDefinition):
        "Returns a parking lot"


class MallParkingLotFactory(ParkingLotFactory):
    def get_parking_lot(self, spot_defn: SpotDefinition):
        return


class StadiumParkingLotFactory(ParkingLotFactory):
    def get_parking_lot(self, spot_defn: SpotDefinition):
        return


class AirportParkingLotFactory(ParkingLotFactory):
    def get_parking_lot(self, spot_defn: SpotDefinition):
        return
