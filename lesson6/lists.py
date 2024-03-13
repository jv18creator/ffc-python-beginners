users = ['Dave', 'JV', 'Vani']

data = ['JV', 22, True]

emptylist = []

# print('Vani' in emptylist)

# print(users[1])
# print(users[-1])

# users.extend(['JV'])
# print(users)

users.insert(0, 'LOL')

users[2:2] = ['Eddie', 'Alex']
print(users)

users[1:3] = ['Robert', 'Kishan']
print(users)

users.remove('Robert')
print(users)

users.pop()
print(users)

del users[0]
print(users)

data.clear()
print(data)

users[1:2] = ['dave']
print(users)

users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

nums.sort()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(type(nums))

# Tubles
mytuple = tuple(('JKV', 22, True))

anothertuple = (1,4,2,9, 2)
print(type(mytuple))
print(anothertuple)

newlist = list(mytuple)
newlist.append('Neil')
print(newlist)

newtuple = tuple(newlist)
print(newtuple)

(one, *two) = anothertuple
print(one)
print(two)

print(anothertuple.count(2))