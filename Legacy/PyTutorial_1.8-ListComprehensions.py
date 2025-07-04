# PyTutorial 1.8 - List Comprehensions

# # In Python, there are several ways to generate lists.
# # We can generate a list using a for loop.
# # For example, here we create an empty list 'my_list' and fill it with
# # elements equal to '2*n' for each 'n' in the existing list 'nums':
# nums = [1,2,3,4,5,6,7,8,9,10]
# my_list = []
# for n in nums:
# 	my_list.append(2*n)
# print(my_list)

#-------------------------------------

# # A list comprehension is a much simpler and elegant way to create a list.
# # We can achieve the same result as above using one line of code:
# nums = [1,2,3,4,5,6,7,8,9,10]
# my_list = [2*n for n in nums]
# print(my_list)

#-------------------------------------

# # Note that if we simply multiply new_list by 2, this does not achieve the same result:
# nums = [1,2,3,4,5,6,7,8,9,10]
# my_list = 2*nums
# print(my_list)
# # This is because multiplying a list by an integer 'm' simply concatenates that list with itself 'm' times.
# # If we try to multiply by a float, we get an error because floating-point multiplication is not defined for lists.
# # TypeError: can't multiply sequence by non-int of type 'float'
# # However, we can do this with numpy arrays, as we'll see later.

#-------------------------------------

# # Here's a slightly more complicated example with a for loop.
# # Suppose we want my_list to contain 'n*n' for each 'n' in 'nums'
# # but only if 'n' is even:
# nums = [1,2,3,4,5,6,7,8,9,10]
# my_list = []
# for n in nums:
# 	if n % 2 == 0:
# 		my_list.append(n*n)
# print(my_list)

#-------------------------------------

# # Here the same example with a list comprehension:
# nums = [1,2,3,4,5,6,7,8,9,10]
# my_list = [n*n for n in nums if n%2 == 0]
# print(my_list)

#-------------------------------------

# # Suppose we want a (letter,num) pair for each letter in 'abcd' and each number in '0123':
# my_list = []
# for letter in 'abcd':
# 	for num in range(4):
# 		my_list.append((letter,num))
# print(my_list)

#-------------------------------------

# # With a list comprehension:
# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)

#-------------------------------------

# # Suppose we want a dictionary with the format {'name':'hero'}:
# # That is, each name is a key and each hero is the corresponding value.
# # Here, we use zip(names,heroes), which transposes the two lists and returns a list of tuples.
# names = ['Bruce','Clark','Peter','Logan','Wade']
# heroes = ['Batman','Superman','Spiderman','Wolverine','Deadpool']
# my_dict = {}
# for name, hero in zip(names,heroes):
# 	my_dict[name] = hero
# print(my_dict)

#-------------------------------------

# # We can also do comprehensions with dictionaries (dictionary comprehensions):
# names = ['Bruce','Clark','Peter','Logan','Wade']
# heroes = ['Batman','Superman','Spiderman','Wolverine','Deadpool']
# my_dict = {name: hero for name, hero in zip(names,heroes)}
# print(my_dict)

#-------------------------------------

# # Here is the same example with the condition: if 'name' not equal to 'Peter'
# names = ['Bruce','Clark','Peter','Logan','Wade']
# heroes = ['Batman','Superman','Spiderman','Wolverine','Deadpool']
# my_dict = {name: hero for name, hero in zip(names,heroes) if name != 'Peter'}
# print(my_dict)
# Note the use of curly brackets and colons for dictionary comprehensions!

#-------------------------------------

# # Here's an example of creating a set with a for loop:
# nums = [1,1,2,3,1,4,5,4,6,6,7,8,2,8,9,10,10]
# my_set = set()
# for n in nums:
# 	my_set.add(n)
# print(my_set)

#-------------------------------------

# # We can also use a set comprehensions
# nums = [1,1,2,3,1,4,5,4,6,6,7,8,2,8,9,10,10]
# my_set = {n for n in nums}
# print(my_set)
# # Note the use of curly brackets for set comprehensions!
