from exceptions import InvalidMenuItemError, InsufficientQuantityError

class Order:
    def __init__(self, menu):
        self.menu = menu
        self.items = {}

    def add_item_to_order(self, name, quantity):
        if name not in self.menu.menu_items:
            raise InvalidMenuItemError(f"Item '{name}' not found in the menu.")
        if quantity > self.menu.menu_items[name].quantity:
            raise InsufficientQuantityError(f"Insufficient quantity available for '{name}'.")
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

    def calculate_total(self):
        total = 0
        for name, quantity in self.items.items():
            total += self.menu.menu_items[name].price * quantity
        return total

    def generate_receipt(self):
        print("------ Receipt ------")
        for name, quantity in self.items.items():
            item = self.menu.menu_items[name]
            print(f"{item.name} x{quantity}: Rs.{item.price:.2f} each")
        total = self.calculate_total()
        print(f"Total: Rs.{total:.2f}")

    def write_orders_to_file(self, filename):
        with open(filename, 'w') as file:
            for name, quantity in self.items.items():
                file.write(f"{name},{quantity}\n")

    def read_orders_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                name, quantity = line.strip().split(',')
                self.items[name] = int(quantity)
