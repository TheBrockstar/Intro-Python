# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

def f1(q, w):
    return q + w

print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and prints the
# sum. Google for "python arbitrary arguments" and look for "*args"

def f2(*v):
    e = 0
    for c in v:
        e = e + c
    return e

print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# What thing do you have to add to make this work? ANSWER: Add an asterisk!
print(f2(*a))    # Should print 22

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments. Google "python default arguments" for a hint.

# Old Version (Not Using Default Arguments)
# def f3(*purple):
#     if len(purple) == 1:
#         return purple[0] + 1
#     else:
#         if len(purple) == 2:
#             return purple[0] + purple[1]
#         else:
#             return f'Error: Invalid number of arguments: {len(purple)}. must be 1 or 2.'

# Using Default Arguments... Restricted to Only Two Arguments
def f3(a, b = 1):
    return a + b

print(f3(1, 2))     # Should print 3
print(f3(8))        # Should print 9

# Extra tests for old version
# print(f3(1, 2, 7))  # Should print an error
# print(f3())         # Should print an error


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints ouf the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Google "python keyword arguments".

def f4(**wunder):
    for key, value in wunder.items():
        print(f'key: {key}, value: {value}')

# Should print
# key: a, value: 12
# key: b, value: 30
f4(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# What thing do you have to add to make this work? ANSWER: Add double asterisks!
f4(**d)