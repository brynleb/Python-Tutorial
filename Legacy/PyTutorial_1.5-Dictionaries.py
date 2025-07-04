## PyTutorial 1.5 - Dictionaries

# Dictionaries allow us to work with key-value pairs
# In other languages these are called 'hashmaps' or 'associative arrays'
# A key is a unique identifier that references a particular value.
# Keys are typically strings, but can also be integers or floats
# Values can be any mutable object

# # Dictionaries are defined with curly brackets:
# d = {'name': 'John', 'age': 25, 'courses': ['Math', 'Physics'], 1: 'one', 3.14: 'pi'}
# print(d)

# # We can access particular values by passing the corresponding key in square brackets:
# print(d['name'])
# print(d['age'])
# print(d['courses'])
# print(d[1])
# print(d[3.14])

#-------------------------------------

# # To access values, we can also use the dictionary method 'get':
# student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Physics']}
# print(student.get('name'))

# # If we try to get the value of a key that doesn't exist in the dictionary, we get a key error:
# # print(student['phone'])

# # Instead of an error, using 'get' with a key that doesn't exist will return 'None' by default
# print(student.get('phone'))
 
# # We can also specify what value get will return if the key doesn't exist:
# print(student.get('phone', 'Key not found'))

#-------------------------------------

# # To add a value to a dictionary or to update an existing value,
# # we simply assign a new value to that key:
# student = {'name': 'John', 'age': 25, 'courses': ['Math','Physics']}
# student['name'] = 'Jane'
# student['phone'] = '555-5555'
# print(student)

# # We can update multiple values at a time with the 'update' method:
# student.update({'age': 39, 'phone': '443-9243'})
# print(student)

#-------------------------------------

# # To delete elements from a dictionary we can use the 'del' keyword
# student = {'name': 'John', 'age': 25, 'courses': ['Math','Physics']}
# del student['age']
# print(student)

# # We can also remove elements with the 'pop' method, but remember that pop returns that value:
# courses = student.pop('courses')
# print(courses)
# print(student)

#-------------------------------------

# # To access the length of a dictionary, we can use the len() function: 
# student = {'name': 'John', 'age': 25, 'courses': ['Math','Physics']}
# print(len(student))

# # To access all the keys or values, use the 'keys' or 'values' methods:
# print(student.keys())
# print(student.values())

# # To access the key-value pairs, use the 'items' method:
# print(student.items())

# # Note that each of these methods returns a specific data type: 'dict_keys', 'dict_values', 'dict_items'
# # These data types are not subscriptable (we can use the square brackets to access their elements)
# print(student.keys()[0])

# # Instead, we can convert these into a list using the list() function:
# keys = list(student.keys())
# values = list(student.values())
# items = list(student.items())
# print(keys)
# print(values)
# print(items)
# print(keys[0])
# print(values[0])
# print(items[0])
# print(items[0][1])
