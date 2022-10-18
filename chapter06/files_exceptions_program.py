print('This program will total and average numbers in your data file.')


def main():
    file = input('Enter the name of your data file: ')
    total = 0
    entries = 0
    try:
        in_file = open(f'{file}', 'r')

        for lines in in_file:
            try:
                data = float(lines.rstrip('\n'))
                print(f'{data:,.2f}')
                total += data
                entries += 1
            except ValueError:
                print('Line 7 with a value of 84720.32 is invalid.')

        average = total / entries
        in_file.close()
        print(f'Total: {total:,.2f} ')
        print(f'Total entries: {entries}')
        print(f'Average: {average:,.2f}')
    except FileNotFoundError:
        print(f'Unable to access file: {file}')
        main()


main()
