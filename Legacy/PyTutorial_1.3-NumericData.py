## PyTutorial 1.3 - Working with numeric data

# # Numeric data in Python is most commonly represented in integers and floats.
# # Python is a dynamically typed language, meaning that we don't need to predefine
# # the data type of a given object as we do in FORTRAN, C, C++, or Java.
# # Python will automatically detect and assign data types on the fly.
# # We can display the data type of an object using the built-in function 'type()'

# num = 1
# print(type(num))

# num = 1.
# print(type(num))

#------------------------------------

# # Python has several built-in arithmetic operators:
# # Addition: 		3 + 2
# # Subtraction:  	3 - 2
# # Multiplication:	3 * 2
# # Division:		  	3 / 2
# # Floor Division: 	3 // 2
# # Exponent:			3 ** 2
# # Modulus:			3 % 2

# x = 5
# y = 2
# print('{} + {} = {}'.format(x,y,x+y))
# print('{} - {} = {}'.format(x,y,x-y))
# print('{} * {} = {}'.format(x,y,x*y))
# print('{} / {} = {}'.format(x,y,x/y))
# print('{}// {} = {}'.format(x,y,x//y))
# print('{}**{}  = {}'.format(x,y,x**y))
# print('{} % {} = {}'.format(x,y,x%y))

#------------------------------------

# # Python follows the standard order of operations for arithmetic:
# print(3 * 2 + 1 - 2 / 4)
# print((3 * 2 + 1) - 2 / 4)
# print(3 * (2 + 1) - 2 / 4)
# print(3 * ((2 + 1) - 2) / 4)
# print(3 * ((2 + 1) - 2 / 4))

#------------------------------------

# # There are several ways we can increment variables:
# num = 1
# print(num)

# num = num + 1
# print(num)

# # Shorthands for incrementing by a constant:
# num += 1
# print(num)

# num -= 1
# print(num)

# # Shorthand for multiplying by a constant:
# num *= -10
# print(num)

#------------------------------------

# # Taking the absolute value of a number:
# num = abs(num)
# print(num)

#------------------------------------

# # Rounding a float value to the nearest integer:
# x = 3.7548
# print(round(x))

# # Passing an integer n to the 2nd argument of round(x,n) will instead round 
# # the nth digit after the decimal
# x = 3.7548
# print(round(x))
# print(round(x,1))
# print(round(x,2))
# print(round(x,3))

#------------------------------------

# # Python has several built-in comparison operators:
# # Equal:			x == y
# # Not Equal:		x != y
# # Greater Than: 	x > y
# # Less Than:		x < y
# # Greater or Equal:	x >= y
# # Less or Equal:	x <= y

# x = 3
# y = 2
# print('{} == {} = {}'.format(x,y,x == y))
# print('{} != {} = {}'.format(x,y,x != y))
# print('{}  > {} = {}'.format(x,y,x > y))
# print('{}  < {} = {}'.format(x,y,x < y))
# print('{} >= {} = {}'.format(x,y,x >= y))
# print('{} <= {} = {}'.format(x,y,x <= y))

#------------------------------------

# # A common problem you'll encounter is converting between numerical data types and strings.
# # Suppose we read in some numbers from a file, but they are represented as strings.

# x_str = '100.2'
# y_str = '200.1'
# print(type(x_str))

# # Arithmetic on strings doesn't work the same as for numbers:
# print('x = ', x_str)
# print('y = ', y_str)
# print('x + y = ', x_str + y_str)

# # We can cast these strings as floats using the float() function
# x = float(x_str)
# y = float(y_str)
# print(type(x))

# # Now we can perform arithmetic operations as usual
# print('x = ', x)
# print('y = ', y)
# print('x + y = ', x + y)

# # We can also cast the floats as integers using the int() function
# x = int(x)
# y = int(y)
# print(type(x))
# print('x = ', x)
# print('y = ', y)
# print('x + y = ', x + y)

# # Note that we can cast strings directly to integers using int() only if they have no decimal:
# x_str = '100'
# y_str = '100.'
# print(int(x_str))
# print(int(y_str))