from inheritance_classes import Employee
from inheritance_classes import ProductionWorker


def main():
    print('Please enter Employee information:')
    name = input('Name: ')
    number = input('Employee Number: ')
    shift = input('Shift (1=day, 2=night, 0=unassigned): ')
    pay = input('Hourly Pay Rate: ')
    new_employee = ProductionWorker(name, number, shift, pay)
    print('Employee Name: ' + new_employee.get_employee_name() + '\nEmployee Number: ' + new_employee.get_employee_number() + '\nShift: ' + new_employee.get_shift_number() + '\nHourly Pay Rate: ' + new_employee.get_hourly_pay())


main()
