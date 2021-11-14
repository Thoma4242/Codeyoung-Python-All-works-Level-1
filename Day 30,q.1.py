class Employee(object):
 standard_pay_rate = 0.0
def __init__(self, name, number, hire_date):
 self._name = name
 self._number = number
 self._hire_date = hire_date
def get_employee_name(self):
 return self._name
def get_employee_number(self):
 return self._number
def get_employee_hire_date(self):
 return self._hire_date
def set_employee_name(self, name):
 self._name = name
def set_employee_number(self, number):
 self._number = number
def set_employee_hire_date(self, hire_date):
 self._hire_date =_hire_date
