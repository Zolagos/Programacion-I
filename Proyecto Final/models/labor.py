from models.item import Item

class Labor(Item):

    # Constructor
    def __init__(self, new_name, new_price, new_description, new_estimated_hours):
        super().__init__(new_name, new_price, new_description)
        self.set_estimated_hours(new_estimated_hours)

    # Getter for estimated hours
    def get_estimated_hours(self):
        return self._estimated_hours
    
    # Setter for estimated hours
    def set_estimated_hours(self, new_estimated_hours):
        if (new_estimated_hours > 0):
            self.estimateed_hours = new_estimated_hours
        else:
            print("The estimated hours can not be negative")
    
    # Show info
    def show_info(self):
        return (f"Labor: {self.get_name()}, Price per hour: {self.get_price()}, Estimated Hours: {self.get_estimated_hours()}")
    
    