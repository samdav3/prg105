class Employee:
    def __init__(self, employee_name, employee_number):
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number

    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.__employee_number

    def __str__(self):
        employee_info = 'Employee Name: ' + self.get_employee_name() + '  ' + 'Employee Number: ' + self.get_employee_number()
        return employee_info


class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay):
        Employee.__init__(self, employee_name, employee_number)
        self.__shift_number = shift_number
        self.__hourly_pay = hourly_pay

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_pay(self, hourly_pay):
        self.__hourly_pay = hourly_pay

    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_pay(self):
        return self.__hourly_pay

    def __str__(self):
        production_worker_info = 'Employee name: ' + self.get_employee_name() + '  ' + 'Employee Number: ' + self.get_employee_number() + '  ' + 'Shift number:' + self.get_shift_number() + '  ' + 'Hourly pay rate: ' + self.get_hourly_pay()
        return production_worker_info
