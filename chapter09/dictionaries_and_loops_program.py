print('You will be entering the number of steps taken for each day in a week.')
days = {'Monday': '', 'Tuesday': '', 'Wednesday': '', 'Thursday': '', 'Friday': '', 'Saturday': '', 'Sunday': ''}
count = 0
total = 0
average = 0
maximum = 0
minimum = 2000000
for key in days:
    steps = int(input(f'Please enter the number of steps taken on {key}: '))
    days[key] = steps
    count += 1
    total += steps
    average = total / count
    if steps > maximum:
        maximum = steps
    if steps < minimum:
        minimum = steps

print(f'You walked a total of {total} steps during the week.')
print(f'That was an average of {average} steps.')
print(f'The maximum steps you took were {maximum} on: ')
for key in days:
    if days[key] == maximum:
        print(key)
print(f'The minimum steps you took were {minimum} on: ')
for key in days:
    if days[key] == minimum:
        print(key)
