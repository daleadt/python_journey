# functions: are reusable pieces of code that perform a specific task.
# They help to break down complex problems into smaller, more manageable parts,
# and they can be called multiple times throughout a program.


def myfunction():
    print("first function")


myfunction()


# function with arguments: are values that are passed to a function when it is called.
# they allow you to provide input to a function, which can then be used to perform a
#  specific task or calculation.


def addition(a, b):
    c = a + b
    print(c)
    return c


addition(5, 6)
ans = addition

# default arguments: are values that are assigned to a function's parameters when the function
# is defined.These default values are used when the function is called without providing a value
# for that parameter.


def myfunction(age=18):
    print(age)


myfunction(20)
myfunction()


# value argument *args: allows a function to accept an arbitrary number of positional arguments.
# The *args syntax is used in the function definition to indicate that the function can accept
# any number of positional arguments, which are then passed to the function as a tuple.


# 1) with indexing
def myfunction(*arg):
    l = len(arg)

    for i in range(0, l):
        print(arg[i])


myfunction(10, 20, 56, 56, 46, 69)


# 2 without indexing
def myfunction(*arg):
    for i in arg:
        print(arg)


myfunction(10, 20, 78, 56, 0, 69)


# keyword arguments **kwargs: allows a function to accept an arbitrary number of keyword arguments.
# The **kwargs syntax is used in the function definition to indicate that the function can accept
# any number of keyword arguments, which are then passed to the function as a dictionary.
# example:cookies in chrome are stored in a key value pair


def myfunction(**kwargs):
    for i, j in kwargs.items():
        print(i, j)


myfunction(name="john", age=30, city="new york")
