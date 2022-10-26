"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""

# TODO 8.1 Basic string Operation
print("=" * 10, "Section 8.1 string operations", "=" * 10)
# 1) Print all the characters from the name variable by accessing one character at a time
name = "John Jacob Jingleheimer Schmidt"
for ch in name:
    print(ch)
# 2) Use the index value to access and print the capital s in Schmidt from the variable name
print(name[24])
# 3) Use a negative index value to print the letters from the last name "Schmidt" in name
print(name[-7], name[-6], name[-5], name[-4], name[-3], name[-2], name[-1])

# TODO 8.2 String slicing
print("=" * 10, "Section 8.2 string slicing", "=" * 10)
# 1) Use string slicing to assign the middle name "Jacob" from name to the variable middle, replace the ""
# 2) Print middle
middle = name[5:11]
print(middle)


# TODO 8.3 Testing, Searching, and manipulating strings
print("=" * 10, "Section 8.3 manipulating strings", "=" * 10)
# 1) Test to see if the string "Jacob" is in name, print the result
if 'Jacob' in name:
    print('Jacob was found in string.')
else:
    print('Jacob was not found in string.')
# 2) Test to see if the string "Michael" is in name, print the result
if 'Michael' not in name:
    print('Micheal was not found in string.')
else:
    print('Micheal was found in string.')
# 3) Test to see if name contains only digits, print the result
#    Hint: Use the built-in string testing methods
if name.isdigit():
    print(f'{name} contains only digits.')
else:
    print(f'{name} contains characters other than digits.')
# 4) Test to see if name is lowercase, print the result
if name.islower():
    print(f'{name} is lowercase.')
else:
    print(f'{name} is not lowercase.')
# 5) Search for "J" in name, replace with "j" (lower case), print the result
#    Note: You can assign this to a variable first, or just print
low_name = name.replace('J', 'j')
print(low_name)

# 6) Split the string name into the variable name_list below (replace the ""), print the result
name_list = name.split()
print(name_list)
