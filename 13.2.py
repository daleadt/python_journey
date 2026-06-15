#union Intersection Difference in sets

setA={1,2,3,4,5}
setB={2,3,4,5,6}
set_union=setA.union(setB) #returns a new set that contains all the elements from both sets, without duplicates.
print(set_union)

set_intersection=setA.intersection(setB) #returns a new set that contains only the elements that are present in both sets.  
print(set_intersection)

set_difference=setA.difference(setB) #returns a new set that contains the elements that are present in the first set but not in the second set.
print(set_difference)