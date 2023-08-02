# Design Parking Garage System
# a garage may be full, so the customer won't be able to book it

# support different sizes? small car, SUV/van

from abc import ABC, abstractmethod
from enum import Enum


class ParkingStatus(Enum):
    EMPTY = 0
    RESERVED = 1
    FILLED = 2

class VehicleSize(Enum):
    SMALL = 0
    LARGE = 1

class Vehicle(ABC):
    def __init__(self, size: VehicleSize, plate: str):
        self.size = size
        self.plateNum = plate

    
class SmallCar(Vehicle):
    
    
class LargeCar(Vehicle):
    
    
class ParkingSpot(ABC):
    size: VehicleSize
    status: ParkingStatus
    
    def empty(self):
        self.status = 0
        
    def reserve(self):
        self.status = 1
    
    def fill(self):
        self.status = 2
    
class LargeSpot(ParkingSpot):
    
class SmallSpot(ParkingSpot):
    
class ParkingLot:
    def __init__(self, small_spots: list[SmallSpot], large_spots: list[LargeSpot]):
        self.small_spots = small_spots
        self.large_spots = large_spots
    
    def get_next_available(self, size):
        if size == "SMALL":
            for spot in self.small_spots:
                if spot.status == 0:
                    return spot
        return False
    
    def is_full(self):
        pass
    
class ticketSystem:
    ''''''
    def __init__(self, lot: ParkingLot):
        self.parkingLot = lot
        self.next_small = 0
        self.next_large = 0
    
    def get_ticket(self, size: VehicleSize):
        '''Check if we can allocate a spot, return that spot if yes'''
        # reserve the next small spot, then return the index
        spot = self.parkingLot.small_spots.get_next_available(size)
        if not spot:
            return "Error"
        spot.reserve()
        return spot.number
        
    def check_in(self, size, ticket):
        if size == "SMALL":
            self.parkingLot.small_spots[ticket].fill()
        elif size == "LARGE":
            self.parkingLot.large_spots[ticket].fill()
    
    def check_out(self, size, ticket):
        if size == "SMALL":
            self.parkingLot.small_spots[ticket].empty()
        elif size == "LARGE":
            self.parkingLot.large_spots[ticket].empty()
    
    
    