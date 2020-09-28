num1 = 1
num2 = 1

n = int(input())
print(num1, end=' ')
print(num2, end= ' ')
for i in range(1, n):
    num1,num2 = num2 , num1+ num2
    print(num2, end=' ')