from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, license_no) -> None:
        self.__license_no = license_no

    @abstractmethod
    def assign_ticket(self, ticket):
        pass


class Car(Vehicle):
    def __init__(self, license_no) -> None:
        super().__init__(license_no)

    def assign_ticket(self, ticket):
        pass


class Truck(Vehicle):
    def __init__(self, license_no) -> None:
        super().__init__(license_no)

    def assign_ticket(self, ticket):
        pass


class Motorcycle(Vehicle):
    def __init__(self, license_no) -> None:
        super().__init__(license_no)

    def assign_ticket(self, ticket):
        pass
