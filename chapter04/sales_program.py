# Variables
total = 0.0
for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
    sales = float(input(f'What were the total sales for {day}: '))
    total += sales
print(f'The total sales for the week was: ${total:,.2f}')
average = total / 7
print(f'The average sales per day was: ${average:,.2f}')

