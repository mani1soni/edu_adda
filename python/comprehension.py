'''
This file shows basic examples of comprehension in Python
'''

## List Comprehension:
# List comprehensions are a looping construct in Python that is an expression
# rather than a statement. Instead of making a list of squared numbers like so:
squared_list = []
for x in range(10):
    squared_list.append(x**2)
# You could write it as a list comprehension like this:
squared_list = [x**2 for x in range(10)]


## Set Comprehension:
# Set comprehensions work exactly the same as list comprehensions, but a set
# is built instead of a list. So instead of this:
squared_set = set()
for x in range(10):
    squared_set.add(x)
# You could write it as a set comprehension like this:
squared_set = {x**2 for x in range(10)}
# Note the curly brackets being used instead of the square brackets

## Generator Comprehension:
# A generator comprehension has a similar syntax as the examples above, but
# instead of using curly brackets or square brackets, parenthesis are used:
squared_generator = (x**2 for x in range(10000000000000000000000000000000000))
# Because this creates a generator instead of a list/set, values are only
# produced as they are needed, it can only be iterated over once, it supports
# infinite sequences, and it does not support random access.


## Tuple Comprehension:
# Tuple comprehension doesn't exist in Python, as the syntax to create tuple
# literals is already being used by generator comprehension. You can, however,
# efficiently create a tuple with a generator comprehension by calling the
# tuple constructor on it as follows:
squared_tuple = tuple(x**2 for x in range(10))

## Dictionary Comprehension:
# Dictionary comprehension looks like set comprehension because it also uses
# curly brackets, but the difference it it also has a key for each value:
squared_dict = {x:x**2 for x in range(10)}
# This creates a dictionary which maps each value in range(10) to that value
# squared. The non-comprehension way of doing this would be like so:
squared_dict = {}
for x in range(10):
    squared_dict[x] = x**2


# Here are the values defined in this tutorial printed out:
# >>> squared_list
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# >>> squared_set
# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
# >>> squared_generator
# <generator object <genexpr> at 0x7fe6b9a481a8>
# >>> squared_tuple
# (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
# >>> squared_dict
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# Note that the order of squared_set is not guaranteed, and the address of the
# generator expression will also (likely) be different for you.

