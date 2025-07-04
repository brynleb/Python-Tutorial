## PyTutorial 1.2 - Strings and string functions

# Comments are preceded by a hastag '#', or with the hotkey: Alt + /

# # Print a message to the screen
# print('Hello World')

#------------------------------------

# # Define a string variable to hold the message
message = 'Hello World'
print(message)

#------------------------------------

# Strings can be defined with single or double quotes
# message = "Hello World"
# print(message)

# # Beware of using multiple quotes in single string: e.g. 'Harry's Car' results in an error
# # Solution:
# message = "Harry's car"
# # Alternate solution:
# message = 'Harry\'s car'
# print(message)

#------------------------------------

# # Strings can be defined across multiple lines using triple quotes
# message = """Harry's car had
# a bad day"""
# print(message)

#------------------------------------

# # Strings are just a list of characters.
# # We can operate on individual characters with basic functions from the standard library.
# # The function 'len(s)' returns the number of characters in string 's'
# message = 'Hello World'
# print(len(message))

#------------------------------------

# # Individual characters can be accessed with square brackets by passing the index of the desired character:
# # Note the first character is accessed with index = 0, and the last is index = len(s)-1
# message = 'Hello World'
# print(message[0])
# print(message[1])
# print(message[2])
# print(message[3])
# print(message[4])
# print(message[10])
# print(message[11])
# # Note the error thrown by Python on the last command:
# # 'string index out of range' because the last character is at index = 10

#------------------------------------

# # We can access a range of characters using the colon ':'
# message = 'Hello World'
# print(message[0:5])
# # Here, the 1st index is inclusive but the 2nd index is not
# # This means Python will return a string starting at the 1st index up to, but not including, the 2nd index.

# # Leaving the 1st index blank will default to the beginning of the string
# print(message[:5])
# # Leaving the 2nd index blank will default to the end of the string
# print(message[6:])

#------------------------------------

# # Suppose we want to count the number of occurances a particular letter has in a string.
# # We can use the string method 'count(s)' which takes a string as an argument:
# message = 'Hello World'
# print(message.count('l'))

# # We can also count the number of sub-strings in a string by passing that to count:
# print(message.count('Hello'))

# # Note that count is case sensitive:
# print(message.count('hello'))

#------------------------------------

# # We can also find where particular sub-strings are in a string using 'find(s)'.
# message = 'Hello World'
# print(message.find('o'))
# # Note that 'find(s)' returns the index corresponding to the first occurance of s.

# print(message.find('World'))
# # In this case, it returns the index of message corresponding to the first character in 'World'.

# # 'find(s)' is also case sensitive, and returns -1 if the sub-string is not found.
# print(message.find('world'))

#------------------------------------

# # If we want to replace part of a string with a new string,
# # we can use the 'replace(s1,s2)' method which replaces sub-string s1 with s2
# message = 'Hello World'
# new_message = message.replace('World', 'Universe')
# print(new_message)

# # Note that 'replace' does not modify the original string, it returns a new one
# message.replace('World', 'Universe')
# print(message)

#------------------------------------

# # We can combine/concatenate multiple strings together using '+'
# greeting = 'Hello'
# name = 'Michael'
# message = greeting + name
# print(message)

# # Add a comma and a space:
# message = greeting + ', ' + name
# print(message)

# # Add another word and more punctuation:
# message = greeting + ', ' + name + '. Welcome!'
# print(message)

#------------------------------------

# A more elegant way to combine strings is to use a format statement.
# Placeholders are specified with curly brackets {}
# greeting = 'Hello'
# name = 'Michael'
# message = '{} {}, Welcome!'.format(greeting, name)
# print(message)

#------------------------------------

# # We could also use f-strings, which is new since Python 3.6 and aims to make string formating as simple as possible.
# # f-strings are preceded with an 'f' before the string statement, and the variables appear directly within the placeholders:
# greeting = 'Hello'
# name = 'Michael'
# message = f'{greeting} {name}, Welcome!'
# print(message)

# # The advantage of f-strings is that code can be written directly within the placeholders.
# message = f'{greeting.lower()} {name.upper()}, Welcome!'
# print(message)

#------------------------------------

# # Tips and tricks:
# # Use the 'dir' function to get a list of all the attributes and methods accessible to a particular variable
# message = 'Hello World'
# print(dir(message))

# # Use type(variable) to return the variable type of a given variable
# print(type(message))

# # Use the 'help' function with a given variable type to get a description of its attributes and methods
# print(help(type(message)))

# # You can also specify a specific attribute or message:
# print(help(type(message).replace))