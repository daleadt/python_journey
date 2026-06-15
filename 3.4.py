a = int(input("enter first number:"))
b = int(input("enter second number:"))

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a**b)

if a == b:
    print("a is equal to b")
if a != b:
    print("a is not equal to b")
if a < b:
    print("a is less than b")
if a > b:
    print("a is more than b")
if a <= b:
    print("a is less than or equal to b")
if a >= b:
    print("a is more than or equal to b")

if a and b:
    print("true")
else:
    print("false")

if a or b:
    print("true")
else:
    print("false")

if not a:
    print("value")


print(f"Addition of {a} and {b} is {a+b}")
print(f"Subtraction of {a} and {b} is {a-b}")
print(f"Multiplication of {a} and {b} is {a*b}")
print(f"Division of {a} and {b} is {a/b}")
print(f"Floor division of {a} and {b} is {a//b}")
print(f"Modulus of {a} and {b} is {a%b}")
print(f"Exponentiation of {a} and {b} is {a**b}")

print(f"Is {a} equal to {b} : {a==b}")
print(f"Is {a} not equal to {b} : {a!=b}")
print(f"Is {a} less than {b} : {a<b}")
print(f"Is {a} more than {b} : {a>b}")
print(f"Is {a} less than or equal to {b} : {a<=b}")
print(f"Is {a} more than or equal to {b} : {a>=b}")

print(f"Logical AND of {a} and {b} is : {a and b}")
print(f"Logical OR of {a} and {b} is : {a or b}")
print(f"Logical NOT of {a} is : {not a}")
