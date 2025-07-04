# PyTutorial 1.7 - Loops and iterations

# # To construct a simple for loop:
# nums = [1,2,3,4,5]
# for item in nums:
# 	print(item)
# # This loop and can be understood quasi-verbatim:
# # for (each) item in (the list) nums:
# #    print (the) item
# # This will loop through and print each number in the list.
# # Note the indent before the print statement.
# # Python reads this white space as an indication that this code is part of the for loop.
# # By default, the print statement will create a new line on each execution.

#-------------------------------------

# # The iterator variable 'item' is a dummy variable and can be (almost) any string:
# nums = [1,2,3,4,5]
# for num in nums:
# 	print(num)

# # The list can be any iterable object and can contain non-numerical entries:
# courses = ['History', 'Math', 'Physics', 'CompSci']
# for course in courses:
# 	print(course)

# # We can also loop through the elements of a dictionary:
# student = {'name': 'John', 'age': 25, 'courses': ['Math','Physics']}
# for key in student:
# 	print(key)
# # Note that this only gives us the keys.

# # To loop over the key-value pairs we need to use the 'items' method
# # with two iterator variables:
# for key, value in student.items():
# 	print(key,':', value)

#-------------------------------------

# # To loop over the indices of a list we can use the 'range' command:
# courses = ['History', 'Math', 'Physics', 'CompSci']
# for i in range(len(courses)):
# 	print(courses[i])
# # In this case the index i runs from i = 0, 1, ..., len(courses)-1 = 3
# # Note that integer iterators always start at zero

#-------------------------------------

# # Sometimes it's useful to have access to both the index and the value of the list.
# # In this case, we can use the enumerate() function, which returns both:
# courses = ['History', 'Math', 'Physics', 'CompSci']
# for index, course in enumerate(courses):
# 	print(index, course)

# # By default, enumerate starts at index = 0. To start the index incrementing elsewhere,
# # we can pass a value to the 'start' keyword of enumerate:
# for index, course in enumerate(courses, start=2):
# 	print(index, course)

#-------------------------------------

# # To construct nested loops (a loop within a loop):
# nums = [1,2,3,4,5]
# string = 'abc'
# for num in nums:
# 	for char in string:
# 		print(num,char)
# # For each number in nums, this loop will print out the number
# # with each character in the string 'abc'

#-------------------------------------

# # Two important keywords when working with loops:
# # 	'break' will exit the loop on a given iteration
# # 	'continue' will move on the next iteration of the loop
# # Example of a loop using the 'break' statement
# nums = [1,2,3,4,5]
# for num in nums:
# 	if num == 3:
# 		print(num,'found!')
# 		break
# 	print(num)

# # Example of using 'continue'
# for num in nums:
# 	if num == 3:
# 		print(num,'found!')
# 		continue
# 	print(num)

# # Note the break will only exit one level of a nested loop:
# nums = [1,2,3,4,5]
# string = 'abc'
# for num in nums:
# 	for char in string:
# 		if num == 3 and char == 'b':
# 			print(num,char,'found!')
# 			break
# 		print(num,char)

# # Two break statements are required to exit out of a double loop:
# for num in nums:
# 	for char in string:
# 		if num == 3 and char == 'b':
# 			break
# 		print(num,char)
# 	if num == 3 and char == 'b':
# 		print(num,char,'found!')
# 		break

#-------------------------------------

# # For loops will loop over a predefined list of values.
# # While loops will continue until a condition is met:
# x = 0
# while x < 10:
# 	print(x)
# 	x += 1
# # Note that the loop will execute only if the condition is True

# # Example of a while loop with a break statement:
# x = 0
# while x <= 10:
# 	if x == 5:
# 		break
# 	print(x)
# 	x += 1

# # Example of an infinite loop with a break statement:
# x = 0
# while True:
# 	if x == 5:
# 		break
# 	print(x)
# 	x += 1
# # To stop an infinite loop you can use 'Ctrl-C' to terminate Python from a terminal
# # or use 'Ctrl-Alt-M' in VS Code