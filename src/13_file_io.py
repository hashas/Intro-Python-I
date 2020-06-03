"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open("foo.txt") as f:
	print(f.read())

# file1 = open("foo.txt", "r")
# print(file1.read())
# file1.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('bar.txt', 'w') as f:
	f.write("This is the first line of the file.\nThis is the second line of the file.\nThis is the third line of the file\n")
	
# file = open('bar.txt', 'w')
# file.write("This is the first line of the file.\nThis is the second line of the file.\nThis is the third line of the file\n")
# file.close()

with open('bar.txt', 'r') as f:
	print(f.read())

# file = open('bar.txt', 'r')
# print(file.read())
# file.close()