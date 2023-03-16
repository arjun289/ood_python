from factories.parking_lot_factory import StadiumParkingLotFactory, \
    MallParkingLotFactory, AirportParkingLotFactory, \
    SpotDefinition, FeeModelType


def get_parking_lot(spot_defn: SpotDefinition, model: FeeModelType):
    """
    Returns a parking lot based on the passed arguments.
    Parameters:
    spot_defn: The function expects a spot definition object containing number
        of vehciles of certain type.
    model: Fee Model to be used for the parking lot. See FeeModel class for
        more details.
    """
    factory = {
        model.STADIUM: StadiumParkingLotFactory(spot_defn),
        model.MALL: MallParkingLotFactory(spot_defn),
        model.AIRPORT: AirportParkingLotFactory(spot_defn)
    }

    parking_lot = factory[SpotDefinition]
    return parking_lot
