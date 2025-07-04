# PyTutorial 1.9 - Functions and Lambdas

# In Python, functions are subroutines that package together several instructions.
# The allow us to pass arguments as input and optionally return the value of an object.
# The main benefit of function is that they allow us to write code that does not have redundant copies of itself.
# It is generally good practice to write code that is as DRY (Don't Repeat Yourself) as possible!

# # To create a function in Python, use the 'def' keyword (which stands for define):
# def func():
# 	pass
# # The pass keyword allows us to create a function with no return value

# # We can print the function definition and its location in memory:
# print(func)
# # Note that this does not execute the function

# # To execute a function we need to include paratheses:
# print(func())
# # This function returns 'None' because it has no return value

#-------------------------------------

# # This example function has no return value:
# def hello_func():
# 	print('Hello Function!')

# hello_func()
# # Note that since the print statement appears in the function, we don't need one when executing the function.

# # We can execute the function several times without repeating the code within the function:
# hello_func()
# hello_func()
# hello_func()

# # This example illustrates the benefit of functions and writing DRY code.
# # If we want to modify a block of code that appears regularly within a larger body of code,
# # it's usually best to define a function that contains that block in a single location.
# # This makes modifying that block within a larger project much easier to implement.

#-------------------------------------

# # This example returns a string:
# def hello_func():
# 	return 'Hello Function!'

# print(hello_func())
# # Here, the print statement is needed to display the string returned by the function.

# # We can treat functions in the same way as the data type it returns
# print(type(hello_func()))

# # For example, we can use the 'len' function to get the number of characters
# # in the string returned by the function:
# print(len(hello_func()))

# # We can also use the 'upper' method to change the string to all upper case:
# print(hello_func().upper())

#-------------------------------------

# # To pass an argument called 'greeting' to the function:
# def hello_func(greeting):
# 	return '{} Function!'.format(greeting)
# # Here, greeting is another string that is combined with the returned string.

# # Now if we try to execute the function without passing a value for 'greeting', we'll get a error:
# print(hello_func())
# # TypeError: hello_func() missing 1 required positional argument: 'greeting'
# # This is because 'greeting' is now a required argument (it has no default value)

# # Executing the function with a value for greeting:
# print(hello_func('Hi'))

# # Note that greeting is a local variable within the function.
# # Its value is does not affect variables outside the function. (See Python Scope)
# # For example:
# greeting = 'Hello'
# print(hello_func('Hi'))
# print(greeting)

#-------------------------------------

# # We can also define default values for arguments, which renders them as optional keyword arguments.
# # To create a 2nd argument with a default value:
# def hello_func(greeting, name='You'):
# 	return '{}, {}'.format(greeting, name)

# print(hello_func('Hi'))
# # Since we did not specify a value for 'name', the function used the default value 'You'.
# print(hello_func('Hi', 'Brynle'))
# # When we specify a value for 'name', the default value is overwritten.

# # Note that the required positional arguments must come before the keyword arguments.
# # If instead we write them out of order:
# def hello_func(name='You', greeting):
# 	return '{}, {}'.format(greeting, name)
# # We get an error: SyntaxError: non-default argument follows default argument

#-------------------------------------

# # Python allows us to write functions with an arbitrary number of arguments in a compact form.
# # For example:
# def student_info(*args, **kwargs):
# 	print(args)
# 	print(kwargs)

# # '*args' allows the function to take an arbitrary number of positional arguments.
# # '**kwargs' allows the function to take an arbitrary number of key word arguments
# # In this example, 'args' represents the courses the student is taking and
# # 'kwargs' are other information about the student.
# # This format is useful when we don't know how many arguments there will be.

# student_info('Math', 'Art', name='John', age=22)

#-------------------------------------

# # Another way to do this is to call the function with a list called 'courses'
# # and a dictionary called 'info' containing the positional and keyword arguments, respectively.
# # Preceding a list with '*' indicates to Python to unpack the list one element at a time,
# # and '**' tells Python to unpack the dictionary one key-value pair at a time. 
# def student_info(*args, **kwargs):
# 	print(args)
# 	print(kwargs)

# courses = ['Math', 'Art']
# info = {'name': 'John', 'age': 22}

# # Executing the function in this way will pass the arguments as in the example above:
# student_info(*courses, **info)

#-------------------------------------

# # The following example computes the numbers of days in a given month in a given year.

# # List of days in each month. The index corresponds to a given month (0 = Jan, 1 = Feb, etc.)
# month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

# # This function returns True if a year is a leap year and False otherwise. It can be read as follows:
# # if the year is divisible by 4 and (the year is not divisible by 100 or the year is divisible by 400).
# def is_leap(year):
# 	"""Return True for leap years, False for non-leap years"""

# 	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
# # The string in triple quotes within the function is called a doc-string.
# # These help document what a function does. It's good practice to use these.

# # This function takes a year and month as positional arguments and returns the number of days in that month.
# # If the month is not between 1 and 12, the function returns 'Invalid month'.
# # If the month is 2 (February) and if the function is_leap(year) is True,
# # then the function returns 29 for that month.
# # If neither of these conditions are met, then it returns the element of the list
# # month_days corresponding to the month (index = month - 1).
# def days_in_month(year, month):
# 	"""Return number of days in that month in that year."""

# 	if not 1 <= month <= 12:
# 		return 'Invalid month'
# 	if month == 2 and is_leap(year):
# 		return 29

# 	return month_days[month-1]
# # Note that functions can make use of objects defined outside their scope (e.g. month_days),
# # which act like global variables. Variables defined within a function are local variables.

# year = 2024
# month = 2
# print(is_leap(year))
# print(days_in_month(year,month))

# # We can print this in a more user friendly fashion:
# month_str = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
# print('Is {} a leap year? {}'.format(year, is_leap(year)))
# print('Number of days in {} of {}: {}'.format(month_str[month-1], year, days_in_month(year,month)))

#-------------------------------------

# # Python also has a simple way to write mathematical expressions as functions using
# # the 'lambda' keyword. They are restricted to a single expression, but can have
# # multiple positional arguments.
# # For example:
# func = lambda x, y: (x + y)**2
# print(func(1,2))
# # A Lambda function object is equivalent to a function object
# # and can be used whereever function objects are required.