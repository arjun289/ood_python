from parking_lot.factories.parking_lot_factory import MallParkingLotFactory, \
    SpotDefinition
from parking_lot.account.address import Address
import pytest


@pytest.fixture
def mall_spot_defn():
    spot_defn = SpotDefinition(motorbikes_scooters=100, cars_suvs=80,
                               trucks_buses=10)
    return spot_defn


@pytest.fixture
def address():
    address = Address(address="9 victoria lane", city="London", country="UK", 
                      zip_code="E32FH")
    return address


def test_mall_parking_lot_factory(mall_spot_defn, address):
    pl = MallParkingLotFactory()
    pl.get_parking_lot(spot_defn=mall_spot_defn, addr=address)
    