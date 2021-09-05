
#create list for names and numbers
listname = ['Amal' ,1111111111 , 'Mohammed' ,2222222222 , 'Khadija',3333333333 , 'Abdulla' ,4444444444 , 'Rawan' , 5555555555, 'Fisal' ,
6666666666, 'Layla' ,77777777777]


n = input("please enter name")

if n == "Amal":
    print("1111111111")
elif n == "Mohammed":
    print("2222222222")
elif n == "Khadija":
    print("3333333333")
elif n == "Abdulla":
    print("4444444444")
elif n == "Rawan":
    print("5555555555")
elif n == "Fisal":
    print("6666666666")
elif n == "Layla":
    print("7777777777")
else:
    print("Sorry, the number is not found")


# extra questions
# 1
name = input("Enter Name :")
if name in listname:
    print(name)
else:
    print("Name not found")

# 2
listname.append(input("enter name and number"))
print(listname)
