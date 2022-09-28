"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""

# TODO 4.2 A condition controlled loop
print("=" * 10, "Section 4.2 condition controlled loop", "=" * 10)
# Write a while loop that will change the variable in num by subtracting 1,
# then print the variable. Keep looping until num = 0, ie. while num > 0:
num = 10
# write your code here, the variable needs to exist before you start the loop
while num > 0:
    print('The number is 10')
    int(input('What is the number minus 1? '))
    print('The number is 9')
    int(input('What is the number minus 1? '))
    print('The number is 8')
    int(input('What is the number minus 1? '))
    print('The number is 7')
    int(input('What is the number minus 1? '))
    print('The number is 6')
    int(input('What is the number minus 1? '))
    print('The number is 5')
    int(input('What is the number minus 1? '))
    print('The number is 4')
    int(input('What is the number minus 1? '))
    print('The number is 3')
    int(input('What is the number minus 1? '))
    print('The number is 2')
    int(input('What is the number minus 1? '))
    print('The number is 1')
    num = int(input('What is the number minus 1? '))
    print('The number is 0')

# TODO 4.3 the For Loop
print("=" * 10, "Section 4.3 for loop", "=" * 10)
# Use a for-in loop with a list of the days of the week,
# print each day of the week
# SEE PROGRAM 4-6 FOR AN EXAMPLE
for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
    print(day)

# TODO 4.3 using range() in a for loop
print("=" * 10, "Section 4.3 using range() in a for loop", "=" * 10)
# use the range function to print the numbers from 1 to 10
for num in range(1, 11):
    print(num)

# TODO 4.3 using range() with a step value
print("=" * 10, "Section 4.3 using range() with a step value", "=" * 10)
# use the range function to print the odd numbers from 5 to 15
for num in range(5, 16, 2):
    print(num)

# TODO 4.3 using the control variable in a for loop
print("=" * 10, "Section 4.3 using the control variable in a for loop", "=" * 10)
# NOTE: The terms "Control Variable" and "Target Variable" both refer to the for loop variable
# 1) Write a for loop using range(1,10) and a control variable called number
# 2) Inside the loop, print the result of number times 7
print('Number\t\tNumber * 7')
print('______________________________')
for number in range(1, 10):
    times_7 = (number*7)
    print(f'{number}\t\t\t{times_7}')

# TODO 4.4 a running total
print("=" * 10, "Section 4.4 running total", "=" * 10)
# Use a loop to have the user enter 5 numbers, provide a total at the end
# You will need to initialize your accumulator before entering the loop
# You can assume valid integers are entered
MAX = 5
total = 0.0
print(f'This program sum of {MAX} numbers you will enter.')
for counter in range(MAX):
    number = int(input('Enter a number:  '))
    total = total + number
print(f'The total is {total}.')

# TODO 4.5 Sentinel Value
print("=" * 10, "Section 4.5 sentinel value", "=" * 10)
# Create a variable to store a total amount. Initialize it to zero.
# Initialize another variable to store a count of the numbers entered.
# Use a while loop to have the user enter test scores until
# a sentinel value of -1 is entered.
# After the loop, display the total, the count, and the average (total / count)
total = 0
count = 0
print("Enter the test score or enter -1 to end.")
number = float(input('Test score: '))
while number != -1:
    total += number
    count += 1
    print('Enter the next test score or -1 to end.')
    number = float(input('Test score: '))
print(f'The total of the test scores is %{total:.2f}.')
print(f'The total number of test scores entered is {count:.2f}.')
if count > 0:
    average = total / count
print(f'The average test score is %{average:.2f}.')

# TODO 4.6 validating data
print("=" * 10, "Section 4.6 data validation loop", "=" * 10)
# Ask the user to enter a number between 1 and 10.
# Use a while loop to force the user to repeat the
# input until the user enters a valid number. Test with
# both valid and invalid data.

number = int(input('Enter a number between 1 and 10:  '))
while number < 1 or number > 10:
    number = int(input('ERROR: You must enter a number between 1 and 10: '))


