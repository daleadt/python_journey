#add update and membership operators in a dictionary


dict={"name":"Aditi",
      "age":23,
      "marks":100,
      "talent":"polymath"}

dict["jerseyno"]=22 #add new item
print(dict)

dict['age']=25 #update item
print(dict)

# check using membership operator
print('talent'in dict)