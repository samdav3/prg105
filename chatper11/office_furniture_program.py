from office_furniture_classes import OfficeFurniture
from office_furniture_classes import Desk


def main():
    desk = Desk('Desk', 'Wood', '48 in', '24 in', '36 in', '$500', 'Left', '3')
    chair = OfficeFurniture('Chair', 'Wood', '24 in', '24 in', '48 in', '$100')
    print('Something in Inventory:')
    print(desk.__str__())

    print('Something in Inventory:')
    print(chair.__str__())


main()
