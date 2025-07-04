# PyTutorial 1.10 - Importing modules and the standard library

# In Python, a module is some code written in a separate file.
# We can import modules into our main body of code using the 'import' command.
# When importing a module, Python runs all the code in that file.
 
# Here, we're importing a custom module from the file 'MyModule.py' located
# in the same directory as this file.
import MyModule

# We can now access objects defined within the module. 
# We must reference the module name:
print(MyModule.test)

courses = ['History', 'Math', 'Physics', 'CompSci']

# To execute the function find_index defined in the module:
index = MyModule.find_index(courses, 'Physics')
print(index)

#-------------------------------------

# # To reduce the length of the module name,
# # we can import the module using an alias 'mm':
# import MyModule as mm

# courses = ['History', 'Math', 'Physics', 'CompSci']
# index = mm.find_index(courses,'Math')
# print(index)

#-------------------------------------

# # We can also import specific objects from 'MyModule.py'
# from MyModule import find_index

# courses = ['History', 'Math', 'Physics', 'CompSci']
# index = find_index(courses, 'Math')
# print(index)
# print(test)
# # Note that this method only imports the find_index, so the above results in a NameError.

# # We do not have access to other objects in MyModule (e.g. test)
# # To import test as well, we can add this to the list of imported objects:
# # from MyModule import find_index, test

#-------------------------------------

# # Now lets import the sys module from the standard library.
# import sys

# # When importing modules, Python checks the folders contained within the sys.path variable
# # in the order that they appear.
# # We can check these folders by printing out the sys.path variable.
# print(sys.path)

# # First, Python checks your working directory (the directory where you are running your script).
# # Next, Python checks the PythonPath environment variable.
# # Next, Python checks the standard library directories (defined in your system's PATH environment variable).
# # Finally, Python checks the 'site-packages' directory for third party packages.

# # If MyModule.py is not in your working directory, it can be appended to sys.path using
# # sys.path.append('directory name')
# # One can also edit the PythonPath variable, but this should be done uniquely for each editor.

#-------------------------------------

# # Some examples of useful modules from the standard library
# # A module containing random variable generators:
# import random

# courses = ['History', 'Math', 'Physics', 'CompSci']
# random_course = random.choice(courses)
# print(random_course)

#-------------------------------------

# # A module containing mathematical functions defined by the C standard
# import math

# pi = math.pi
# theta_deg = 90.
# theta_rad = math.radians(theta_deg)
# sin_theta = math.sin(theta_rad)

# print(pi)
# print(theta_rad)
# print(sin_theta)

#-------------------------------------

# # A module containing definitions of the datetime class and many date and time functions
# import datetime
# # A module containing the calendar class and calendar print functions
# import calendar

# today = datetime.date.today()
# isleap = calendar.isleap(2022)

# print(today)
# print(isleap)

#-------------------------------------

# # The os module gives access to your operating system subroutines
# import os

# # Use 'dir' function to get list of all methods and attributes available in a given module
# print(dir(os))

# # Get the current working directory:
# cwd = os.getcwd()
# print(cwd)

# # Get the location of the Python standard library:
# stdlibpath = os.__file__
# print(stdlibpath)

#-------------------------------------

# # A joke built into the Python standard library!
# import antigravity
