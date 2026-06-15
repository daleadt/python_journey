import numpy as np

print(np.zeros((3, 3)))
print(np.ones((3, 3)))


# series

a = np.array([1, 2, 3, 4, 5])
print(a)


# dataframe

b = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(b)


c = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(c)


# indexing


print(a[0])  # single element retrieval
print(b[1, 1])

print(b[2:3])  # row retrieval
print(b[:, 2:3])  # column retrieval
print(b[0, 0], b[1, 1], b[2, 2])
