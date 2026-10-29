
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        item = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["price"] * item["quantity"]
        return total

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return
        print("Item not found")

cart1 = ShoppingCart()
cart1.add_item("Book", 500, 2)
cart1.add_item("Pen", 50, 3)

cart2 = ShoppingCart()
cart2.add_item("Bag", 1500, 1)
cart2.add_item("Shoes", 2000, 2)

print("Cart 1 Total:", cart1.calculate_total())
print("Cart 2 Total:", cart2.calculate_total())
