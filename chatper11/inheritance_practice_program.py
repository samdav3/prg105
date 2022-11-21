from inheritance_classes import Employee
from inheritance_classes import ProductionWorker


def main():
    print('Please enter Employee information:')
    employee_info = Employee(employee_name=input('Name: '), employee_number=input('Employee Number: '))
    shift = ProductionWorker(shift_number=input('Shift Number ( 1=day, 2=night, 0=unassigned): '), hourly_pay=input('Hourly Pay Rate: '), employee_name=employee_info, employee_number=employee_info)
    
    print(employee_info.__str__())
    print(shift.__str__())


main()
