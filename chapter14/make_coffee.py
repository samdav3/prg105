import sqlite3


def main():
    coffee_db = None
    try:
        coffee_db = sqlite3.connect('coffee.db')
        coffee_cursor = coffee_db.cursor()
        table_structure = coffee_cursor.execute('''CREATE TABLE IF NOT EXISTS Coffee
                                        (ProdID INTEGER PRIMARY KEY NOT NULL,
                                        Product TEXT, 
                                        Category TEXT, 
                                        Supplier TEXT)''')
        coffee_cursor.execute(table_structure)
        coffee_db.commit()

        try:
            count = 0
            coffee_file = open('coffeehouse_supplies.csv', 'rb')
            for line in coffee_file:
                coffee_data = line.strip().split(',')
                coffee_cursor.execute('''INSERT INTO Coffee (ProdID, Product, Category, Supplier)
                                VALUES (?, ?, ?, ?)''', (coffee_data[0], coffee_data[1], coffee_data[2], coffee_data[3]))
                count += 1
                print(f'{count} records added')
            coffee_db.close()
            coffee_db.commit()


        except IndexError:
            print('IndexError: File data type is incompatible.')

        except IOError:
            print('IOError: Unable to add data to coffeehouse_supplies.csv.')

        except sqlite3.Error:
            print('%SQL Error encountered.')

    except sqlite3.Error:
        print('%SQL Error encountered.')

    finally:
        if coffee_db is not None:
            coffee_db.close()


main()
