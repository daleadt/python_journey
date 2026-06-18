# for loop

#range
for i in range(0,8):
    print(i)
    
#even number
for i in range(0,8,2):
    print(i)
    
for i in range(6):
    print(i)
    
#odd number
for i in range(1,10,2):
    print(i)
    
#print reverse numbers
for i in range(10,0,-1):
    print(i)
    
#print reverse string
s="hello"
for i in range(len(s)-1,-1,-1):
    print(s[i])
    
string="python"
#slicing
print(string[::-1])

rev =""                        #empty string initialization
for char in string:
    print(char)                #taking first character and adding to rev
    rev = char + rev           #taking second character and adding to rev
print(rev)

