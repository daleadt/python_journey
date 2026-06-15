#in-built functions 
dict1={"name":"vira",
       "age":25,
       "gender":"female",
       "marks":110}



#len()
print(len(dict1))
  

#dict()
d=[("a",10),("b",11),("c",12)]
dict2=dict(d)
print(dict2)


#keys()
print(dict1.keys())


#values()
print(dict1.values())


#items()
print(dict1.items())


#get()
print(dict1.get("marks"))


#update()
dict1={"name":"aditi",
       "age":22}
print(dict1)


#del
del dict1["age"]
print(dict1)


#clear
dict1.clear()
print(dict1)