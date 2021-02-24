# no arguments
def dell():
    print('My func() no arguments')


# with arguments
def media(n1, n2, n3):
    m1 = (n1 + n2 + n3) / 3
    return m1


l1 = [10, 2, 5]


# small number in list
def smaller(n1):
    min(n1)
    return min(n1)


# big number in list
def bigger(n1):
    max(n1)
    return max(n1)


print(smaller(l1))
print(bigger(l1))
