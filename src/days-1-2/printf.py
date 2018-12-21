x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('x is %d, y is %.2f, z is "%s"' % (x, y, z))

# Use the 'format' string method to print the same thing
print('x is {0}, y is {1:.3}, z is "{2}"'.format(x, y, z)) # Manual
print('x is {}, y is {:.3}, z is "{}"'.format(x, y, z)) # Automatic

# Finally, print the same thing using an f-string
print(f'x is {x}, y is {y:.3}, z is "{z}"')