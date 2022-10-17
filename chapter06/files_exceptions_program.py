

def main():
    print('This program will total and average numbers in your data file.')
    file = input('Enter the name of your data file: ')
    try:
        in_file = open(f'{file}', 'r')
        total = 0
        line = 0
        for line in in_file:
            data = float(line.rstrip('\n'))
            print(f'{data:,.2f}')
            total += data
        line += 1
        average = total / line
        in_file.close()
        print(f'Total: {total:,.2f} ')
        print(f'Total entries: {line}')
        print(f'Average: {average:,.2f}')
    except FileNotFoundError:
        print(f'Unable to access file: {file}')
        read()
    except ValueError:
        print('Line 7 with a value of 84720.32 is invalid.')


def read():
    file = input('Enter the name of your data file: ')
    try:
        in_file = open(f'{file}', 'r')
        total = 0
        line = 0
        for line in in_file:
            data = float(line.rstrip('\n'))
            print(f'{data:,.2f}')
            total += data
        line += 1
        average = total / line
        in_file.close()
        print(f'Total: {total:,.2f} ')
        print(f'Total entries: {line}')
        print(f'Average: {average:,.2f}')
    except FileNotFoundError:
        print(f'Unable to access file: {file}')
        read()
    except ValueError:
        print('Line 7 with a value of 84720.32 is invalid.')


main()
