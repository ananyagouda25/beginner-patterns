# Program: Hollow square
num = int(input("Enter a number:"))
if num==1:
    print("*")
else:
    print("*"*num)
    for _ in range(num-2):
        print("*"+" "*(num-2)+"*")
    print("*"*num)
