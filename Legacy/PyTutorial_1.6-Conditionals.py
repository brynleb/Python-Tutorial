# PyTutorial 1.6 - Conditionals, Booleans, if, else, and elif statments

# # In Python, boolean variables can take on values of 'True' or 'False'.
# # To construct a conditional statement, we use the 'if' command:
# if True:
# 	print('Conditional was True')
# # This print statement is executed because the conditional is always True.
# # Note the tab indentation which Python uses to recognize code within the if-block.

# if False:
# 	print('Conditional was True')
# # This print statement is not executed because the conditional is always False.

#-------------------------------------

# # Python uses the following comparisons to construct conditional statements:
# # Equal:			== (checks same value)
# # Not equal: 		!=
# # Greater than:		>
# # Less than:		<
# # Greater or equal: >=
# # Less or equal: 	<=
# # Object Identity:	is (checks same location in memory)

# # To construct a complete if-elif-else block:
# language = 'Python'
# # language = 'Java'
# # language = 'C++'
# # language = 'Fortran'
# if language == 'Python':
# 	print('Language is Python')
# elif language == 'Java':
# 	print('Language is Java')
# elif language == 'C++':
# 	print('Language is C++')
# else:
# 	print('No language match')
# # Note that we can keep adding 'elif' statements.
# # The 'else' statement is always the last case.

#-------------------------------------

# # Python uses the following keywords as boolean operators:
# # 'and', 'or', 'not'
# # For example:
# user = 'Admin'
# logged_in = True
# if user == 'Admin' and logged_in:
# 	print('Admin Page')
# else:
# 	print('Bad credentials')

# if not logged_in:
# 	print('Please log in')
# else:
# 	print('Welcome')

#-------------------------------------

# # To check if the values of two objects are the same, we use '==':
# a = [1,2,3]
# b = [1,2,3]
# print(a)
# print(b)
# print(a == b)

# # To check if the identities of two objects are the same, we use 'is':
# print(id(a))
# print(id(b))
# print(a is b)
# # This is equivalent to id(a) == id(b)

# # We can set these two objects to the same location in memory and check again:
# b = a
# print(id(a))
# print(id(b))
# print(a is b)

# # This works because Python assignment statements pass by reference, not by value.
# # This is especially important when coding with extended objects like lists and arrays.

#-------------------------------------

# # Python conditional tests that will evaluate to False:
# # 	False
# # 	None
# # 	Zero of any numeric type
# # 	Any empty sequence: e.g. '', (), []
# # 	Any empty mapping: e.g. {}

# # For example:
# condition = False
# condition = None
# condition = 0
# condition = 0.
# condition = 10
# condition = ''
# condition = 'a'
# condition = []	# Empty list
# condition = [1,2,3]
# condition = {}	# Empty dictionary
# condition = {'name': 'John'}

# if condition:
# 	print('Evaluated to True')
# else:
# 	print('Evaluated to False')
