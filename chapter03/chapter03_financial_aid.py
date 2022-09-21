# Variables
eligible_for_financial_aid = True
min_gpa = 2.0
gpa_na = 0.0
min_credit_hours = 6
max_gross_income = 49999
criminal_record = 'no'

status = str(input('Are you a new or returning Student? (n/r)  '))
gpa = float(input('What is your current GPA? (x.x)  '))
if gpa <= min_gpa:
    eligible_for_financial_aid = False
    print('Your GPA must be greater than 2.0 to apply for financial aid.')
criminal_record = str(input('Have you ever been convicted of a drug felony? (y/n)  '))
if criminal_record:
    eligible_for_financial_aid = False
    print('You cannot apply for financial aid when you have been convicted of a drug-related felony.')
credit_hours = int(input('How many credit hours are you taking next semester?  '))
if credit_hours < min_credit_hours:
    eligible_for_financial_aid = False
    print('You must take at least 6 credit hours to apply for financial aid.')
gross_income = int(input('What is your gross yearly income, rounded to the nearest dollar? (Do Not Use Commas)  '))
if gross_income > max_gross_income:
    eligible_for_financial_aid = False
    print('Your gross income must be below $50,000 to apply for financial aid.')

if eligible_for_financial_aid:
    print('Based on the information you have provided, you have been approved to apply for financial aid.')
if not eligible_for_financial_aid:
    print('Based on the information you have provided, you have not been approved to apply for financial aid.')
