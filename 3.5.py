# if else elif condition and loops
# academic results code
marks = int(input("Enter your marks:"))

if marks > 35:
    print("pass")
elif marks > 75 and marks <= 100:
    print("distinction")
else:
    print("fail")


# voting eligibility code
votingage = int(input("Enter your age:"))
if votingage >= 20 and votingage <= 40:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")
