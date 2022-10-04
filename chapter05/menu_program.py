print('Select one of the menu options below to find out more...')
print('A. Cheese pizza slice')
print('B. Cheeseburger')
print('C. Cesar Salad')
print('D. Steak')
print('E. Chicken')


def main():
    letter = input('Please enter the letter of your choice: ')
    pick = choice(letter)
    print(f'{pick}')


def choice(user_letter):
    if user_letter == 'a' or user_letter == 'A':
        print('Cheese pizza slice served with a side salad, your choice of dressing.')
    elif user_letter == 'b' or user_letter == 'B':
        print('Cheeseburger with your choice of cheese served with french fries.')
    elif user_letter == 'c' or user_letter == 'C':
        print('Cesar Salad served with or without chicken and a side of bread.')
    elif user_letter == 'd' or user_letter == 'D':
        print('Ribeye steak served with mashed potatoes and your choice of vegetable.')
    elif user_letter == 'e' or user_letter == 'E':
        print('Parmesan crusted chicken breast served with mashed potatoes and your choice of vegetable.')
    user_choice = user_letter
    return user_choice


main()
