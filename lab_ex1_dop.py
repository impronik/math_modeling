a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

d = b**2 - 4*a*c
if (d < 0):
    print("нет действительных корней")
else:
    x1 = (-b + d**(0.5)) / (2*a)
    x2 = (-b - d**(0.5)) / (2*a)
    if (d == 0):
        print("один корень X =", x1)
    else:
        print("два корня \n\tX1 =", x1, "\n\tX2 =", x2)