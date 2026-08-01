# Program: Palindrome check. (uses lambda function. could be simpler tho.. hehe)
a = input("Enter input:")
pal = lambda x: x[::-1]
if pal(a)==a:
  print("palindrome")
else:
  print("not a palindrome")
