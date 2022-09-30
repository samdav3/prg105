
age = int(input('How old are you currently? '))
retire = int(input('At what age do you plan to retire? '))
income = int(input('What is your yearly income? '))
save_percentage = int(input('What percent of your income do you save? %'))
savings = int(input('How much money do you currently have in savings? '))
print('This project assumes a 3% raise each year and a 6% yearly return on investment.')
print('Age\t\tIncome\t\t\tSavings Contribution\t\tTotal Savings')
for age in range(age, (age + 1)):
    print(f'{age}\t\t', f'{income:,.2f}\t\t', f'{(income * (save_percentage / 100)):,.2f}\t\t\t\t\t', f'{savings + (income * (save_percentage / 100)) + (savings * .06):,.2f}')
    total = savings + (income * (save_percentage / 100)) + (savings * .06)
while age < retire:
    age = age + 1
    income = (income * .03) + income
    contribution = income * (save_percentage / 100)
    total = total + contribution + (total * .06)
    print(f'{age}\t\t', f'{income:,.2f}\t\t', f'{contribution:,.2f}\t\t\t\t\t', f'{total:,.2f}')
