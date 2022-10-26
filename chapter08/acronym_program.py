print('This program accepts a phrase and returns the acronym.')
phrase = input('Please enter a phrase to convert: ')
phrase = phrase.split()
let1 = phrase[0]
let2 = phrase[1]
let3 = phrase[2]
ac1 = let1[0]
ac2 = let2[0]
ac3 = let3[0]
print(f'{ac1.upper()}{ac2.upper()}{ac3.upper()}')
