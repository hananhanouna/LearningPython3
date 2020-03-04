# Python uses snake_case format

# hardcoded

# parameters
# arguments

# local scope


def sum_of_two_values(num1, num2):
    # num1 and num2 are local scope
    return num1 + num2


# total is a global scope
total = sum_of_two_values(3, 10)


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
    return 'Finished'


# a = print_lyrics()
#
# print(a)


# create three functions to do minus, multiple and divide two numbers
# call the functions and assigned the returned values to a variable
# print the variable
