n = int(input())

num = 0
i = 1
while (True):
    i += 1
    num = 2**(i - 1) * (2**i - 1)
    if (num < n):
        print(num)
    else:
        break