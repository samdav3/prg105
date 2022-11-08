

class Contact:

    def __init__(self, name, age, address, phone):
        self.name = str(name)
        self.age = int(age)
        self.address = str(address)
        self.phone = str(phone)

    def set_name(self, __name):
        self.name = 'Sam Davenport'
        self.name = 'Katie Callahan'
        self.name = 'Kelsey Davenport'

    def set_age(self, __age):
        self.age = '28'
        self.age = '28'
        self.age = '32'

    def set_address(self, __address):
        self.address = '1 Hickory Rd'
        self.address = '1 Hickory Rd'
        self.address = '1093 Plum Tree Dr'

    def set_phone(self, __phone):
        self.phone = '815-690-3247'
        self.phone = '630-363-1572'
        self.phone = '815-690-1782'

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone


def main():
    contact = Contact()
    print(contact.get_name())
    print(contact.get_age())
    print(contact.get_address())
    print(contact.get_phone())


main()
