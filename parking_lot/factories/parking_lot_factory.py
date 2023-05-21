from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from parking_lot.parking_lot.parking_lot import ParkingLot
from parking_lot.account.address import Address
from parking_lot.payment.fee_model import MallFeeModel, StadiumFeeModel, \
    AirportFeeModel


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
    def get_parking_lot(self, spot_defn: SpotDefinition, addr: Address):
        "Returns a parking lot"


class MallParkingLotFactory(ParkingLotFactory):
    def get_parking_lot(self, spot_defn, addr):
        fee_model = MallFeeModel
        return ParkingLot(fee_model=fee_model, spots=spot_defn, address=addr)


class StadiumParkingLotFactory(ParkingLotFactory):
    
    def get_parking_lot(self, spot_defn, addr):
        fee_model = StadiumFeeModel()
        return ParkingLot(fee_model=fee_model, spots=spot_defn, address=addr)


class AirportParkingLotFactory(ParkingLotFactory):
    def get_parking_lot(self, spot_defn, addr):
        fee_model = AirportFeeModel()
        return ParkingLot(fee_model=fee_model, spots=spot_defn, address=addr)
