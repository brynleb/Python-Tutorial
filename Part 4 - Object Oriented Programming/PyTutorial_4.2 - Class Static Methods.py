class Employee:
    ## Class variables -- shared amongst all instances of a class
    num_of_emps = 0
    raise_amt   = 1.04

    ## Init method -- runs once each time a new instance is created (constructor in c++)
    def __init__(self, first, last, pay):
        ## Instance variables -- used for data that is unique to each class instance
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        ## Class variable -- shared amongst all instances of a class
        Employee.num_of_emps += 1

    ## Method -- automatically takes instance as first argument
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    ## Method -- automatically takes instance as first argument
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    ## Class method -- @classmethod decorator alters the functionality of the method to take the class as the first argument
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    ## Static method -- @staticmethod decorator disables automatic passing of class or instance
    ## Methods should be static if cls or self attributes are not called
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt,'\n')

## Running the class method automatically passes the class as the first argument
# Employee.set_raise_amt(1.05)
## This is the same as running: 
## Employee.raise_amt = 1.05

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt,'\n')

## Class methods can be used as alternative constructors
## Example: create an employee out of a string using 'from_string' class method instead of init method

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

# first, last, pay = emp_str_1.split('-')

# # new_emp_1 = Employee(first, last, pay)
# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)
 
import datetime
my_date = datetime.date(2020, 4, 24)
print(Employee.is_workday(my_date))