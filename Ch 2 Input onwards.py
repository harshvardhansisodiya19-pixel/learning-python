#Input
a= input("Enter a number 1: ")#by default input is string
b= input("Enter a number 2: ")
print("Number a is: ", a)
print("Number b is: ", b)
print ("The sum of these two numbers is: ", a+b)#this will give a string concatenation (jur gyi as it is) because both are string
a = int(a)#typecasting to int
b = int(b)
print ("The sum of these two numbers is: ", a+b)#this will give a integer addition because both are int
