# PyTutorial 2.1 - Using the OS module

# # The OS module always us to interact with the underlying operation system is seveval ways.
# # It can be used to navigate the file system, get file information,
# # create/move/delete files and folders, change environment variables, etc.

# # To access the OS module, it must be imported:
# import os

#-------------------------------------

# # To get the current working directory (cwd):
# print(os.getcwd())

# ## To change the directory:
# os.chdir('c:\\')
# print(os.getcwd())

# Lets change the directory to a new one relative to the cwd
# cwd = os.getcwd()
# os.chdir(cwd + '\\Teaching\\PHYS4332\\Python Tutorial\\')

#-------------------------------------

# To list the contents of a directory:
# print(os.getcwd())
# print(os.listdir())

#-------------------------------------

# To create a new directory within the cwd:
# os.mkdir('Example-Dir')
# print(os.listdir())
# Note that the 'mkdir' method can create only a single directory level.

# # Alternatively, the 'makedirs' method creates all directory sub levels.
# os.makedirs('Example-Dir\\Sub-Dir', exist_ok=True)
# print(os.listdir())

#-------------------------------------

# # To remove directories:
# os.rmdir('Example-Dir\\Sub-Dir')
# print(os.listdir())
# # Note that 'rmdir' will only remove the specified directory if it has no sub-directories.

# # Alternatively, 'removedirs' will remove the leaf directory and all intermediate ones:
# os.removedirs('Example-Dir\\Sub-Dir')
# print(os.listdir())

#-------------------------------------

# To rename a file:
# cwd = os.getcwd()
# os.chdir(cwd + '\\Teaching\\PHYS4332\\Python Tutorial\\')
# os.rename('Demo.txt', 'Test.txt')
# print(os.listdir())

#-------------------------------------

# # To join several paths together, use the 'join' method of os.path.
# # This function automatically accounts for the presence or absence of slashes,
# # and returns the path of the new file or folder.
# # This example creates a path to new directory called 'Example-Dir' in the cwd
# new_dir = os.path.join(os.getcwd(), 'Example-Dir')
# print(new_dir)

# # This example creates a new file path called 'Test.txt' in new_dir:
# new_file = os.path.join(new_dir, 'Test.txt')
# print(new_file)

#-------------------------------------

# # To check if a path exists, and if it corresponds to a file or directory:
# new_dir = os.path.join(os.getcwd(), 'Example-Dir')
# new_file = os.path.join(new_dir, 'Test.txt')
# os.mkdir(new_dir)

# print(os.path.exists(new_dir))
# print(os.path.isdir(new_dir))
# print(os.path.isfile(new_dir))

# os.rmdir(new_dir)

#-------------------------------------

# # Some useful methods for getting the path directory name, basename, filename and file extension:
# path = 'Example-Dir\\Test.txt'
# print(os.path.dirname(path))
# print(os.path.basename(path))
# print(os.path.split(path))
# print(os.path.splitext(path))
