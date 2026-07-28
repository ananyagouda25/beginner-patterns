#Program: Hollow right triangle
num = int(input("Enter a number:"))
if num == 1:
    print("*")
else:
    print("*")
    for i in range(0,num-2):
        print("*"+" "*(i)+"*")
    print("*"*num)
