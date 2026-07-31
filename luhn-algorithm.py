# Program: Luhn's algorithm (only supports 14 and 16 digit card numbers)
def card_check():
    if (len(stack)<14 or len(stack)>16):
        print("Enter valid card number")
        return
print("This program checks if the entered card number is valid or not.")
card = int(input("Enter your card number:"))
cardnum = str(card)
stack = []
for i in cardnum:
    stack.append(i)
card_check()
odd=stack[1::2]
od = []
for a in odd:
    b=int(a)
    od.append(b)
idk = stack[::2]
rev = []
for i in idk:
    k=int(i)*2
    if k>=10:
        l = k-9
        rev.append(l)
    else:
        rev.append(k)
c = od+rev
l = 0
for i in c:
    l+=i
if l%10==0:
    print("Your card is valid")
else:
    print("Enter a valid card number")
