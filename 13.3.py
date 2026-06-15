#dictionary

#creating a dictionary
dict1={"name":"aditi",
       "age":23,
       "city":"pune"}
print(dict1)
print(len(dict1)) #number of key-value pairs in the dictionary
print(dict1["name"]) #accessing value using key
print(dict1.get("age")) #accessing value using get() method


dict={"dict2":{"name":"aditi"},
      "dict3":{1:"hello"}
      }
print(dict["dict2"])#accessing nested dictionary
print(dict["dict3"][1])#accessing nested dictionary value using key