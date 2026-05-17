from models.item import Item

class SparePart (Item):

    # Constructor
    def __init__(self, new_name, new_price, new_description, new_stock):
        super().__init__(new_name, new_price, new_description)
        self.set_stock(new_stock)

    # Getter for stock
    def get_stock(self):
        return self._stock
    
    # Setter for stock
    def set_stock(self, new_stock):
        if (new_stock >= 0):
            self._stock = new_stock
        else:
            print("The stock can not be negative")

    # Show info
    def show_info(self):
        return (f"Product: {self.get_name()}, price: {self.get_price()}, description: {self.description}, stock: {self.get_stock()}")
    
     # Calculate total
    def calculate_total(self):
        return self.get_price() *  self.get_stock() 