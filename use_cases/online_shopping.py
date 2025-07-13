
# Online Shopping Cart System

# Design an OOP system that simulates a shopping cart in an online store. Your system should:
# 	1.	Add items to the cart.
# 	2.	Remove items from the cart.
# 	3.	Calculate the total price.
# 	4.	Display a summary of the cart (item names, quantities, prices).

# Requirements:
# 	•	Each item must have a name, price, and quantity.
# 	•	Use at least two classes (e.g., Item, Cart).
# 	•	Apply encapsulation and separation of concerns.


class Item:

    def __init__(self, name:str, price:float, quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity
    

class Cart:

    def __init__(self):
        self.list_items = []

    def add_item(self, item):
        self.list_items.append(item)

    def remove_item(self,name_item):

        for index, item in enumerate(self.list_items):
            
            if item.name == name_item:
                self.list_items.pop(index)


    def summary(self):
        for item in self.list_items:
            print(f"The client selected {item.name} which as a price: {item.price} the number of units is: {item.quantity}")
        print(f"Total price: {self.total_price()}")
      

    def total_price(self):
        total =0
        for item in self.list_items:
            total += item.price*item.quantity
        return total
            

if __name__ == "__main__":

    item1 = Item('chocolate',100,5)
    item2 = Item('Milk', 6, 1)
    item3 = Item('Apples',10,300)
    item4 = Item('Eggs',17,35)

    cart = Cart()
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    print(f"{'*'*10} before")
    cart.summary()

    print(f"{'*'*10} after delete Apple item")
    cart.remove_item('Apples')

    cart.summary()









