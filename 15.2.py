student_marks={
    "harry": 20,
    "rohan": 78,    
    "hammad": 99,
    "aakash": 95
}

print(student_marks.items())


input=input("enter the name of the student: ")
for  name,values in student_marks.items():
    if name==input:
        if values>40:
            print(name,"pass")
        else:
            print(name,"fail")



for value in student_marks.values():
    if value > 40:
        print("pass")
    else:
        print("fail")