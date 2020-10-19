import numpy as np
print('Введите значения для массива:')
array1= np.zeros((3, 3))

for i, x in np.ndenumerate(array1):
    array1[i] =input(f'{i} = ')
print("массив:\t", array1)

print('Введите значения для массива2:')
array2= np.zeros((3, 3))
array3 = np.zeros((3,3))
for i, x in np.ndenumerate(array2):
    array2[i] =input(f'{i} = ')
    if (array1[i] >= array2[i]):
        array3[i] = array1[i]
    else:
        array3[i] = array2[i]
print("массив2:\t", array2)

print('\narray3:\n', array3)
