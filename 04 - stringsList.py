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

# remove
list1.remove('one')
del list1[2]
print(list1)

