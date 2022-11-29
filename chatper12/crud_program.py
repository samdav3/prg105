import pickle
LOOK_UP = '1'
ADD = '2'
CHANGE = '3'
DELETE = '4'
STOP = '5'


def main():
    print('Welcome to your email list manager!')
    email_manager()


def email_manager():

    print('\n')
    selection = input('Enter your selection:' '\n\t1. Look up an email by name \n\t2. Add a new entry'
                      "\n\t3. Change a person\n\t4. Delete an entry\n\t5. Quit \nSelection: ")

    customer_file = {}
    open('crud_dictionary.txt', 'r')

    while selection != STOP:
        if selection == LOOK_UP:
            look_up(customer_file)
        if selection == ADD:
            add(customer_file)
        if selection == CHANGE:
            change(customer_file)
        if selection == DELETE:
            delete(customer_file)
        if selection == STOP:
            quit(customer_file)


def look_up(customer_file):
    customer_name = input('Enter a name: ')
    if customer_name in customer_file:
        print(customer_file.get(customer_name))
        email_manager()
    else:
        print('Name not found.')
        email_manager()


def add(customer_file):
    customer_name = input('Enter the name you want to add: ')
    customer_email = input('Enter the email you want to add: ')
    customer_file[customer_name] = customer_email
    dump(customer_file)
    print('Your new entry has been added to your email list manager.')
    email_manager()


def change(customer_file):
    customer_name = input('Enter the name you want to change: ')
    if customer_name in customer_file:
        confirm = input(f'The current email address for this user is {customer_file[1]}, are you sure you want to change this? (y/n): ')
        if confirm == 'y' or confirm == 'Y':
            new_email = input('Please enter the new email address: ')
            customer_file[customer_name] = new_email
            dump(customer_file)
            print(f'Your email list manager has been updated for {customer_name}.')
            email_manager()
        else:
            print('No changes made to your email list manager.')
            email_manager()
    else:
        print('Name not found.')
        email_manager()


def delete(customer_file):
    customer_name = input('Enter the name you want to delete: ')
    if customer_name in customer_file:
        confirm = input(f'The email address for {customer_name} is currently {customer_file[1]}, are you sure you want to delete this? (y/n): ')
        if confirm == 'y' or confirm == 'Y':
            print(f'{customer_name} has been removed from your email list manager.')
            del customer_file[customer_name]
            dump(customer_file)
            email_manager()
        else:
            print('No changes made to your email list manager.')
            email_manager()
    else:
        print('Name not found.')
        email_manager()


def stop(customer_file):
    quit()


def dump(pickled_file):
    customer_file = {}
    pickled_file = open('crud_dictionary.txt', 'wb')
    pickle.dump(customer_file, pickled_file)
    pickled_file.close()


main()
