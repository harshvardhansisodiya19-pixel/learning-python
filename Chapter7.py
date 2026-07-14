#Loops
for i in range(1,101):# to print till 100 
    print(i)
# types of loop while loop for loop
#While loop
a=1
while(a<6):
    print(a)
    a+=1#wapis aayega condition check krega aur chalayega tb tk chlte rhega jab tk true
# 1 2 3 4 5 output hogi 6 pe aake rukea kyuki 6 doesnt fut solast printed will be 5
#If its never false then it will keep printing

#WRITE WHILE TO PRINT TILL 50
b=1
while(b<51):
    print(b)
    b+=1
#Write a program to print content of a list
x=[1,4,"Harry",False]
y=0
while(y<len(x)):
    print(x[y])
    y+=1
#For loop = bhai of while loop
for i in x:
    print(i)
s="Harsh"
for i in s:  #Each letter individually printed
    print(i)
# For loop with else 
l=[1,7,8]
for i in l:
    print(i)
else:
    print("Bas itna hi tha mere bhai")# primted when list is exhausted

for i in range(100):
    if(i==34):
        break# exit the loop after this point till 33 printed
    print(i)

for i in range(100):
    if(i==34):
        continue#Skip this iteration matlab 34 skip ho gya 31 32 33 35
    print(i)

for i in range(645):
  pass# it instructs to do nothing, basically come back later type of thing


i=0
while(i<45):
    print(i)
    i+=1 # Using pass statement no error is there good

#CHAPTER 7 ENDS HERE