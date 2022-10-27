

def main():
    file = open('rainfall-totals.txt', 'r')
    total = 0
    count = 0
    line = 0
    data = file.readline()
    data.rstrip('\n')
    month = ''
    amount = ''
    data = data.split()
    month += data[0]
    amount += data[1]
    print(month)
    print(amount)
    for data in amount:
        sep_amount = ''
        sep_amount = data.split()
        print(sep_amount)
        for lines in sep_amount:
            lines.strip('.')
            print(lines)
            if lines.isdigit():
                lines.join(sep_amount)
                print(sep_amount)
           # else:
                #print(f"Bad numeric data found for entry: {}")

    #print(f'{count} good values were found.')
    #print(f'The total was {total:.2f}')
    #print(f'The average was {average:.2f}')


main()
