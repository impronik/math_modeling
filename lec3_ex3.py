import numpy as np
a = [1, 6, 10]
b = np.array(a)

print(type(a))
print(type(b))

print (b*b)
print (b-b)
print (b+b)
print (b/b)

c = np.ones((3, 2))
print(c)
img = np.ndarray(shape=(10, 10))
for i in range(1, 9):
    img[5,i]=10
    print(img)