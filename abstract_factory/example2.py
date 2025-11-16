from abc import ABC, abstractmethod

class Ride(ABC):
    @abstractmethod
    def get_info(self) -> str:
        pass

class FoodStall(ABC):
    @abstractmethod
    def get_info(self) -> str:
        pass



# Fantasy-themed products
class MagicCarpetRide(Ride):
    def get_info(self) -> str:
        return "Magic Carpet Ride: A thrilling flight on a flying carpet."

class GnomeSweetShop(FoodStall):
    def get_info(self) -> str:
        return "Gnome Sweet Shop: Serving enchanted gingerbread and honey cakes."

# Sci-Fi-themed products
class SpaceshipRide(Ride):
    def get_info(self) -> str:
        return "Spaceship Ride: A futuristic journey through the galaxy."

class RobotCafe(FoodStall):
    def get_info(self) -> str:
        return "Robot Cafe: Dispensing automated snacks and energy drinks."



# define abstract factory
class ThemeParkFactory(ABC):
    @abstractmethod
    def create_ride(self) -> Ride:
        pass

    @abstractmethod
    def create_food_stall(self) -> FoodStall:
        pass


class FantasyThemeFactory(ThemeParkFactory):
    def create_ride(self) -> Ride:
        return MagicCarpetRide()

    def create_food_stall(self) -> FoodStall:
        return GnomeSweetShop()

class SciFiThemeFactory(ThemeParkFactory):
    def create_ride(self) -> Ride:
        return SpaceshipRide()

    def create_food_stall(self) -> FoodStall:
        return RobotCafe()
