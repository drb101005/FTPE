#To Apply OOP principles
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item_name, qty):
        self.items.append((item_name, qty))
    
    def remove_item(self, item_name):
        self.items = [item for item in self.items if item[0] != item_name]
    
    def calculate_total(self):
        return sum(qty for _, qty in self.items)

# Example usage
cart = ShoppingCart()
cart.add_item("Papaya", 100)
cart.add_item("Apple", 5)
cart.add_item("Orange", 10)

print("Current items in cart:")
for name, qty in cart.items:
    print(f"{name} - {qty}")

print("Total Quantity:", cart.calculate_total())

cart.remove_item("Orange")
print("\nUpdated items after removing Orange:")
for name, qty in cart.items:
    print(f"{name} - {qty}")

print("Total Quantity:", cart.calculate_total())