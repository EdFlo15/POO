from abc import ABC, abstractmethod

# ============================
#  Abstract Products
# ============================

class Predator(ABC):
    @abstractmethod
    def hunt(self):
        pass


class Herbivore(ABC):
    @abstractmethod
    def eat_plants(self):
        pass


# ============================
#  Concrete Products (Jungle)
# ============================

class Tiger(Predator):
    def hunt(self):
        return "Tiger hunts in the jungle"


class Deer(Herbivore):
    def eat_plants(self):
        return "Deer eats plants in the jungle"


# ============================
#  Concrete Products (Ocean)
# ============================

class Shark(Predator):
    def hunt(self):
        return "Shark hunts in the ocean"


class SeaTurtle(Herbivore):
    def eat_plants(self):
        return "Sea turtle eats seaweed"


# ============================
#  Abstract Factory
# ============================

class AnimalFactory(ABC):
    @abstractmethod
    def create_predator(self) -> Predator:
        pass

    @abstractmethod
    def create_herbivore(self) -> Herbivore:
        pass


# ============================
#  Concrete Factories
# ============================

class JungleAnimalFactory(AnimalFactory):
    def create_predator(self) -> Predator:
        return Tiger()

    def create_herbivore(self) -> Herbivore:
        return Deer()


class OceanAnimalFactory(AnimalFactory):
    def create_predator(self) -> Predator:
        return Shark()

    def create_herbivore(self) -> Herbivore:
        return SeaTurtle()


# ============================
#  Client Code
# ============================

def explore(factory: AnimalFactory):
    predator = factory.create_predator()
    herbivore = factory.create_herbivore()

    print(predator.hunt())
    print(herbivore.eat_plants())


# ============================
#  Run Example
# ============================

if __name__ == "__main__":
    print("Jungle Ecosystem:")
    explore(JungleAnimalFactory())

    print("\nOcean Ecosystem:")
    explore(OceanAnimalFactory())