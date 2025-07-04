class Employee:

	# Init method runs once each time a new instance is created (like a constructor in c++)
    def __init__(self, first, last, pay):
	    # Instance variables -- used for data that is unique to each class instance
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

	## Method -- automatically takes instance as first argument
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.email)
print(emp_2.email)

# Calling methods from an instance -- instance is passed automatically as the 'self' argument
print(emp_1.fullname())
print(emp_2.fullname())

# Calling methods from a class name -- must pass an instance as argument 'self'
print(Employee.fullname(emp_1))
