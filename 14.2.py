#example problem

marks=int(input("Enter your marks: "))
if (marks>=80):
    if(marks>=90):
        print("Top of the class")
    else:
        print("Grade A")
elif marks>=60:
    print("Grade B")
elif marks>=40:
    print("Grade C")
else:
    print("Grade D")