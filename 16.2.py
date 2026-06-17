#examples
#write a program to take input from user and check whether the string is starting with a vowel or not.

a=input("Enter your word/sentence: ")

if a[0] in "aeiouAEIOU":
    print("string starts with a vowel")
else:
    print("string does not start with a vowel")