import sqlite3


def main():
    pet_owner_db = None
    try:
        pet_owner_db = sqlite3.connect('pets.db')
        cursor = pet_owner_db.cursor()
        owners_table = '''CREATE TABLE IF NOT EXISTS Owners 
                        (OwnerID INTEGER PRIMARY KEY NOT NULL, OwnerName TEXT, OwnerPhone TEXT)'''
        pets_table = '''CREATE TABLE IF NOT EXISTS Pets 
                    (PetID INTEGER PRIMARY KEY NOT NULL, PetName TEXT, PetType TEXT, PetBreed TEXT, 
                    OwnerID INTEGER, FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID)'''
        cursor.execute(owners_table)
        cursor.execute(pets_table)
        pet_owner_db.commit()
        try:
            owners = open('Owners.txt', 'r')
            pets = open('Pets.txt', 'r')
            for line in owners:
                owner_data = line.strip().split(',')
                cursor.execute('''INSERT INTO Owners (OwnerName, OwnerPhone)
                                VALUES (?, ?)''', (owner_data[1], owner_data[2]))
                pet_owner_db.commit()
                for line2 in pets:
                    pet_data = line2.strip().split(',')
                    cursor.execute('''INSERT INTO Pets (PetName, PetType, PetBreed, OwnerID)
                                    VALUES (?, ?, ?)''', (pet_data[0], pet_data[1], pet_data[2]))
                    pet_owner_db.close()
                    pet_owner_db.commit()
                    print(f'{owner_data[1]}' + "   " + f"{owner_data[2]}" + "\n" + '\t' + f'{pet_data[0]}' + "is a" + f'{pet_data[2]}' + "," + f'{pet_data[1]}')

        except IndexError:
            print('IndexError: File data type is incompatible.')

        except IOError:
            print('IOError: Unable to add data to coffeehouse_supplies.csv.')

        except sqlite3.Error:
            print('%SQL Error encountered.')

    except sqlite3.Error:
        print('%SQL Error encountered.')

    finally:
        if pet_owner_db is not None:
            pet_owner_db.close()


main()
