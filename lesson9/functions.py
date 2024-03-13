# def hello_mom():
#     print('Hello mom!')

# hello_mom()

# def sum(num1, num2):
#     print(num1 + num2)

# sum(1, 2)

# def sum(num1 = 0, num2 = 0):
#     if type(num1) != int or type(num2) != int:
#         return 0
#     return num1 + num2

# total = sum()
# print(total)

# def multiple_items(*args):
#     print(type(args))
#     print('args: ', args)
#     count = 1
#     for x in args:
#         count *= x
#         print(count)

# multiple_items(2, 3, 4, 5)

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = 'Dave', last = 'Grat')
