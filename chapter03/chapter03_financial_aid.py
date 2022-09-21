# Variables
eligible_for_financial_aid = True

status = (input('Are you a new or returning Student? (n/r)  '))
if status == 'r' or status == 'R':
    gpa = float(input('What is your current GPA? (x.x)  '))
    if gpa <= 2.0:
        eligible_for_financial_aid = False
        print('Your GPA must be higher than 2.0 to apply for financial aid.')
criminal_record = str(input('Have you ever been convicted of a drug felony? (y/n)  '))
if criminal_record == 'y' or criminal_record == 'Y':
    eligible_for_financial_aid = False
    print('You cannot have a drug-related felony to apply for financial aid.')
credit_hours = int(input('How many credit hours are you taking next semester?  '))
if credit_hours < 6:
    eligible_for_financial_aid = False
    print('You must take at least 6 credit hours to apply for financial aid.')
gross_income = int(input('What is your gross yearly income, rounded to the nearest dollar? (Do Not Use Commas)  '))
if gross_income > 50000:
    eligible_for_financial_aid = False
    print('Your annual gross income must be less than $50,000 to apply for financial aid.')

if eligible_for_financial_aid:
    print('Based on the information you have provided, you have been approved to apply for financial aid.')
else:
    print('Based on the information you have provided, you have not been approved to apply for financial aid.')
