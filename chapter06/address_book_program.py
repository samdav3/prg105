

def main():
    count = 0
    add_book = open('add_book.txt', 'w')
    entry = int(input('How many people do you want to add to the file? '))
    for count in range(count, entry):
        name = input('What is the name of the person? ')
        phone = input('What is their phone number? ')
        email = input('What is their email address? ')
        add_book.write(f'{name, phone, email}\n')
    add_book.close()


main()
