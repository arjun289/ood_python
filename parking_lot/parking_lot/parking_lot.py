from parking_lot.payment.fee_model import FeeModel
from uuid import uuid1
from parking_lot.account.address import Address
from parking_lot.parking_lot.vehicle import Vehicle


class ParkingLot:
    def __init__(self, fee_model: FeeModel, address: Address, spots) -> None:
        self.fee_model = fee_model
        self.address = address
        self.parking_slots = self._init_parking_spot(spots)
        self.display_board = self._init_display_board()
        self.entry = ParkingEntry("Entry1")
        self.exit = ParkingExit("Exit1")

    def _init_parking_spot(self):
        pass

    def _init_display_board(self):
        pass

    def park_vehicle(self, vehicle: Vehicle):
        pass

    def remove_vehicle(self, vehicle: Vehicle):
        pass


class ParkingEntry:
    def __init__(self, name: str) -> None:
        self.id = uuid1()
        self.name = name

    def generate_uuid(self):
        return uuid1()


class ParkingExit:
    def __init__(self, name: str) -> None:
        self.id = uuid1()
        self.name = name

    def generate_uuid(self):
        return uuid1()
