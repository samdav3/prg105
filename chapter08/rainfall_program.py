

def main():
    data = open('rainfall-totals.txt', 'r')
    total = 0
    count = 0
    for line in data:
        line = line.rstrip('\n')
        rain = line.split()
        rain_month = rain[0]
        rain_amount = rain[1].split(".")

        if rain_amount[0].isdigit() and rain_amount[1].isdigit():
            amount = float(rain_amount[0] + '.' + rain_amount[1])
            total += float(amount)
            count += 1
        else:
            print(f"Bad numeric data found for entry: {rain_month}" + " " + f'{float(rain_amount[0])}')

    average = total / count
    data.close()
    print(f'{count} good values were found.')
    print(f'The total was {total:.2f}')
    print(f'The average was {average:.2f}')


main()
