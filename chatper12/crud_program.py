import pickle
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():
    print('Welcome to your email list manager!')
    email_manager()


def email_manager():

    try:
        pickled_file = open('crud_dictionary.txt', 'rb')
        pickle.load(pickled_file)
    except (FileNotFoundError, IOError):
        print('File not found, please add a customer then quit to create the file.')

    customer_file = {}

    selection = 0

    while selection != QUIT:
        print('\n')
        selection = int(input('Enter your selection:' '\n\t1. Look up an email by name \n\t2. Add a new entry'
                              "\n\t3. Change a person\n\t4. Delete an entry\n\t5. Quit \nSelection: "))
        while selection < 1 or selection > 5:
            print('Please enter a valid choice.')
            email_manager()
        if selection == LOOK_UP:
            look_up(customer_file)
        if selection == ADD:
            add(customer_file)
        if selection == CHANGE:
            change(customer_file)
        if selection == DELETE:
            delete(customer_file)
        if selection == QUIT:
            save(customer_file)


def look_up(customer_file):
    customer_name = input('Enter a name: ')
    print(customer_file.get(customer_name, 'Name not found.'))


def add(customer_file):
    customer_name = input('Enter the name you want to add: ')
    customer_email = input('Enter the email you want to add: ')
    if customer_name not in customer_file:
        customer_file[customer_name] = customer_email
        print('Your new entry has been added to your email list manager.')
    else:
        print('Error adding name to email manager.')


def change(customer_file):
    customer_name = input('Enter the name you want to change: ')
    if customer_name in customer_file:
        confirm = input(f'The current email address for this user is {customer_name}, are you sure you want to change this? (y/n): ')
        if confirm == 'y' or confirm == 'Y':
            new_email = input('Please enter the new email address: ')
            customer_file[customer_name] = new_email
            print(f'Your email list manager has been updated for {customer_name}.')
        else:
            print('No changes made to your email list manager.')
    else:
        print('Name not found.')


def delete(customer_file):
    customer_name = input('Enter the name you want to delete: ')
    if customer_name in customer_file:
        confirm = input(f'The email address for {customer_name} is currently {customer_file[1]}, are you sure you want to delete this? (y/n): ')
        if confirm == 'y' or confirm == 'Y':
            print(f'{customer_name} has been removed from your email list manager.')
            del customer_file[customer_name]
        else:
            print('No changes made to your email list manager.')
    else:
        print('Name not found.')


def save(customer_file):
    print('The data in this file has been updated with your choices.')
    save_file = open('crud_dictionary.txt', 'wb')
    pickle.dump(customer_file, save_file)
    save_file.close()


main()
