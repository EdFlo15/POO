class Sandwich:
    def __init__(self):
        self.bread = None
        self.meat = None
        self.cheese = None

    def __str__(self):
        return f"Bread: {self.bread}, Meat: {self.meat}, Cheese: {self.cheese}"


class SandwichBuilder:
    def __init__(self):
        self.sandwich = Sandwich()

    def set_bread(self, bread):
        self.sandwich.bread = bread
        return self

    def set_meat(self, meat):
        self.sandwich.meat = meat
        return self

    def set_cheese(self, cheese):
        self.sandwich.cheese = cheese
        return self

    def build(self):
        return self.sandwich


builder = SandwichBuilder()
sandwich1 = (
    builder
    .set_bread("white")
    .set_meat("chicken")
    .set_cheese("cheddar")
    .build()
)

print("Sandwich 1:", sandwich1)


builder = SandwichBuilder()
sandwich2 = (
    builder
    .set_bread("wheat")
    .set_cheese("mozzarella")
    .build()
)

print("Sandwich 2:", sandwich2)

#avoid the use of this:
#Sandwich(bread="white", meat="chicken", cheese="cheddar", sauce=None, extra=None, ...)