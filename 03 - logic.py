var_true = True
number = 10
print(type(var_true))

# comparison
number = 3
print(number > 0)
print(number < 0)
print(number >= 0)
print(number <= 0)
print(number == 0)
print(number != 0)

# logic
if number == 1:
    print('is 1')
elif number == 2:
    print('is 2')
elif number == 3:
    print('is 3')
else:
    print('number invalid')

# in, not, is, is not, and, or
list1 = [1, 2, 3, 4, 5]
print(2 in list1)
print((not 2) in list1)
print(list1 is list1)
print(list1 is not list1)
print(1 and 2 and 4 in list1)
print((5 or 11) in list1)
