

def main():
    number = int(input('Enter a whole number between 20 and 200: '))
    while number > 100 or number < 20:
        print('That is not a valid number.')
        number = int(input('Enter a whole number between 20 and 200: '))
    good_number = validate(number)
    div_2(number)
    div_3(number)
    div_5(number)


def validate(user_number):
    valid_number = user_number
    return valid_number


def div_2(user_number):
    quotient = (user_number / 2)
    if quotient == int(quotient):
        print(f'{user_number} is divisible by 2.')
    elif quotient != int(quotient):
        print(f'{user_number} is not divisible by 2.')
    return user_number


def div_3(user_number):
    quotient = (user_number / 3)
    if quotient == int(quotient):
        print(f'{user_number} is divisible by 3.')
    elif quotient != int(quotient):
        print(f'{user_number} is not divisible by 3.')
    return user_number


def div_5(user_number):
    quotient = (user_number / 5)
    if quotient == int(quotient):
        print(f'{user_number} is divisible by 5.')
    elif quotient != int(quotient):
        print(f'{user_number} is not divisible by 5.')
    return user_number


main()
