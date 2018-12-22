# Use open to open file "foo.txt" for reading

foo = open('foo.txt', 'r')

# Print all the lines in the file
print(foo.read())

# Close the file
foo.close()

# Use open to open file "bar.txt" for writing
bar = open('bar.txt', 'w')

# Use the write() method to write three lines to the file
bar.write('''"To be, or not to be, that is the question:
Whether 'tis nobler to suffer the sling and arrows of outrageous fortune..."
 --Hamlet
''')

# Close the file
bar.close()