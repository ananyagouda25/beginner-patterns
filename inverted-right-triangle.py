# Program: Inverted right triangle using stars
rows = int(input("Enter the number of rows:"))
for i in range(0,rows+1):
  print("*" * (rows-i))
