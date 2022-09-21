"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""

# TODO 3.1 Relational Operators
print("=" * 10, "Section 3.1 relational operators", "=" * 10)
# 1) Write a boolean expression using the variables below and a
#    greater-than sign that will evaluate to true.
#    Include the expression in a print statement to display the result.
# 2) Write a boolean expression using the variables below that
#    compares two of the variables to see if they are equal.
#    Include the expression in a print statement to display the result.
# 3) Write a boolean expression using the variables below to compare
#    two of the variables to see if they are NOT equal.
#    Include the expression in a print statement to display the result.
# 4) Write a boolean expression using the variables below that uses
#    the less than or equal to operator.
#    Include the expression in a print statement to display the result.

# variables
a = 6
b = 8
c = 5

# 1 sample answer
print(a > 3)
print(a < b)
# 2
print(c == a)
# 3
print(b != c)
# 4
print(a <= b)
# TODO 3.2 the if else statement
print("=" * 10, "Section 3.2 if-else", "=" * 10)
# Add code below to determine if age is greater than or equal to 18
# Depending on the answer, display the appropriate statement:
#    "You are old enough to vote" or "You are not old enough to vote"
# Use the if-else structure (remember to use proper indentation)
age = int(input("How old are you? "))
if age < 18:
    print('You are not old enough to vote')
else:
    print('You are old enough to vote')

# TODO 3.3 comparing strings
print("=" * 10, "Section 3.3 comparing strings", "=" * 10)
# Complete the code below so that if the user input matches the password
# it will display "that is correct"; otherwise display "that is not correct"
password = "narwhals"
user_password = input("Please enter the password:  ")
if user_password == password:
    print("that is correct")
else:
    print("that is not correct")

# TODO 3.4 if - elif - else
print("=" * 10, "Section 3.4 if-elif-else", "=" * 10)
# Complete the code to accept a number between 1 and 5 from the user
# and display a roman numeral for that number. If the number entered is
# not between 1 and 5, have the else statement display "That is not a valid number"
number = int(input("Please enter a number between 1 and 5: "))
if number >= 1:
    if number <= 5:
        print("this number was accepted")
    else:
        print("this number was not accepted")
else:
    print("this number was not accepted")

# TODO 3.4 a series of conditions
print("=" * 10, "Section 3.4 multiple conditions", "=" * 10)
# Buffet prices are based on the persons age. If the person is a senior
# citizen (62 or over), the charge is $9.89. If the person is age 12-
# 61, the charge is $12.89. If it is a child of under age 3, they eat
# for free. If the child is between 3 and 11 they are charged $0.99 for
# each year of age. Complete the partial code below to determine cost.
# HINT: Organize the options in order according to age to simplify the logic.
# SEE PROGRAM 3-6 FOR AN EXAMPLE USING GRADES -- the first example shows a full
# traditional ELSE IF structure, there is also a simpler example using IF-ELIF-ELSE.

customer_age = int(input("How old is the customer?   "))
# initializing cost, assign the correct price to this variable
# Write the code here to determine the correct cost based on age
if customer_age <= 3:
    cost = 0
elif customer_age >= 3:
    if customer_age <= 11:
        cost = (0.99 * customer_age)
    elif customer_age >= 12:
        if customer_age <= 61:
            cost = 12.89
        elif customer_age >= 62:
            cost = 9.89

# Output, correctly formatted -- leave this code to display the result
print("Your cost for a customer who is", customer_age, "years old ", end="")
print(f"will be ${cost: ,.2f}")

# TODO 3.5 Logical Operators
print("=" * 10, "Section 3.5 logical operators", "=" * 10)
# Using the variables below, create compound Boolean expressions using logical operators
# Example: d > f or e == f
# 1) write a print statement using the and operator that will evaluate to true
# 2) write a print statement using the or operator that will evaluate to true
# 3) write a print statement using the not operator that will evaluate to true
d = 10
e = 10
f = 12
if d==e and d<f:
    print('True')
if d>f or f>d:
    print('True')
if not (d>f):
    print('True')

# TODO 3.6 Boolean variables
print("=" * 10, "Section 3.6 boolean variables", "=" * 10)
# You are programming a baby doll. If the baby doll is tired, it will close its eyes
# if it is hungry, it will cry. Write code to print  "Eyes open" or "Eyes closed" depending
# on the tired value. Then print "Crying" or "quiet" depending on the hungry variable
tired = True
hungry = False
if tired:
    print('Eyes closed')
else:
    print('Eyes open')
if hungry:
    print('Crying')
else:
    print('Quiet')
