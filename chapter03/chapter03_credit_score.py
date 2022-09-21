
credit_score = int(input('What is your credit score?  '))
if credit_score <= 629:
    print(f'With a credit score of {credit_score}, you have bad credit.')
elif 630 <= credit_score <= 689:
    print(f'With a credit score of {credit_score}, you have fair credit.')
elif 690 <= credit_score <= 719:
    print(f'With a credit score of {credit_score}, you have good credit.')
else:
    print(f'With a credit score of {credit_score}, you have excellent credit.')
