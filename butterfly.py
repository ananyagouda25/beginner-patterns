# Program: Makes a butterfly pattern of stars
num = int(input("Enter a number:"))
for i in range(1,num+1):
    print("*"*i+" "*(2*(num-i))+"*"*i)
for k in range(num-1,0,-1):
    print("*"*k+" "*(2*(num-k))+"*"*k)
