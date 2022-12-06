import sqlite3


def main():
    coffee_db = None
    try:
        coffee_db = sqlite3.connect('coffee.db')
        coffee_cursor = coffee_db.cursor()
        coffee_cursor.execute('''SELECT Category FROM Coffee''')
        category_list = coffee_cursor.fetchall()
        unique_categories = []
        for category in category_list:
            if category[0] not in unique_categories:
                unique_categories.append(category[0])

        print('Category\t\t\tProduct\t\t\tSupplier')

        unique_categories.sort()
        for category in unique_categories:
            print(category)
            coffee_cursor.execute('''SELECT * FROM Coffee WHERE Category == ?''', (category,))
            product_list = coffee_cursor.fetchall()
            for product in product_list:
                print(f'{product[1]:20} {product[3]}')

    except sqlite3.Error:
        print('$SQL Error Encountered.')
    finally:
        if coffee_db is not None:
            coffee_db.close()

            
main()
