a = int(input())
b = int(input())
if (b==0):
    print('lol')
elif (a % b == 0):
    print('kek, bez ostatka')
else:
    print('ostatok = ' , a % b , sep = '')
    print('chastnoe =' , a / b , sep = '' )
    