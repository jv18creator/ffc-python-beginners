sqaured = lambda num: num * num

print(sqaured(2))

sum_total = lambda a, b: a + b

print(sum_total(1, 2))


def func_builder(x):
    return lambda num: num + x


addTen = func_builder(10)
addTwenty = func_builder(20)

print(addTen(7))

print(addTwenty(2))


numbers = [1, 7, 11, 76, 9]

squared_numbers = map(
    lambda num: num * num, numbers
)  ## map is a higher order built in function which takes a function in this case lambda

print(list(squared_numbers))

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))


from functools import reduce

total = reduce(lambda acc, curr: acc + curr, numbers, 6)
print(total)


print(sum(numbers, 6))


names = ["Jeet", "Sarah", "Darling"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
