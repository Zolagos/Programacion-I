from models.spare_part import SparePart
from models.labor import Labor
from models.rider import Rider
from models.mechanic import Mechanic
from models.work_order import WorkOrder

catalog = []
users = []
work_orders = []

def show_menu():
    print("\n=== MOTORCYCLE WORKSHOP ===")
    print("1. Add Spare Part")
    print("2. Add Labor Service")
    print("3. Add Rider (Client)")
    print("4. Add Mechanic")
    print("5. Show Catalog")
    print("6. Show Users")
    print("7. Create Work Order")
    print("8. Exit")

def add_spare_part():
    print("\n--- Add Spare Part ---")
    name = input("Enter part name (e.g., Shaft Helmet visor, Brake pads): ")
    price = float(input("Enter part price: "))
    description = input("Enter description: ")
    stock = int(input("Enter stock: "))

    part = SparePart(name, price, description, stock)
    catalog.append(part)
    print("Spare part added successfully.")

def add_labor():
    print("\n--- Add Labor Service ---")
    name = input("Enter service name (e.g., Oil change, General maintenance): ")
    price = float(input("Enter price per hour: "))
    description = input("Enter description: ")
    hours = float(input("Enter estimated hours: "))

    labor = Labor(name, price, description, hours)
    catalog.append(labor)
    print("Labor service added successfully.")

def add_rider():
    print("\n--- Add Rider ---")
    name = input("Enter rider name: ")
    last_name = input("Enter rider last name: ")
    phone = input("Enter rider phone: ")
    license_cat = input("Enter license category (e.g., A2): ")

    rider = Rider(name, last_name, phone, license_cat)
    users.append(rider)
    print("Rider added successfully.")

def add_mechanic():
    print("\n--- Add Mechanic ---")
    name = input("Enter mechanic name: ")
    last_name = input("Enter mechanic last name: ")
    phone = input("Enter mechanic phone: ")
    specialty = input("Enter specialty: ")

    mechanic = Mechanic(name, last_name, phone, specialty)
    users.append(mechanic)
    print("Mechanic added successfully.")

def show_catalog():
    print("\n--- Catalog ---")
    for item in catalog:
        print(item.show_info())

def show_users():
    print("\n--- Users ---")
    for user in users:
        print(user.show_info())

def create_work_order():
    print("\n--- Create Work Order ---")
    rider_phone = input("Enter rider phone number to search: ")

    rider_found = None
    for user in users:
        if user.get_phone() == rider_phone and user.get_role() == "Rider":
            rider_found = user
            break
    
    if rider_found is None:
        print("Rider not found in system.")
        return
    
    moto_model = input("Enter motorcycle model (e.g., TVS Raider 125): ")
    order = WorkOrder(rider_found, moto_model)

    add_item = "yes"
    while add_item.lower() == "yes":
        item_name = input("Enter spare part or service name to add: ")
        
        item_found = None
        for item in catalog:
            if item.get_name() == item_name:
                item_found = item
                break

        if item_found is None:
            print("Item/Service not found in catalog.")
        else: 
            order.add_item(item_found)
            print("Added to work order successfully.")

        add_item = input("Do you want to add another item? (yes/no): ")

    work_orders.append(order)
    print("\nWork order created successfully!")
    order.show_info()

option = 0

while option != 8:
    show_menu()
    try:
        option = int(input("\nEnter an option (1-8): "))

        if option == 1:
            add_spare_part()
        elif option == 2:
            add_labor()
        elif option == 3:
            add_rider()
        elif option == 4:
            add_mechanic()
        elif option == 5:
            show_catalog()
        elif option == 6:
            show_users()
        elif option == 7:
            create_work_order()
        elif option == 8:
            print("\nClosing Workshop System. Ride safe!")
        else:
            print("\nInvalid option.")
    except ValueError:
        print("\nPlease enter a valid number.")