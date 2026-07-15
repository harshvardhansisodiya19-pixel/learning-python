# Problem 1 Print table
n=int(input("Enter a number:"))
for i in range(1,11):
    print(f"{n}x{i}={n*i}")

#write program to greet person whose name starts with s in given list
l=["Harsh","Saanya","Saurabh","Harjeet"]
for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")
#attempt using while
i=1
while(i<11):
    print(f"{n}x{i}={n*i}")
    i+=1
# Program to find number prime or not

for i in range(2,n):
    if(n%i)==0:
        print("Number is not a prime")
    else:
        print("Number is a prime")
#Problem
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)
    
# Factorial n 
product=1
for i in range(1,n+1):
    product=product*i
print(f"The factorial of {n} is {product}")

#write program to print the following star pattern
'''
n=3
  *
 ***
'''  
for i in range(1,n+1):
    print(" "* (n-i),end="")
    print("*"*(2*i-1),end="")
    print("\n")

#problem
for i in range(1,n+1):
    if(i==1 or i ==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")
    # pattern ***
             #* *
             #***
# Program to write table of n in reverse order
a=[]
for i in range(1,11):
  
    a.append(f"{n}x{i}={n*i}")
    a.reverse()
    print(a)
# 2nd way
for i in range(1,11):
    b=(f"{n}x{11-i}={n}*{11-i}")
    print(b)
  
