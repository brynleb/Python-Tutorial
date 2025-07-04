# PyTutorial 2.2 - File Objects

# # In Python, we can create a file object using the built-in 'open' command.
# # To open a file for reading:
# f = open('Test.txt','r')
# # Here the file 'Test.txt' is located in the same directory as this script.
# # Note the 'r' indicates we want to open the file 'reading' only (this is the default if not specified).
# # We can also open a file for writing ('w'), appending ('a'), or reading and writing ('r+').
# # Note also that when opening a file manually this way, we must also close it explicitly with the 'close' method.

# # To get the file name:
# print(f.name)
# # To get the mode the file was opened with:
# print(f.mode)
# # To read the entire contents of the file:
# print(f.read())
# # To get the open/closed state:
# print(f.closed)

# # To close the file:
# f.close()
# # This is required when directly using the open command without a 'context manager' in order to avoid memory leaks.

# print(f.closed)

#-------------------------------------

# # In Python, it's better to open a file using a context manager using the 'with' keyword.
# # This automatically closes the file at the end, avoiding possible memory leaks.
# with open('Test.txt','r') as f:
# 	pass

# # We can verify that the file has been closed:
# print(f.closed)
# # We still have access to the file object's info:
# print(f.name)
# # But not the contents:
# print(f.read())

#-------------------------------------

# # From within the context manager, we can access file contents in different ways:.
# with open('Test.txt','r') as f:
	# # Using the 'read()' method returns all the contents as a string:
	# f_contents = f.read()
	# print(f_contents, end='')

	# # The 'readlines()' method returns a list of each line within the file:
	# f_contents = f.readlines()
	# print(f_contents, end='')

	# # The 'readline()' method returns a single line:
	# f_contents = f.readline()
	# print(f_contents, end='')

	# # Each time we execute 'readline()', it goes to the next line in the file:
	# f_contents = f.readline()
	# print(f_contents, end='')

	# # We can also loop over each line with a for loop:
	# for line in f:
	# 	print(line, end='')
	# # Note that this method is more efficient than loading in the entire file contexts all at once,
	# # which can lead to memory issues for very large files. Here, we are reading in one line at a time
	# # and performing an operation on each line (printing it to the screen).

	# # Using the 'read()' method, we can also specify the characters we want to read at a time:
	# num_chars = 50
	# f_contents = f.read(num_chars)
	# print(f_contents, end='*') # The '*' character here illustrates the position where read ends.
	# # Each time 'read' is executed on the same file object, it resumes where the previous read finished: 
	# f_contents = f.read(num_chars)
	# print(f_contents, end='*')
	# # If it reaches the end of the file, 'read' returns an empty string:
	# f_contents = f.read(num_chars)
	# print(f_contents, end='*')

	# # The following loop reads the entire file 10 characters at a time:
	# num_chars = 10
	# f_contents = f.read(num_chars)
	# while len(f_contents) > 0:
	# 	print(f_contents,end='*')
	# 	f_contents = f.read(num_chars)

	# Use the 'tell()' method to get the current character position in the file:
	# f_contents = f.read(20)
	# print(f.tell())

	# Use the 'seek' method to change read position:
	# print(f.read(10))
	# f.seek(0)
	# print(f.read(10))
	# f.seek(22)
	# print(f.read(10))

#-------------------------------------

# # To write to files, they must be opened in write mode 'w' :
# with open('Test2.txt','w') as f:
# # If the file does not exist, this operation creates a new file
# # If the file does exist, this operation overwrites the file
# # Use 'a' instead of 'w' to append to an existing file

# 	# Use the 'write()' method to write text to the file:
# 	f.write('This is some text.')
# 	# Opening the file in a text editor, you should see this string written at the beginning of the file.
# 	f.write('Some more text...')
# 	# Calling 'write', Python will pick up where the previous write finished. 

# 	# The 'seek' method can also be used to change the write position:
# 	f.seek(0)
# 	f.write('Even more text.')
# 	# However, this will result in overwriting only a portion of the existing text
# 	# since this string has fewer characters than already in the file.

#-------------------------------------

# # Attempting to use the 'read' method on a file opened in write mode will cause an error.
# # To both read and write to the same file, open it in update mode using 'r+' (no file truncation).
# # The mode 'w+' will also work, but the file's contents will initially be truncated.
# with open('Test.txt','r+') as f:
# 	f_contents = f.read()
# 	print(f_contents, end='\n')
# 	f.write('11) Eleventh line\n')
# 	f.seek(0)
# 	f_contents = f.read()
# 	print(f_contents)

#-------------------------------------

# # The following example makes a copy of 'Test.txt' in a new file called 'Test_copy.txt'
# # Here, we open 'Test.txt' in read mode and 'Test_copy.txt' in write mode.
# # For each line in 'Test.txt', we write the same line to 'Test_copy.txt'.
# with open('Test.txt','r') as rf:
# 	with open('Test_copy.txt','w') as wf:
# 		for line in rf:
# 			wf.write(line)
