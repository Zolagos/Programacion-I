class WorkOrder:

    # Constructor
    def __init__(self, rider, motorcycle_model):
        self._rider = rider
        self._motorcycle_model = motorcycle_model
        self._items = []

    # Add an item into items
    def add_item(self, item):
        self._items.append(item)

    # Calculate total's sale
    def calculate_total(self):
        total = 0
        for item in self._items:
            if hasattr(item, 'get_estimated_hours'):
                total = (total + (item.get_price() * item.get_estimated_hours()))
            else:
                total += item.get_price()
        return total
    
    def show_info(self):
        print("--------------------------------------------------")
        print(f"WORK ORDER FOR: {self._rider.get_name()} {self._rider.get_last_name()}")
        print(f"MOTORCYCLE: {self._motorcycle_model}")
        print("\nItems and Labor: ")
        
        for item in self._items:
            print(f"- {item.show_info()}")
        
        print(f"\nTOTAL COST: ${self.calculate_total()}")
        print("--------------------------------------------------")
        
