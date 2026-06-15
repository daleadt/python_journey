#sets
a={1,2,3,4,4,5,5,6}
print(a)
print(type(a))


#creating an empty set
setA=set()
print(setA)
print(type(setA))


#creating set with a string
#since a string is iterable this will successfully create a set with the characters of the string as elements
setA=set("python")
print(setA)


#creating a set with a list
setA=set(["c","c++","java","python"])
print(setA)


myString="hello world"
setA=set(myString)
print(setA)