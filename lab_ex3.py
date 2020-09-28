year= int(input())
if (year% 4 ==0) or (year % 100 ==0) or (year %400 ==0):
    print('Visokosnii')
else:
    print('ne visokosnii')