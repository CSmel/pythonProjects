# Employee class

class Employee:
    # Initialize the object.
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
        

    # Mutator for the __name attribute.
    def set_name(self, name):
        self.__name = name

    # Mutator for the __number attribute.
    def set_number(self, number):
        self.__number = number

    # Accessor for the __name attribute.
    def get_name(self):
        return self.__name

    # Accessor for the __number attribute.
    def get_number(self):
        return self.__number
    
# Customer class
class ProductionWorker(Employee):
    # Initialize the object.
    def __init__(self, name, number,
                 shift_number, pay_rate):
        # Call the superclass __init__ method.
        Employee.__init__(self, name, number)

        # Initialize the specialized attributes.
        self.__shift_number = shift_number
        self.__pay_rate = pay_rate

    # Mutator for the __shift_number attribute.
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    # Mutator for the __pay_rate attribute.
    def set_mailing_list(self, pay_rate):
        self.__pay_rate = pay_rate

    # Accessor for the __shift_number attribute.
    def get_shift_number(self):
        return self.__shift_number

    # Accessor for the __pay_rate attribute.
    def get_pay_rate(self):
        return self.__pay_rate
    
