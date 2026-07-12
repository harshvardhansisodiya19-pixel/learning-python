#Write a program to write greates of all the numbers entered by users
a1=int(input("Enter number 1:"))
a2=int(input("Enter number 2:"))
a3=int(input("Enter number 3:"))
a4=int(input("Enter number 4:"))
if(a1>a2 and a1>a3 and a1>4):
    print("Greatest is a1")
if(a2>a1 and a2>a3 and a2>4):
    print("Greatest is a2")
if(a3>a2 and a3>a1 and a3>4):
    print("Greatest is a3")
if(a4>a2 and a4>a3 and a4>a1):
    print("Greatest is a4")

# A total of 40% marks and 33% min each subject

mark1 = int(input("Enter marks one"))
mark2 = int(input("Enter marks one"))
mark3 = int(input("Enter marks one"))

#Check for total %
total_percentage=(mark1+mark2+mark3)/300
p1=mark1/100
p2=mark2/100
p3=mark3/100

if(total_percentage>=.40 and p1>=.33 and p2>=.33 and p3>=.33):
    print("Congratulations you passed !")
    print(f"Your percentage is:",total_percentage*100)
else:
    print("Sorry, please try again next year.")

#write a program to detect spam comment using keywords
l1="Make a lot of money"
l2="Buy now"
l3="Subscribe this"
l4="Subscribe this"
message = input("Enter your comment:")
if ((l1 in message)or(l2 in message)or(l3 in message)or(l4 in message)):
    print("This is a spam")
else:
    print("This comment is a spam")

#  Lenght under 10 charactrs or not
name=input("Enter your name:")
if(0<len(name)<=10):
    print("Length of character under 10")
elif(len(name)>10):
    print("Length of character exceeds 10")
else:
    print("Invalid name")# suu wrote correct code by myself and no issues as well

#Write a program to find if given name present in list or not
j=["Harry","Harsh","Max"]
if(name in j):
    print("Your name is in the list")
else:
    print("Your name is not in the list.")

#For grade
if (0.9<=total_percentage<=1):
    grade="Ex"
elif(0.8<=total_percentage<0.9):
    grade="A"
elif(0.7<=total_percentage<0.8):
    grade="B"
elif(0.6<=total_percentage<0.7):
    grade="C"
elif(0.5<=total_percentage<0.6):
    grade="D"
elif(0<=total_percentage<0.5):
    grade="F"
print("Your grade is",grade)

#Write a program to find if the post  is talking about Harsh
post="Aur Harsh bhai kya halchal?"
if("Harsh".lower() in post.lower()):# sabko lower case krke compare kkrlo hArsh ho ya HARSH or any other it will work like a charm
    print("Harsh was mentioned in post")
else:
    print("Harsh was not mentiooned in post")