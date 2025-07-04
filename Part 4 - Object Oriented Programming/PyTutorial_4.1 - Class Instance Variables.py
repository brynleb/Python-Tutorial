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

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

## Print the namespace of a class using:
# print(Employee.__dict__)

## Print the namespace of an instance using:
# print(emp_1.__dict__)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

## Can access a class variable from both class name and instances
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt,'\n')

## When accessing an attribute from an instance, Python will first look for that attribute in the instance
## If it doesn't exist as an instance attribute, it will then check in the class definition

## Changing the raise_amount in the class modifies it for all instances
Employee.raise_amt = 1.05

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt,'\n')

## Changing the raise_amt in an instance modifies it for only that instance
emp_1.raise_amt = 1.06

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt,'\n')
