# ParkingLot

### Description
A parking lot is a dedicated area that is intended for parking vehicles. Parking 
lots are present in every city and suburban area. Shopping malls, stadiums, airports, train stations, and similar venues often feature a parking lot with a large capacity. A parking lot can spread across multiple buildings with multiple floors or can be in a large open area.
- The parking lot will allow different types of vehicles to be parked:
- Motorcycles/Scooters
- Cars/SUVs
- Buses/Trucks
- Each vehicle will occupy a single spot and the spot size will be different for different
vehicles.
- The number of spots per vehicle type will be different for different parking lots. For
example
- Motorcycles/scooters: 100 spots
- Cars/SUVs: 80 spots
- Buses/Trucks: 40 spots
- When a vehicle is parked, a parking ticket should be generated with the spot number
and the entry date-time.
- When a vehicle is unparked, a receipt should be generated with the entry date-time,
exit date-time, and the applicable fees to be paid.

### Fee Model
Different locations have different fee models. Below are a few possible models:

**Mall**

Per-hour flat fees

| **Vehicle** | **Fee** |
|-------------|---------|
| Motorcyle   | 10      |
| Car/SUV     | 20      |
| Bus/Truck   | 50      |

**Stadium**
Flat rate up to a few hours and then per-hour rate. The total fee is the sum of 
all the previous interval fees. No parking spots for buses/trucks at the stadium.

| **Vehicle** | **Interval**                                    | **Fee**             |
|-------------|-------------------------------------------------|---------------------|
| Motorcycle  | [0, 4) hours<br> [4, 12) hours<br> [12, Infinity) hours | 30<br> 60<br>  100 per hour |
| Car/SUV     | [0, 4) hours<br> [4, 12) hours<br> [12, Infinity) hours | 60<br> 120<br> 200 per hour |
As stated by the notation, the start times are inclusive and the end times are exclusive.

** Airport
Flat rate up to one day. Then per-day rate. There is no summing up of the previous interval fees. No parking spots for buses/trucks at the airport.

| **Vehicle** | **Interval**                                                 | **Fee**        |
|-------------|--------------------------------------------------------------|----------------|
| Motorcycle  | [0, 1) hours<br> [1, 8) hours<br> [8, 24) hours<br> Each day | Free<br> 40<br> 60<br> 80 |
| Car/SUV     | [0, 12) hours<br> [12, 24) hours<br> Each day            | 60<br> 80<br> 100      |

As stated by the notations, the start times are inclusive and end times are exclusive.

## Use Case
Checkout the use case diagram

## System Components

### Vehicle
- attrs: license_number, vehicle_type
- methods: assignTicket()

### ParkingSpot
- attrs: id, isfree?
- methods: get_is_free()

### DisplayBoard
- attrs: id, motorcycle_slots, car_slots, bus_slots
- methods: showFreeslots()

### Entrance and Exit()
- attrs: id, 
- methods: get_ticket(), validate_ticket()

### ParkingTicket 
- attrs: ticket_no, timestamp, spot_number, vehicle_type

### ExitReceipt
- attrs: entry_timestamp, exit_timestamp, spot, vechicle_type, fees 

### ParkingLotType

## ParkingFloor

### ParkingLot
- attrs: id,name, address
- composition: parkingspots, entrance/exit, lot_type, parking_floor

