class Vehicle:
    def __init__(self, vehicle_id, brand, model, year, category):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.year = year
        self.category = category
        
    def to_string(self):
        return f"ID: {self.vehicle_id}, Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Category: {self.category}"


Rental_System= []
Vehicles_set = {}

def add_vehicle(vehicle):
    if vehicle.vehicle_id not in Vehicles_set:
        Rental_System.append(vehicle)
        Vehicles_set[vehicle.vehicle_id] = vehicle
        print("Vehicle added successfully")
    else: 
        v=list[vehicle]
        Vehicles_set[vehicle_id] = v
        print("Vehicle already exists in the library")

def remove_vehicle(vehicle_id):
    if vehicle_id in Vehicles_set:
            vehicle=Vehicles_set[vehicle_id]
            Rental_System.remove(vehicle)
            del Vehicles_set[vehicle_id]
            print("Vehicle removed successfully")
            return
    print("Vehicle not found")

def search_vehicle(vehicle_id):
    if vehicle_id in Vehicles_set:
        print("Vehicle found: ", Vehicles_set[vehicle_id].to_string())
    else:
        print("Vehicle not found")

def list_vehicles(Rental_System):
    if not Rental_System:
        print("No vehicles in the system")
    else:
        for vehicle in Rental_System:
            print(vehicle.to_string())

def categorize_vehicle():
    categories = {}
    for vehicle in Rental_System:
        if vehicle.category not in categories:
            categories[vehicle.category] = []
        categories[vehicle.category].append(vehicle)
    for category, vehicles in categories.items():
        print("Category: ", category)
        for vehicle in vehicles:
            print(vehicle.to_string())


while True:
    print("1. Add a vehicle")
    print("2. Remove a vehicle")
    print("3. Search for vehicles")
    print("4. List all vehicles")
    print("5. Categorize vehicles")
    print("6. Exit")
    d = int(input("Enter a number between 1 and 6: "))

    if d == 1:
        n = int(input("Enter the number of vehicles to be added in the system:"))
        for i in range(n):
            vehicle_id=str(input("Enter vehicle id:"))
            brand=str(input("Enter the Brand of vehicle:"))
            model=str(input("Enter the model of vehicle:"))
            year=int(input("Enter vehicle year:"))
            category=str(input("Enter the Category of vehicle:"))
            vehicle = Vehicle(vehicle_id, brand, model, year, category)
            add_vehicle(vehicle)

    elif d == 2:
        vehicle_id = str(input("Enter the vehicle id to be removed:"))
        remove_vehicle(vehicle_id)

    elif d == 3:
        vehicle_id = str(input("Enter the vehicle id to be searched:"))
        search_vehicle(vehicle_id)

    elif d == 4:
        list_vehicles(Rental_System)

    elif d == 5:
        categorize_vehicle()

    elif d == 6:
        exit(0)
    else:
        print("Invalid Choice")
