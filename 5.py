# list is a collection which is ordered and changeable. Allows duplicate members.

l1 = [1, 2, 3]
l2 = list()
l3 = ["xyz", "farhan", "python"]
l5 = [12, 4.5, 64, 7.6]

print(l1)
l = len(l1)
for i in range(0, 3):
    print(l1[i])


# tuple() : is a collection which is ordered and unchangeable. Allows duplicate members.

T = tuple()
T1 = (1, 2, 3, 4, 5)
print(T1[1:2])
print(T1[3])


# dictionary : is a collection which is unordered, changeable and indexed. No duplicate members.

d = dict()
d = {"name": "aditi", "age": 22, "roll_n0": 305}
print(d)

for i, j in d.items():
    print(i, j)


# set : is a collection which is unordered and unindexed. No duplicate members.

s1 = {1, 2, 3, 4, 5}
print(s1)
s2 = {4, 5, 6, 7, 8}
print(s1 | s2)  # union
print(s1 & s2)  # intersection
print(s1 - s2)  # difference
print(s1 ^ s2)  # symmetric difference

s3 = {
    1,
    1,
    2,
    3,
    4,
    4,
    5,
    6,
    6,
    6,
}
print(s3)  # duplicate values are not allowed in set
