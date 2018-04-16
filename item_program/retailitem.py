class RetailItem:

   # The __init__ method initialiazes the attributes.

    def __init__(self, item_descr, units_inven, price):
        self.__item_descr = item_descr
        self.__units_inven = units_inven
        self.__price = price

        # The set_item_descr method accepts an argument for the
        # retail's item description.

    def set_item_descr(self, item_descr):
        self.__item_descr = item_descr

        # The set units_inven method accepts an argument for the
        # retail's amount of units in inventory.
    def set_units_inven(self, units_inven):
        self.__units_inven = units_inven

        # The set price method accepts an argument for the retail's
        # unit price.
    def set_price(self, price):
        self.__price = price

        # The get_item_descr method returns the item description.
    def get_item_descr(self):
        return self.__item_descr

        # The get_units_inven method returns the retail's
        # amount of units in inventory.
    def get_units_inven(self):
        return self.__units_inven

        # The get_price method returns the retail's unit price.
    def get_price(self):
        return self.__price
    
