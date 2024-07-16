from menu import Menu
from order import Order
from exceptions import CustomException, InvalidMenuItemError, InsufficientQuantityError

menu = Menu()
order = Order(menu)

def display_menu_options():
    while True:
        print("\n===== Menu Options =====")
        print("1. Add item to menu")
        print("2. Update item in menu")
        print("3. Delete item from menu")
        print("4. Display menu")
        print("5. Place order")
        print("6. Display receipt")
        print("7. Save menu to file")
        print("8. Load menu from file")
        print("9. Save order to file")
        print("10. Load order from file")
        print("11. Exit")
        print("========================")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                n = int(input("Total Item to be added:"))
                for i in range(n):
                    name = input("Enter item name: ")
                    price = float(input("Enter item price: "))
                    quantity = int(input("Enter item quantity: "))
                    menu.add_item(name, price, quantity)
                    print(f"Item added: {name}, {price}, {quantity}")

            elif choice == '2':
                name = input("Enter item name to update: ")
                price = float(input("Enter new price: "))
                quantity = int(input("Enter new quantity: "))
                menu.update_item(name, price, quantity)
                print("Menu updated")

            elif choice == '3':
                name = input("Enter item name to delete: ")
                menu.delete_item(name)

            elif choice == '4':
                menu.display_menu()

            elif choice == '5':
                h = int(input("Total Item to be added:"))
                for i in range(h):
                    name = input("Enter item name to order: ")
                    quantity = int(input("Enter quantity: "))
                    order.add_item_to_order(name, quantity)
                    print("Order Placed")

            elif choice == '6':
                order.generate_receipt()

            elif choice == '7':
                menu.write_menu_to_file('E:\\nimu\\menu.txt')
                print("Menu Saved Sucessfully")
                
            elif choice == '8':
                menu.read_menu_from_file('E:\\nimu\\menu.txt')
                print("Menu Loaded Sucessfully")

            elif choice == '9':
                order.write_orders_to_file('E:\\nimu\\orders.txt')
                print("Order Saved Sucessfully")

            elif choice == '10':
                order.read_orders_from_file('E:\\nimu\\orders.txt')
                print("Order Loaded Sucessfully")

            elif choice == '11':
                break

            else:
                print("Invalid choice. Please enter a number from the menu.")

        except ValueError as ve:
            print(f"ValueError: {ve}. Please enter a valid number or format.")
        except CustomException as ce:
            print(f"CustomException: {ce}")
        except InvalidMenuItemError as ime:
            print(f"InvalidMenuItemError: {ime}")
        except InsufficientQuantityError as iqe:
            print(f"InsufficientQuantityError: {iqe}")
        except FileNotFoundError as fnf:
            print(f"FileNotFoundError: {fnf}. Please check the filename and path.")
        except Exception as e:
            print(f"Error: {e}. An unexpected error occurred.")

if __name__ == "__main__":
    display_menu_options()
