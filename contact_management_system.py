# PROGRAM: It's a basic CRUD system for contacts. One of my first ever projects.
a=[]
def cms():
    print("========== CONTACT MANAGEMENT SYSTEM ==========")
    print("Please enter the corresponding numbers to run that particular function.")
    print("1. Add contact \n2. Display All Contacts \n3. Search Contact \n4. Update Contact")
    print("5. Delete Contact \n6. Sort Contacts by Name \n7. Exit")
    inp=int(input())
    return inp
def add_contact():
    print("Please enter the details.")
    name=input("Name:")
    phno=input("Phone no.:")
    email=input("Email:")
    city=input("City:")
    contact={
        'Name':name,
        'Phno':phno,
        'Email':email,
        'City':city
        }
    for exist_contact in a:
        if (exist_contact['Phno']==phno or exist_contact['Email']==email):
            print("Contact already saved")
            return
    a.append(contact)
    print("Contact saved")
def display_contact():
    if len(a)==0:
        print("No contacts saved.")
    else:
        for contact in a:
            print("NAME:",contact['Name'],"\n""PH NO.:",contact['Phno'])
            print("CITY:",contact['City'],"\n""EMAIL:",contact['Email'])
            print("------------------------")  
def search_contact():
    name=input("Enter name:")
    for contact in a:
        if contact['Name']==name:
            print("NAME:",name)
            print("PHNO:",contact['Phno'])
            print("CITY:",contact['City'])
            print("EMAIL:",contact['Email'])
            return
    print("Not found")
def update_contact():
    name=input("Enter name:")
    for contact in a:
        if contact['Name']==name:
            print("Which field do u want to update?\nEnter the following numbers for respective features")
            print("1.Name\n2.Phno.\n3.Email\n4.City")
            num=int(input("Enter num: "))
            if num==1:
                newName=input("Name: ")
                contact['Name']=newName
            elif num==2:
                newPhno=input("Phno: ")
                contact['Phno']=newPhno
            elif num==3:
                newEmail=input("Email: ")
                contact['Email']=newEmail   
            elif num==4:
                newCity=input("City: ")
                contact['City']=newCity
            else:
                print("Invalid number")
                return
            print("Contact updated succesfully")
            return
    print("Contact not found")
def delete_contact():
    name=input("Name: ")
    for contact in a:
        if contact['Name']==name:
            a.remove(contact)
            print("Contact deleted.")
            return
    print("Contact not found")
def merge_sort(name):
    if len(name)<=1:
        return name
    mid=len(name)//2
    leftHalf=name[:mid]
    rightHalf=name[mid:]
    leftHalf=merge_sort(leftHalf)
    rightHalf=merge_sort(rightHalf)
    merged=[]
    i=j=0
    while j<len(rightHalf) and i<len(leftHalf):
        if leftHalf[i]['Name']<rightHalf[j]['Name']:
            merged.append(leftHalf[i])
            i+=1
        else:
            merged.append(rightHalf[j])
            j+=1
    while i < len(leftHalf):
        merged.append(leftHalf[i])
        i += 1

    while j < len(rightHalf):
        merged.append(rightHalf[j])
        j += 1
    return merged
def sort_name():
    if len(a)==0:
        print("No contacts saved")
        return
    sorted_contacts=merge_sort(a)
    for contact in sorted_contacts:
        print(contact)
while True:
    k=cms()
    if k==1:
        add_contact()
    elif k==2:
        display_contact()
    elif k==3:
        search_contact()
    elif k==4:
        update_contact()
    elif k==5:
        delete_contact()
    elif k==6:
        sort_name()
    else:
        print("Goodbye")
        break
