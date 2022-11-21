class OfficeFurniture:
    def __init__(self, category, material, length, width, height, price):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    def set_category(self, category):
        self.__category = category

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price

    def get_category(self):
        return self.__category

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    def __str__(self):
        inventory_item = 'Category: ' + self.get_category() + '  ' + 'Material: ' + self.get_material() + '  ' + 'Length: ' + self.get_length() + '  ' + 'Width: ' + self.get_width() + '  ' + 'Height: ' + self.get_height() + '  ' + 'Price: ' + self.get_price()
        return inventory_item


class Desk(OfficeFurniture):
    def __init__(self, category, material, length, width, height, price, location_of_drawers, number_of_drawers):
        OfficeFurniture.__init__(self, category, material, length, width, height, price)
        self.__location_of_drawers = location_of_drawers
        self.__number_of_drawers = number_of_drawers

    def set_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers

    def set_number_of_drawers(self, number_of_drawers):
        self.__number_of_drawers = number_of_drawers

    def get_location_of_drawers(self):
        return self.__location_of_drawers

    def get_number_of_drawers(self):
        return self.__number_of_drawers

    def __str__(self):
        inventory_item = 'Category: ' + self.get_category() + '  ' + 'Material: ' + self.get_material() + '  ' + 'Length: ' + self.get_length() + '  ' + 'Width: ' + self.get_width() + '  ' + 'Height: ' + self.get_height() + '  ' + 'Price: ' + self.get_price() + '  ' + 'Location of Drawers: ' + self.get_location_of_drawers() + '  ' + 'Number of Drawers: ' + self.get_number_of_drawers()
        return inventory_item
