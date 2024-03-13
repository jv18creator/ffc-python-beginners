# While 

value = 1

# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print('Value is nonw equal to ' + str(value))

# For loop
names = ['JV', 'Dave', 'John']

# for name in names:
#     print(name)

# for string in 'Mississippi':
#     print(string)

# for x in names:
#     if x == 'Sarah':
#         break
#     print(x)

# for x in names:
#     if x == 'JV':
#         continue
#     print(x)

# for x in range(4):
#     print(x)

# for x in range(2, 4):
#     print(x)

for x in range(0, 101, 5):
    print(x)
else:
    print('Glad that\'s over')

actions = ['codes', 'eats', 'sleeps']

for action in actions:
    for name in names:
        print(name + '  ' + action + '.')