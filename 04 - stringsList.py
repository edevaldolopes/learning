txt1 = 'The best code'
list1 = ['one', 'two', 'three']

print(txt1)
print(list1)
print(txt1[0])
print(list1[0])

# slice
print(txt1[0:3])
print(list1[0:2])

# slice, step
print(list1[0:3:2])

# negative
print(list1[-1])

# add
list1.append('four')
list1.insert(0, 'zero')
print(list1)

# remove
list1.remove('one')
del list1[2]
print(list1)

# rename
list1[0] = 'one'
list1[1] = 'one'
list1[2] = 'one'
print(list1)

# count
print(list1.count('one'))

# text
print(len(txt1))
print(txt1.count('e'))
print(txt1.find('best'))
print(txt1.upper())
print(txt1.capitalize())

# test logic
print(txt1.islower())
print(txt1.isnumeric())