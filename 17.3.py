#example
#print even and odd numbers in a list

list1=[1,2,3,4,5,6,7,8,9,10]
odd_numbers=[i for i in list1 if i%2!=0]
even_numbers=[i for i in list1 if i%2==0]

print("odd numbers in list are:",odd_numbers)
print("even numbers in list are:",even_numbers)