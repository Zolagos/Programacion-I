class Item:

    # Constructor
    def __init__(self, new_name, new_price, new_description):
        self.set_name(new_name)
        self.set_price(new_price)
        self.description = new_description

    # Getter for name
    def get_name(self):
        return self._name
    
    # Setter for name
    def set_name(self, new_name):
        if (new_name != ""):
            self.name = new_name
        else:
            print("The name can not be empty")

    # Getter for price
    def get_price(self):
        return self._price
    
    # Setter for price
    def set_price(self, new_price):
        if (new_price > 0):
            self._price = new_price
        else:
            print("The price must be greater than 0")

    def get_description(self):
        return self._description
    
    def set_description(self, new_description):
        if new_description != "":
            self._description = new_description
        else:
            print("The description can not be empty")
            

    # Show info
    def show_info(self):
        return (f"Item: {self.get_name()}, price: {self.get_price()}, description: {self.description}")
