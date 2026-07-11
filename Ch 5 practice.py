#problem 1 Write dic with hindi words with value as their enlish translation
words={
"madad":"Help",
"kursi":"chair",
"billi":"cat"
}
# word =input("Enter the word you want meaning of:")
# print(words[word])

#Problem 2
#Write a program to take=int(input( of 8 numbers and display all unique numbers once
numbers=set()
n1=int(input("Enter the number you want:"))
n2=int(input("Enter the number you want:"))
n3=int(input("Enter the number you want:"))
n4=int(input("Enter the number you want:"))
n5=int(input("Enter the number you want:"))
n6=int(input("Enter the number you want:"))
n7=int(input("Enter the number you want:"))
n8=int(input("Enter the number you want:"))
# numbers.update((n1,n2,n3,n4,n5,n6,n7,n8))
# ye shyd galat ho gya set nhi int add krna tha nice try 😂 update se sirph set add krdi
#alt shift down arrow se copy paste ho jaata 
numbers.add(n1)
numbers.add(n2)
numbers.add(n3)
numbers.add(n4)
numbers.add(n5)
numbers.add(n6)
numbers.add(n7)
numbers.add(n8)
print(numbers)

#Problem 3 can we have a set with value 18 as int and string both
s= set()
# s.add(18)
# s.add("18")
# print(s)#yes both printed

#Problem 4
s.add(20)
s.add(20.0)
s.add('20')#lenght of s=2? coz 20=20.00
print(s)
print(1==1.00)#true because value is same so true no matter type s diff

#prohlem 5 s={}=> not set it iz a dictionary
p={}
print(type(p))

#Empty dictionary 4 friends to enter friends fav language
name=input("Enter friends name:")
lang=input("Enter language name:")
p.update({name:lang})
name=input("Enter friends name:")
lang=input("Enter language name:")
p.update({name:lang})
name=input("Enter friends name:")
lang=input("Enter language name:")
p.update({name:lang})
name=input("Enter friends name:")
lang=input("Enter language name:")
p.update({name:lang})
print(p)

#qns number same if two friends hae same name then?
#then the most recent will be considered final language because it will get updated
#q 9 can you change value inside a list which is conatained in a set
# z={8,7,12,"Harsh",[1,2]}
#set has no indexing so cant be changed
#Reason list ko set me include hi nhi kr skte
#kr bhi skte tbhi indexing krke change nhi ho pati
#require the elements to be immutable and hashable