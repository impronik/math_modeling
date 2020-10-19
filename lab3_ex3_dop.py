import numpy as np
l = int(input('Введите длину масcива'))
h = int(input('Введите высоту масcива'))
array1= np.zeros((h,l))

array2 = np.zeros((l,h))
for (i,j),x in np.ndenumerate(array1):
    num = int(input(f'[{i},{j}] = '))
    array1[(i,j)] = num
    array2[(j ,i)] = num
    
array3 = np.zeros(l)
for i, x in np.ndenumerate(array3):
    array3[i]= array2[i].max()


print('\narray1',array1)
print('\narray2',array2)
print('\narray3',array3)