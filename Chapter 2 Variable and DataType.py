a=1
b=2
print(a+b)
#variable = containner in which you can store things just like a jar
# Data types are of following types
# 1)Integers 1 2 3 like a= 1
# 2)Floating numbers Decimal wale a=6.7
# 3)a="Hari" double => string
# 4)Booleans d = True 
# 5)e= None=>none type variable
#   kabhi kabhi nothing ko verify krne me not false because it is for yes or no this is for if something is there or not
a=1
b= 1.2
c="Hari"
d= False
e= None
'''
Rules for defining variable names
A variable name can only start with an alphabets and underscores
A variable name can't start with a digit
No while space is allowed to be used inside a varible name
'''

harry=34
# @Mega=56
_Mega=64
Mega_slayer =8
Mega123=9
# Mega@Slayer=10
# 123Mega=19
# print(Mega@Slayer)

# Operator in python
'''
Arithematic operator +,-,*,/etc.
Assignment operator=,+=,-=etc.
Comparision operator ==,>,>=<,<!=etc.
Logical operators: and,or,not.
7+4=11 here 7 and 4 are operants and + is operand and 11 is result

'''
f=a+b
print(f)

#Assignment operators
a=4-2 #assign 4-2 in a
b=6
b+=3# increment of 3 in b
print(a)
print(b)
b-=6#subtract 6 from currrent value of b i.e. 9
print(b)

#Comparision Operators (they give aanswer as true or false)
print("Comparision operator this point onwards")
d=5<4
print(d)
#False obvious
e= 9>6
print(e)#true
f=5>=5
print(f)#true
g=6==6 # == checks if they are same = is usd for inserting variable
print(g)

#Logical Operators
print("Logical operators this point onwards")
e= True or False
print(e)
#Typical boolean sheet not making a truth table Its all good


print("TYPECASTING ")
#Type FUNCTION AND TYPE CASTING
t= type(a)
print(t)#int obv
print(type(c))#str obvious
b=float(a)#hogai iski type change
