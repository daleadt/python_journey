#add update and delete in set

setA={1,2,3,4,5,6,7,7,8}
setA.add(9) #single element
print(setA)

setA.add((9,10))   #adding a tuple as an element to the set
print(setA)

setA.update([11,12,13]) #adding multiple elements to the set using a list
print(setA)

setA.update([11,12,13],{14,15}) #adding multiple elements to the set using a list and a set
print(setA)

my_set={1,2,3,4,5}
my_set.remove(3)#removes the specified element from the set. If the element is not found, it raises a KeyError.
print(my_set)

my_set.discard(4)#removes the specified element from the set. If the element is not found,
                 #it does nothing (no error) is raised).    
print(my_set)