class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

## Developer class inherits all attributes and methods from Employee class
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        ## Here, we want to use the init method of the inherited class
        ## Using super() allows simple maintainence of code when using multiple inheritance
        super().__init__(first, last, pay)
        ## An alternative solution -- ok for single-level inheritance
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

## Manager class inherits all attributes and methods from Employee class
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

# print(help(Developer))

print(dev_1.__dict__)
print(dev_2.__dict__)

# dev_1.apply_raise()
# print(dev_1.pay,'\n')

# mgr_1 = Manager('Sue', 'Smith', 90000)

# print(mgr_1.email)

# mgr_1.add_emp(dev_1)
# mgr_1.add_emp(dev_2)

# mgr_1.remove_emp(dev_1)

# mgr_1.print_emps()

## Python has built-in functions 'isinstance' and 'issubclass' for testing

# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Developer))
# print(isinstance(mgr_1, Employee),'\n')

# print(isinstance(dev_1, Manager))
# print(isinstance(dev_1, Developer))
# print(isinstance(dev_1, Employee),'\n')

# print(issubclass(Manager, Developer))
# print(issubclass(Manager, Employee))
# print(issubclass(Developer, Manager))
# print(issubclass(Developer, Employee))