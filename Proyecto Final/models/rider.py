from models.user import User

class Rider(User):
    
    # Constructor
    def __init__(self, new_name, new_last_name, new_phone, new_license_category):
        super().__init__(new_name, new_last_name, new_phone)
        self.set_license_categoty(new_license_category)

    # Getter for license_category
    def get_license_category(self):
        return self._license_categoty
    
    # Setter for license_category
    def set_license_category(self, new_license_category):
        if (new_license_category != 0):
            self._license_categoty = new_license_category
        else:
            print("The License Category can not be empty")

    # Get role
    def get_role(self):
        return ("Rider")
    
    def show_info(self):
        return (f"Name: {self.get_name()}, Last Name: {self.get_last_name()}, Phone: {self.get_phone()}, Role: {self.get_role()}, License: {self.get_license_category()}")
    
    