## PyTutorial 1.4 - Lists, tuples and sets

# In Python, lists and tuples are collections of objects in a sequence.
# A set is an unordered collection of values with no duplicates.
# Lists use square brackets: [1,2,3]
# Tuples use paratheses: (1,2,3)
# Sets use curly brackets: {1,2,3} or set(1,2,3)
# Lists are the most common object among the three, so we will first focus on how to use them.

#-------------------------------------

# # Lets create a list of strings called courses:
# courses = ['History', 'Math', 'Physics', 'CompSci']
# print(courses)

# # We can get the number of elements in a list using the 'len()' function the same way we count the number of characters in a string.
# print(len(courses))

# # We can access individual elements in a list using an index with square brackets:
# print(courses[0])
# print(courses[1])
# print(courses[2])
# print(courses[3])
# # Note the last element in the list has index = 4-1 = 3, 
# print(courses[4]) 
# # The last line throws the error IndexError: list index out of range

# # We can also use negative indices to start from the end of the list:
# print(courses[-1])
# print(courses[-2])
# print(courses[-3])
# print(courses[-4])
# # Here the last item will always be specified by index = -1, just as the first is always index = 0

# # We can also access a range of values using a semicolon :
# print(courses[0:2])
# # Remember that the 1st index is inclusive, but the 2nd index is not.

# print(courses[2:])
# # This is called slicing.

#-------------------------------------

# # We can slice lists or strings in the same way.
# # For example, to show only the first 3 elements/characters:
# nums = [0,1,2,3,4,5]
# string = 'abcdef'
# print(nums[:3])
# print(string[:3])

# # We can also specify an index step size using a 2nd colon (by default the step size is 1):
# print(nums[0:6:2])
# print(nums[5:0:-2])

# # To return a list in reverse:
# print(nums[::-1])

#-------------------------------------

# # To add an item to the end of our list we can use the 'append' method:
# courses = ['History', 'Math', 'Physics', 'CompSci']
# print(courses)
# courses.append('Art')
# print(courses)
# # Note that 'append' modifies the value of 'courses' in place, like most list methods.

#-------------------------------------

# # To add an element to a specific location we can use the 'insert' method:
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses.insert(0, 'Chemistry')
# print(courses)

# # Insert also works with lists of values
# courses.insert(0, ['Biology', 'French'])
# print(courses)

# # However, this will insert the entire list as the first element, instead of each element individually.
# print(courses[0])

#-------------------------------------

# # There are different ways to combine two or more lists together:
# # We can use the 'extend' method:
# courses_1 = ['History', 'Math', 'Physics', 'CompSci']
# courses_2 = ['Art', 'Chemistry']
# courses_1.extend(courses_2)
# print(courses_1)
# # This adds each element in courses_2 to the end of courses_1 one item at a time.

# # Similarly, we can simply add the two lists:
# courses = courses_1 + courses_2
# print(courses)
# # Note the extend modifies the list in place, while the '+' operation creates a new list.

#-------------------------------------

# # We can multiply a list by an integer 'm' to concatenates that list with itself 'm' times:
# courses_1 = ['History', 'Math', 'Physics', 'CompSci']
# courses_2 = 3*courses_1
# print(courses_2)
# # Note that floating-point multiplication is not defined for lists.

#-------------------------------------

# # We can remove elements from a list using the 'remove' method:
# courses = ['History', 'Math', 'Physics', 'CompSci']
# print(courses)
# courses.remove('Math')
# print(courses)

# # We can also use elements using the 'pop' method.
# # By default this removes the last item in the list:
# courses.pop()
# print(courses)

# # pop() modifies the list in place, but also returns the element it removed:
# popped = courses.pop()
# print(popped)
# print(courses)
# # This is useful if we want to use our list in a queue by looping over the list,
# # popping off elements until the list is empty.

#-------------------------------------

# # Lists can be sorted in several ways.
# # We can reverse the order of the list using the 'reverse' method:
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses.reverse()
# print(courses)

# # To sort a list of strings alphabetically, use the 'sort' method:
# courses.sort()
# print(courses)

# # sort() can also sort of list of numbers in ascending order:
# nums = [3,2,4,1,5]
# nums.sort()
# print(nums)

# # To sort our lists in descending alphabetical/numerical order, we can pass an optional value to sort:
# courses.sort(reverse=True)
# nums.sort(reverse=True)
# print(courses)
# print(nums)

# # The sort method modifies the list inplace. To avoid this we can use
# # the built-in function 'sorted()', which returns a new sorted version of the list.
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses_sorted = sorted(courses)
# print(courses_sorted)
# # This allows us get a sorted list without altering the original.

#-------------------------------------

# # Some useful built-in functions for numerical lists include min(), max(), sum():
# nums = [3,2,4,1,5]
# print(min(nums))
# print(max(nums))
# print(sum(nums))

#-------------------------------------

# # To find the index of a particular element in a list, we can use the 'index' method:
# courses = ['History', 'Math', 'Physics', 'CompSci']
# print(courses.index('Math'))

# # We can verify this worked by returning that same index:
# index = courses.index('Math')
# print(courses[index])

# # If we search for a value that doesn't exist in the list we'll get a value error:
# # print(courses.index('Biology'))

#-------------------------------------

# # To check if a value is in a list we can use the 'in' operator:
# courses = ['History', 'Math', 'Physics', 'CompSci']
# print('Math' in courses)
# print('Art' in courses)
# # This is a conditional test that returns a Boolean (True or False value)

#-------------------------------------

# # A common operation to make on lists is to combine the elements in a string
# # with each element separated by characters. For this we can use a string method called 'join':
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses_str = ', '.join(courses)
# print(courses_str)
# # This returns a single string with each course separated by ', '

# courses_str = ' - '.join(courses)
# print(courses_str)
# # This returns a single string with each course separated by ' - '

# # To convert the string back into a list, we can use the 'split' string method:
# courses_list = courses_str.split(' - ')
# print(courses_list)
# # This will split a string into a list of strings, where the list elements are detected
# # by instances of the argument ' - '

#-------------------------------------

# # While lists are mutable objects (they can be modified), tubles are immutable objects.
# # Tuples are lists that cannot be modified after creation
# # To illustrate the difference between lists and tuples, lets create two lists:
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1
# print(list_1)
# print(list_2)

# # If we change the value of the first element in list_1, this will also modify list_2:
# list_1[0] = 'Art'
# print(list_1)
# print(list_2)
# # This is because both list_1 and list_2 are the same mutable object (the same location in memory).

# # Now lets create two tuples (using parentheses):
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1
# print(tuple_1)
# print(tuple_2)

# # If we try to charge the first element of tuple_1, we can an error:
# tuple_1[0] = 'Art'
# print(tuple_1)
# print(tuple_2)
# # TypeError: 'tuple' object does not support item assignment
# # This is because tuples are immutable

#-------------------------------------

# # A set is a list of values that are unordered and have no duplicates.
# # Sets are defined with curly brackets {}:
# courses_set = {'History', 'Math', 'Physics', 'CompSci'}
# print(courses_set)
# # Each time we run this code, the set can be different because it doesn't care about order.

# # Sets can contain only unique elements, which means they throw away duplicates:
# courses_set = {'History', 'Math', 'Physics', 'CompSci', 'Math', 'History'}
# print(courses_set)

# # Sets are optimized for detecting whether a value is part of a sequence
# # Sets do this 'membership test' much more efficiently than lists and tuples.
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Art', 'Math', 'French'}
# print('Math' in cs_courses)
# print('Math' in art_courses)

# # We can determine which elements are common to two sets using the 'intersection' method:
# print(cs_courses.intersection(art_courses))

# # To determine which elements are different between two sets, use the 'difference' method:
# print(cs_courses.difference(art_courses))

# # Finally, the 'union' method returns the combined set (only unique elements):
# print(cs_courses.union(art_courses))

#-------------------------------------

# # To create empty lists:
# empty_list = []
# empty_list = list()
# print(empty_list)
# print(type(empty_list))

# # To create empty tuples:
# empty_tuple = ()
# empty_tuple = tuple()
# print(empty_tuple)
# print(type(empty_tuple))

# # To create empty sets:
# empty_set = set()
# print(empty_set)
# print(type(empty_set))

# # Beware of this common mistake.
# # This not an empty set but an empty dictionary:
# empty_dict = {}
# print(empty_dict)
# print(type(empty_dict))

#-------------------------------------
