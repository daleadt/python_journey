#examples
#write a program to take input from user and check whether the string is starting with a vowel or not.

a=input("Enter your word/sentence: ")
l=["a","e","i","o","u","A","E","I","O","U"]
if a[0] in l:
    print("string starts with a vowel")
else:
    print("string does not start with a vowel")