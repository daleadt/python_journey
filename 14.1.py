#nested if statements


num=0 #outer if statement
if (num>=0):
    #inner if statement
    if num==0:
        print("number is zero")
    #inner else statement
    else:
        print("number is positive")
#outer else statement
else:
    print("number is negative")