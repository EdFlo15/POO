from abc import ABC, abstractmethod

# Library classes
class Vehicle(ABC):
    @abstractmethod
    def printVehicle(self):
        pass

class TwoWheeler(Vehicle):
    def printVehicle(self):
        print("I am two wheeler")

class FourWheeler(Vehicle):
    def printVehicle(self):
        print("I am four wheeler")

# Factory Interface
class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self):
        pass

# Concrete Factory for TwoWheeler
class TwoWheelerFactory(VehicleFactory):
    def createVehicle(self):
        return TwoWheeler()

# Concrete Factory for FourWheeler
class FourWheelerFactory(VehicleFactory):
    def createVehicle(self):
        return FourWheeler()

# Client class
class Client:
    def __init__(self, factory: VehicleFactory):
        self.pVehicle = factory.createVehicle()

    def getVehicle(self):
        return self.pVehicle

# Driver program
def main():
    twoWheelerFactory = TwoWheelerFactory()
    twoWheelerClient = Client(twoWheelerFactory)
    twoWheeler = twoWheelerClient.getVehicle()
    twoWheeler.printVehicle()

    fourWheelerFactory = FourWheelerFactory()
    fourWheelerClient = Client(fourWheelerFactory)
    fourWheeler = fourWheelerClient.getVehicle()
    fourWheeler.printVehicle()

if __name__ == "__main__":
    main()


# from https://www.geeksforgeeks.org/system-design/factory-method-for-designing-pattern/