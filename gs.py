from datetime import datetime

class Product:
    def __init__(self, name, category, price, quantity,manufacturing_date, expiration_date):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.manufacturing_date=datetime.strptime(manufacturing_date, "%Y-%m-%d")
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")

    def is_expired(self):
        return datetime.now() > self.expiration_date

    def to_string(self):
        return f"Name: {self.name}, Category: {self.category}, Price: ${self.price:.2f}, Quantity: {self.quantity}, Manufacturing Date: {self.manufacturing_date.strftime('%Y-%m-%d')},Expiration Date: {self.expiration_date.strftime('%Y-%m-%d')}"

Inventory = []
Category_dict = {}

def add_product_to_inventory(product):   
    if product.name not in [p.name for p in Inventory]:
        Inventory.append(product)
        if product.category not in Category_dict:
            Category_dict[product.category] = []
        Category_dict[product.category].append(product)
        print("Product added successfully")
    else:
        print("Product already exists in the inventory")

def remove_product_from_inventory(name, Inventory):   
    product_to_remove = None
    for product in Inventory:
        if product.name == name:
            product_to_remove = product
            break
    if product_to_remove:
        Inventory.remove(product_to_remove)
        if product_to_remove.category in Category_dict:
            Category_dict[product_to_remove.category].remove(product_to_remove)
        print("Product removed successfully")
    else:
        print("Product not found")


def search_products(search_term):   
    found_products = []
    for product in Inventory:
        if search_term in product.name or search_term in product.category:
            found_products.append(product)
    if found_products:
        for product in found_products:
            print("Product found: ", product.to_string())
    else:
        print("Product not found")


def list_all_products(Inventory):     
    if not Inventory:
        print("No products in the inventory")
    else:
        for product in Inventory:
            print(product.to_string())

def categorize_products():       
    for category, products in Category_dict.items():
        print(f"Category: {category}")
        for product in products:
            print(product.to_string())

def check_expired_products(Inventory):
    expired_products = [product for product in Inventory if product.is_expired()]
    if expired_products:
        for product in expired_products:
            print(f"Expired product: {product.to_string()}")
        Inventory[:] = [product for product in Inventory if not product.is_expired()]
        for category, products in Category_dict.items():
            Category_dict[category] = [product for product in products if not product.is_expired()]
        print("Expired products have been removed from inventory")
    else:
        print("No expired products found")

def save_inventory():
    try:
        with open('gs.txt', 'w') as file:
            for product in Inventory:
                file.write(f"{product.name},{product.category},{product.price},{product.quantity},{product.manufacturing_date.strftime('%Y-%m-%d')},{product.expiration_date.strftime('%Y-%m-%d')}\n")
        print(f"Inventory saved to file successfully")
    except IOError:
        print(f"Error: Could not save inventory to the file")

def load_inventory():
    global Inventory, Category_dict
    try:
        with open('gs.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, category, price, quantity, manufacturing_date, expiration_date = line.strip().split(',')
                product = Product(name, category, float(price), int(quantity), manufacturing_date, expiration_date)
                add_product_to_inventory(product)
        print(f"Inventory loaded from file successfully")
    except IOError:
        print(f"Error: Could not load inventory from file")

while True:
    print("1. Add a product")
    print("2. Remove a product")
    print("3. Search for products")
    print("4. List all products")
    print("5. Categorize products")
    print("6. Check for expired products")
    print("7. Save inventory to file")
    print("8. Load inventory from file")
    print("9. Exit")
    
    d = int(input("Enter a number between 1 and 9: "))

    if d == 1:
        n = int(input("Enter the number of products to be added to the inventory: "))
        for i in range(n):
            name = str(input("Enter product name: "))
            category = str(input("Enter product category: "))
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            manufacturing_date=str(input("Enter product manufacturing date (YYYY-MM-DD): "))
            expiration_date = str(input("Enter product expiration date (YYYY-MM-DD): "))
            product = Product(name, category, price, quantity, manufacturing_date, expiration_date)
            add_product_to_inventory(product)

    elif d == 2:
        name = str(input("Enter the product name to be removed: "))
        remove_product_from_inventory(name,Inventory)

    elif d == 3:
        search_term = str(input("Enter the product name or category to be searched: "))
        search_products(search_term)

    elif d == 4:
        list_all_products(Inventory)

    elif d == 5:
        categorize_products()

    elif d == 6:
        check_expired_products(Inventory)

    elif d == 7:
        save_inventory()

    elif d == 8:
        load_inventory()

    elif d == 9:
        break

    else:
        print("Invalid Choice")
