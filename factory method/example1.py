# -----------------------------
# PRODUCT
# -----------------------------
class Pizza:
    def prepare(self):
        raise NotImplementedError

    def bake(self):
        print("Baking at 200°C")

    def cut(self):
        print("Cutting pizza into 8 slices")

    def box(self):
        print("Placing pizza into official box")


# -----------------------------
# CONCRETE PRODUCTS
# -----------------------------
class MargheritaPizza(Pizza):
    def prepare(self):
        print("Preparing Margherita: tomato, mozzarella, basil")


class PepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing Pepperoni: tomato, mozzarella, pepperoni")


class HawaiianPizza(Pizza):
    def prepare(self):
        print("Preparing Hawaiian: tomato, mozzarella, ham, pineapple")


# -----------------------------
# CREATOR (FACTORY METHOD)
# -----------------------------
class Pizzeria:
    def order_pizza(self, type_):
        pizza = self.create_pizza(type_)  # FACTORY METHOD
        print(f"--- Making a {pizza.__class__.__name__} ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        print()
        return pizza

    def create_pizza(self, type_):
        raise NotImplementedError


# -----------------------------
# CONCRETE CREATORS
# -----------------------------
class ItalianPizzeria(Pizzeria):
    def create_pizza(self, type_):
        if type_ == "margherita":
            return MargheritaPizza()
        elif type_ == "pepperoni":
            return PepperoniPizza()
        else:
            raise ValueError("Italian pizzeria only makes margherita or pepperoni")


class AmericanPizzeria(Pizzeria):
    def create_pizza(self, type_):
        if type_ == "pepperoni":
            print("Adding extra cheese (American style!)")
            return PepperoniPizza()
        elif type_ == "hawaiian":
            return HawaiianPizza()
        else:
            raise ValueError("American pizzeria only makes pepperoni or hawaiian")


# -----------------------------
# CLIENT CODE
# -----------------------------
if __name__ == "__main__":
    italian = ItalianPizzeria()
    italian.order_pizza("margherita")
    
    american = AmericanPizzeria()
    american.order_pizza("hawaiian")