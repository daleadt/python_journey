#for loops
name="Vaishu"
for i  in name:
    print(i)


#using end parameter
for i in name:
    print(i,end=" ")


#example iterating over a tuple
t=(63,35,67,96,45)
for i in t:
    print(i)
    
cities=("Delhi","Mumbai","Chennai","Kolkata")
for x in cities:
    print(x)    


#iterating over a list
l=["adt","vira","sachin","dhoni"]
for x in l:
    print(x)


#iterating over a set
s={1,2,3,4,5}
for x in s:
    print(x)


#iterating over a dictionary
d={"name":"Vaishu","age":22,"city":"Delhi"}
print(d.items())

for key in d:
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)

for i,j in d.items():
    print(i,j)
