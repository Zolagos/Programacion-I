class User:
    
    # Constructor
    def __init__(self, new_name, new_last_name, new_phone):
        self.set_name(new_name)
        self.set_last_name(new_last_name)
        self.set_email(new_phone)

    # Getter for name
    def get_name(self):
        return self._name
    
    # Setter for name
    def set_name(self, new_name):
        if (new_name != ""):
            self._name = new_name
        else:
            print("The Name can not be empty")

    # Getter for last_name
    def get_last_name(self):
        return self._last_name
    
    # Setter for last_name
    def set_last_name(self, new_last_name):
        if (new_last_name != ""):
            self._last_name = new_last_name
        else:
            print("The Last Name can not be empty")

    # Getter for phone
    def get_phone(self):
        return self._phone
    
    # Setter for phone
    def set_phone(self, new_phone):
        if (new_phone != ""):
            self._phone = new_phone
        else:
            print("The Phone can not be empty")

    # Getter for role
    def get_role(self):
        return ("User")

    # Show_info
    def show_info(self):
        return (f"Name: {self.get_name()}, Last Name: {self.get_last_name()}, Phone: {self.get_phone()}")
