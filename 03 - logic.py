var_true = True
number = 10
print(type(var_true))

# comparison
number = 11
print(number > 0)
print(number < 0)
print(number >= 0)
print(number <= 0)
print(number == 0)
print(number != 0)
print(number is False)
print(number is True)
print(number is not True)
print(number is not False)

# logic
if number > 0:
    print('Your is best!!!')
else:
    print('No is best!!!')

if not number <= 0 and number < 3:
    print('Fail')
elif 3 < number < 7:
    print('Good')
elif 7 < number < 10:
    print('Best')
else:
    print('Number invalid')
