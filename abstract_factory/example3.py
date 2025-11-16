from abc import ABC, abstractmethod

# -----------------------------
# PRODUCT A: Pizza
# -----------------------------
class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass


class ItalianPizza(Pizza):
    def prepare(self):
        print("Preparing Italian pizza: buffalo mozzarella, fresh basil")


class AmericanPizza(Pizza):
    def prepare(self):
        print("Preparing American pizza: thick crust, extra cheese")


# -----------------------------
# PRODUCT B: Drink
# -----------------------------
class Drink(ABC):
    @abstractmethod
    def pour(self):
        pass


class ItalianDrink(Drink):
    def pour(self):
        print("Pouring Italian red wine")


class AmericanDrink(Drink):
    def pour(self):
        print("Pouring American cola")


# -----------------------------
# ABSTRACT FACTORY
# -----------------------------
class MealFactory(ABC):
    @abstractmethod
    def create_pizza(self):
        pass

    @abstractmethod
    def create_drink(self):
        pass


# -----------------------------
# CONCRETE FACTORIES
# -----------------------------
class ItalianMealFactory(MealFactory):
    def create_pizza(self):
        return ItalianPizza()

    def create_drink(self):
        return ItalianDrink()


class AmericanMealFactory(MealFactory):
    def create_pizza(self):
        return AmericanPizza()

    def create_drink(self):
        return AmericanDrink()


# -----------------------------
# CLIENT CODE
# -----------------------------
def serve_meal(factory: MealFactory):
    pizza = factory.create_pizza()
    drink = factory.create_drink()

    print("--- Serving Meal ---")
    pizza.prepare()
    drink.pour()
    print()


if __name__ == "__main__":
    serve_meal(ItalianMealFactory())
    serve_meal(AmericanMealFactory())