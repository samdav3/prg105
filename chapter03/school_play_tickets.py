# Variables

print('1. Student $5.00')
print('2. Veteran $7.00')
print('3. Show Sponsor $2.00')
print('4. Retiree $4.00')
print('5. General Public $10.00')

category = int(input('Please enter the number of the category you fit for purchasing tickets:  '))
quantity = int(input('How many tickets would you like to purchase?  '))
original_price = str(print(f"Cost before any discounts were applied: ${quantity * 10:.2f}"))

if quantity < 4 and category == 1:
    print(f"Your cost after all the discounts were applied: ${(quantity * 5):.2f}")
    print(f'Your price is $5.00 per ticket')
if quantity < 4 and category == 2:
    print(f"Your cost after all the discounts were applied: ${(quantity * 7):.2f}")
    print(f'Your price is $7.00 per ticket')
if quantity < 4 and category == 3:
    print(f"Your cost after all the discounts were applied: ${(quantity * 2):.2f}")
    print(f'Your price is $2.00 per ticket')
if quantity < 4 and category == 4:
    print(f"Your cost after all the discounts were applied: ${(quantity * 4):.2f}")
    print(f'Your price is $4.00 per ticket')
if quantity < 4 and category == 5:
    print(f"Your cost after all the discounts were applied: ${(quantity * 10):.2f}")
    print(f'Your price is $10.00 per ticket')

if 4 <= quantity <= 8 and category == 1:
    print(f"Your cost after all the discounts were applied: ${(quantity * 5)-(quantity * 5 * .1):.2f}")
    print(f'Your price is ${((quantity * 5)-(quantity * 5 * .1))/quantity:.2f} per ticket')
elif 9 <= quantity <= 15 and category == 1:
    print(f"Your cost after all the discounts were applied: ${(quantity * 5)-(quantity * 5 * .15):.2f}")
    print(f'Your price is ${((quantity * 5)-(quantity * 5 * .15))/quantity:.2f} per ticket')
elif quantity > 15 and category == 1:
    print(f"Your cost after all the discounts were applied: ${(quantity * 5)-(quantity * 5 * .2):.2f}")
    print(f'Your price is ${((quantity * 5)-(quantity * 5 * .2))/quantity:.2f} per ticket')

if 4 <= quantity <= 8 and category == 2:
    print(f"Your cost after all the discounts were applied: ${(quantity * 7)-(quantity * 7 * .1):.2f}")
    print(f'Your price is ${((quantity * 7)-(quantity * 7 * .1))/quantity:.2f} per ticket')
elif 9 <= quantity <= 15 and category == 2:
    print(f"Your cost after all the discounts were applied: ${(quantity * 7)-(quantity * 7 * .15):.2f}")
    print(f'Your price is ${((quantity * 7)-(quantity * 7 * .15))/quantity:.2f} per ticket')
elif quantity > 15 and category == 2:
    print(f"Your cost after all the discounts were applied: ${(quantity * 7)-(quantity * 7 * .2):.2f}")
    print(f'Your price is ${((quantity * 7)-(quantity * 7 * .2))/quantity:.2f} per ticket')

if 4 <= quantity <= 8 and category == 3:
    print(f"Your cost after all the discounts were applied: ${(quantity * 2)-(quantity * 2 * .1):.2f}")
    print(f'Your price is ${((quantity * 2)-(quantity * 2 * .1))/quantity:.2f} per ticket')
elif 9 <= quantity <= 15 and category == 3:
    print(f"Your cost after all the discounts were applied: ${(quantity * 2)-(quantity * 2 * .15):.2f}")
    print(f'Your price is ${((quantity * 2)-(quantity * 2 * .15))/quantity:.2f} per ticket')
elif quantity > 15 and category == 3:
    print(f"Your cost after all the discounts were applied: ${(quantity * 2)-(quantity * 2 * .2):.2f}")
    print(f'Your price is ${((quantity * 2)-(quantity * 2 * .2))/quantity:.2f} per ticket')

if 8 >= quantity >= 4 and category == 4:
    print(f"Your cost after all the discounts were applied: ${(quantity * 4)-(quantity * 4 * .1):.2f}")
    print(f'Your price is ${((quantity * 4)-(quantity * 4 * .1))/quantity:.2f} per ticket')
elif 9 <= quantity <= 15 and category == 4:
    print(f"Your cost after all the discounts were applied: ${(quantity * 4)-(quantity * 4 * .15):.2f}")
    print(f'Your price is ${((quantity * 4)-(quantity * 4 * .15))/quantity:.2f} per ticket')
elif quantity > 15 and category == 4:
    print(f"Your cost after all the discounts were applied: ${(quantity * 4)-(quantity * 4 * .2):.2f}")
    print(f'Your price is ${((quantity * 4)-(quantity * 4 * .2))/quantity:.2f} per ticket')

if 4 <= quantity <= 8 and category == 5:
    print(f"Your cost after all the discounts were applied: ${(quantity * 10)-(quantity * 10 * .1):.2f}")
    print(f'Your price is ${((quantity * 10)-(quantity * 10 * .1))/quantity:.2f} per ticket')
elif 9 <= quantity <= 15 and category == 5:
    print(f"Your cost after all the discounts were applied: ${(quantity * 10)-(quantity * 10 * .15):.2f}")
    print(f'Your price is ${((quantity * 10)-(quantity * 10 * .15))/quantity:.2f} per ticket')
elif quantity > 15 and category == 5:
    print(f"Your cost after all the discounts were applied: ${(quantity * 10)-(quantity * 10 * .2):.2f}")
    print(f'Your price is ${((quantity * 10)-(quantity * 10 * .2))/quantity:.2f} per ticket')
