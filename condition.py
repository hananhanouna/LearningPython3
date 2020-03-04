x = 3
y = 2


# # if statement
# if x == y:
#     print('x is equal to y')
#
# # if else statement
# if x == y:
#     print('x is equal to y')
# else:
#     print('x is not equal to y')
#
# # chaining condition (if else statement)
# if x == y:
#     print('x is equal to y')
# elif x > y:
#     print('x is greater than y')
# else:
#     print('x is less than y')
#
# # nested condition (nested if else statement)
# if x == y:
#     print('x is equal to y')
# else:
#     if x > y:
#         print('x is greater than y')
#     else:
#         print('x is less than y')


# DRY concept (Don't Repeat Yourself)

def divide_two_values(num1, num2):
    if num2 == 0:
        return 'You can not divide by zero'
    return num1 / num2


total = divide_two_values(3, 0)


# print(total)


def log_me_in(username):
    # todo
    # Call to the database to get user's role and based on the role you will either be allowed to access the page or not
    if username == 'Hussein':
        print('Welcome, {usr}!'.format(usr=username))
    else:
        print('You do not have access')


log_me_in('Hussein')



# Create a function to return price of a given car