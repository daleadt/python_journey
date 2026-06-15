# linear search


def linear_search(l1, t):
    for i in range(len(l1)):
        if l1[i] == t:
            return i
    return -1


l1 = [1, 2, 3, 4, 5]
print(linear_search(l1, 3))
