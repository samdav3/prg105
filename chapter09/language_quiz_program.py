print('Enter the number in English which corresponds to the number in Spanish.')
span_quiz = {'uno': 'one', 'dos': 'two', 'tres': 'three', 'cuatro': 'four',
             'cinco': 'five', 'seis': 'six', 'siete': 'seven', 'ocho': 'eight',
             'nueve': 'nine', 'diez': 'ten'}
score = 0
for key in span_quiz:
    answer = input(f'What is the equivalent of {key}: ')
    v = span_quiz[key]
    if answer == v:
        answer = v
        print('Correct')
        score += 1
    else:
        print(f'Incorrect. The correct answer is {span_quiz[key]}')

print(f'Your final score is {score}/10')
if score in range(9, 11):
    print('Your grade is A')
elif score in range(8, 9):
    print('Your grade is B')
elif score in range(7, 8):
    print('Your grade is C')
elif score in range(5, 7):
    print('Your grade is D')
elif score in range(0, 5):
    print('Your grade is F')
