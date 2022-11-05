print('You will be entering the number of steps taken for each day in a week.')
days = {'Monday': '', 'Tuesday': '', 'Wednesday': '', 'Thursday': '', 'Friday': '', 'Saturday': '', 'Sunday': ''}
count = 0
total = 0
average = 0
for key in days:
    steps = int(input(f'Please enter the number of steps taken on {key}: '))
    days[key] = steps
    count += 1
    total += steps
    average = total / count
    for value in days:
        most = days.get(max(value))
        least = days.get(min(value))

print(f'You walked a total of {total} steps during the week.')
print(f'That was an average of {average} steps.')
print(f'The maximum steps you took were {most} on: {key}.')
print(f'The minimum steps you took were {least} on: {key}.')
print(days)
