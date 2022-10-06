

def main():
    print('This program will find the area of a shape for you.')
    print('1. Rectangle')
    print('2. Triangle')
    print('3. Square')
    print('4. Circle')
    print('5. Quit')
    selection = int(input('Please enter the number of your selection: '))
    area = validate(selection)
    while selection == 1:
        rectangle(area)
        selection = (input('Please enter the number of your selection: '))
    while selection == 2:
        triangle(area)
        selection = (input('Please enter the number of your selection: '))
    while selection == 3:
        square(area)
        int(input('Please enter the number of your selection: '))
    while selection == 4:
        circle(area)
        int(input('Please enter the number of your selection: '))
    while selection == 5:
        end()


def validate(selection):
    while selection <= 0 or selection > 5:
        print('That is not a valid number')
        selection = input(int('Please enter the number of your selection: '))
    return selection


def rectangle(area):
    rec_width = int(input('Enter the width of the rectangle in cm: '))
    rec_height = int(input('Enter the height of the rectangle in cm: '))
    rectangle_area = (rec_width * rec_height)
    print(f'The area of the rectangle is {rectangle_area:.2f} square cm.')
    return area


def triangle(area):
    tri_base = int(input('Enter the base of the triangle in cm: '))
    tri_height = int(input('Enter the height of the triangle in cm: '))
    tri_area = (.5 * tri_base) * tri_height
    print(f'The are of the triangle is {tri_area:.2f} square cm.')
    return area


def square(area):
    sq_width = int(input('Enter the width of the square in cm: '))
    sq_height = int(input('Enter the height of the square in cm: '))
    square_area = sq_width * sq_height
    print(f'The area of the square is {square_area:.2f} square cm.')
    return area


def circle(area):
    cir_radius = int(input('Enter the radius of the circle in cm: '))
    circle_area = (3.14 * (cir_radius * cir_radius))
    print(f'The area of the circle is {circle_area:.2f} square cm.')
    return area


def end():
    print('That is not a valid number.')
    print('Goodbye')
    return quit()


main()
