a = int(input())
b = int(input())
c = int(input())

if (a < b + c) and (b < a + c) and (c < a + b):
    print('существует')
    if (a == b == c):
        print('равносторонний')
    elif (a == b) or (b == c) or (c == a):
        print('равнобедренный.')
    elif (a**2 == b**2 + c**2) or (b**2 == c**2 + a**2) or (c**2 == b**2 + a**2):
        print('прямоугольный')
    else:
        print('разн')
else:
    print('не существует')