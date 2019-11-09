'''
This file shows basic examples of decorators in Python
'''

# Simply put, a decorator is a function that accepts a function as its
# argument, and returns another function. Typically the function that is
# returned is a warpper around the one that was passed in as an argument

# Consider this simple echo function
def echo(phrase):
    return phrase
# echo("Hello world!") -> "Hello world!"

# Here's a simple decorators. It can be used on any function that returns a
# string, and it makes it so that the string that is returned is all uppercase
def upper(func):
    def wrapper(x):
        return func(x).upper()
    return wrapper

# Here's how you could use the decorator:
@upper
def make_upper(phrase):
    return phrase
# The @ symbol, followed by the name of the decorator, followed by the
# definition of the function being decorated

# It's worth noting that decorating functions isn't anything beyond syntactic
# sugar. The same can be accomplished by doing the following:

# def make_upper(phrase):
#     return phrase
# make_upper = upper(echo_caps)


# You can also make decorators which accept arguments as follows:
def set_case(case):
    def decorator(func):
        def wrapper(x):
            if case == 'upper':
                return func(x).upper()
            elif case == 'lower':
                return func(x).lower()
            elif case == 'title':
                return func(x).title()
            else:
                return func(x)
        return wrapper
    return decorator
# In this case you make a function that returns a function that itself takes a
# function

@set_case('lower')
def make_lower(phrase):
    return phrase
# make_lower("Hello world!") -> "hello world!"

@set_case('title')
def make_title(phrase):
    return phrase
# make_title("Hello world!") -> "Hello World!"


# Decorators can be used for all sorts of useful things. Typically they're
# used for when you want to provide some reusable composable way of wrapping
# functions such that something happens before/after they execute.

# The Python standard library comes with several decorators. Here are some of
# the more noteworthy ones:
# - @property:
#     The property decorator can be applied to zero-argument methods within a
#     class to make them accessible as if they were a property
# - @functools.lru_cache:
#     This decorator provides a cache for your function. If your function is
#     called again with the same arguments, then instead of being run again,
#     the cached value with be returned instead. It is very useful for some
#     recursive functions.
# - @functools.wraps:
#     This should be used whenever you create a decorator in order to preserve
#     the docstring (and other metadata) of the function that is being wrapped.

