# Program: Floyd's triangle
rows = int(input("Enter the number of rows:"))
lastnum = 1
for i in range (1,rows+1):
    for j in range(1,i+1):
      print(lastnum,end=" ")
      lastnum += 1
    print()
