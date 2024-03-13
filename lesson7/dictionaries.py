# Dictionaries (Javascript objects)

band = {
    'vocals': 'plant',
    'guitar': 'page'
}

band2 = dict(vocals='plant', guitar='page')

# print(band2)
# print(band)
# print(type(band))
# print(type(band2))
# print(len(band2))

print(band['vocals'])
print(band.get('guitar'))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list all key/value paris as tuples
print(band.items())

# verify a key exists
print('guitar' in band)
print('triangle' in band)

# Change values in dictionaries
band['vocals'] = 'lol'
print(band)

band.update({'bass': 'JPJ'})
print(band)

# Remove items
print(band.pop('bass'))
print(band)

band['drums'] = 'Bonham'
print(band)

print(band.popitem())
print(band)

# Delete and clear
band['drums'] = 'Bonham'
del band['drums']
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries

# band2 = band # creates a reference
# print('Bad copy!')
# print(band2)
# print(band)
# band2['drums'] = 'JV'
# print(band)

# print('Good copy!')
band2 = band.copy()
band2['drums'] = 'JV'
print(band)
print(band2)

# or use the dict() contructor funciton
# print('Good copy!')
band3 = dict(band)
print(band3)

# Nested dictionaries
member1 = {
    'name': 'plant',
    'intrument': 'vocals'
}
member2 = {
    'name': 'page',
    'intrument': 'guitar'
}
band = {
    'member1': member1,
    'member2': member2
}
print(band)
print(band['member1']['name'])

# Sets
nums = { 1,2,3,4 }
nums2 = set((1,2,3,4))
print(nums2)
print(type(nums2))
print(len(nums))

# No duplicates allowed
nums = { 1,2,2,3 }
print(nums)

# True is a dupe of 1, False is a dupe of zero
nums = { 1, True, 2, False, 3, 4, 0 }
print(nums)

# Check if a value is in a set
print(2 in nums)
print(7 in nums)

# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
morenums = { 5, 6, 7 }
nums.update(morenums)
print(nums)
morenums.clear()
del morenums

# you can use update with lists, tuples, and dictionaries too.

# Merge two sets to create a new set
one = {1,2,3}
two = {5,6,7}
mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates
one = {1,2,3}
two = {2,3,7}

one.intersection_update(two)
print(one)

# Keep everything except the duplicates
one = {1,2,3}
two = {2,3,7}
one.symmetric_difference_update(two)
print(one)