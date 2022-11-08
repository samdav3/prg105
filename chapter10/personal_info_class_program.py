

class Contact:

    def __init__(self, name_in, age_in, address_in, phone_in):
        self.__name = name_in
        self.__age = age_in
        self.__address = address_in
        self.__phone = phone_in

    def set_name(self, name_in):
        self.__name = name_in

    def set_age(self, age_in):
        self.__age = age_in

    def set_address(self, address_in):
        self.__address = address_in

    def set_phone(self, phone_in):
        self.__phone = phone_in

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def __str__(self):
        return f'{self.__name}' + '\n' + f'{self.__age}' + '\n' + f'{self.__address}' +\
               '\n' + f'{self.__phone}' + '\n'


def main():
    p1 = Contact('Sam', '28', '1 Hickory Rd', '815-690-3247')
    p2 = Contact('Katie', '28', '1 Hickory Rd', '630-363-1572')
    p3 = Contact('Kelsey', '32', '1093 Plum Tree Dr', '815-690-1782')
    print(p1)
    print(p2)
    print(p3)


main()
