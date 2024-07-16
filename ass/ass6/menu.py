from menu_item import MenuItem
from order import Order
from exceptions import CustomException, InvalidMenuItemError, InsufficientQuantityError


class Menu:
    def __init__(self):
        self.menu_items = {}

    def add_item(self, name, price, quantity):
        if name in self.menu_items:
            raise CustomException(f"Item '{name}' already exists in the menu.")
        self.menu_items[name] = MenuItem(name, price, quantity)

    def update_item(self, name, price, quantity):
        if name not in self.menu_items:
            raise CustomException(f"Item '{name}' not found in the menu.")
        self.menu_items[name].price = price
        self.menu_items[name].quantity = quantity

    def delete_item(self, name):
        if name not in self.menu_items:
            raise CustomException(f"Item '{name}' not found in the menu.")
        del self.menu_items[name]
        print(f"Item deleted: {name}")

    def display_menu(self):
        if not self.menu_items:
            print("No items in the menu.")
        else:
            for name, item in self.menu_items.items():
                print(item)

    def write_menu_to_file(self, filename):
        with open(filename, 'w') as file:
            for name, item in self.menu_items.items():
                file.write(f"{name},{item.price},{item.quantity}\n")

    def read_menu_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                name, price, quantity = line.strip().split(',')
                self.menu_items[name] = MenuItem(name, float(price), int(quantity))
