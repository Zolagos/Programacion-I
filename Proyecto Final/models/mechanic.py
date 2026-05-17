from models.user import User

class Mechanic (User):

    # Constructor
    def __init__(self, new_name, new_last_name, new_phone, new_specialty):
        super().__init__(new_name, new_last_name, new_phone)
        self.set_specialty(new_specialty)

    # Getter for specealty
    def get_specealty(self):
        return self._specealty
    
    # Setter for specealty
    def set_specealty(self, new_specialty):
        if (new_specialty != ""):
            self._specelty = new_specialty
        else:
            print("The specialty can not be empty")

    # Get role
    def get_role(self):
        return ("Mechanic")
    
    # Show_info
    def show_info(self):
        return (f"Name: {self.get_name()}, Last Name: {self.get_last_name()}, Phone: {self.get_phone()}, Role: {self.get_role()}, Specialty: {self.get_specialty()}")
    

