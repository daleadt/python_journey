# file handling in python


file = open("newfile.txt", "w")  # write in new created file
file.write("my name is aditi")


file = open("newfile.csv", "w")  # write in new created file
file.write("my name is vira")


file = open("tested.csv", "r")  # read the existing file
for i in file:
    print(i)


file = open("tested.csv", "a")  # apppend is used to add data in the existing file
file.write("my name is aditi")
