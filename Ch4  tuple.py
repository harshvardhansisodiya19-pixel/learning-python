a=()#empty tuple
print(type(a))
#a=(1 not tuple but a=(1,) is a tuple
#Tuple can not be changed
a=(1,45,343,3424,False,"Rohan","shivam")
print(a)
#Tuple methods
no= a.count(45)#counts the number of times 45 is present in the tuple
print(no)

#CHATGPT
# tuple.count()

fruits = ("apple", "banana", "apple", "orange")

print(fruits.count("apple"))
# tuple.index()

fruits = ("apple", "banana", "apple", "orange")

print(fruits.index("banana"))
# tuple.index() with start position

numbers = (1, 2, 3, 2, 4)

print(numbers.index(2, 2))
# Useful functions with tuples

t = (5, 2, 8, 1)

print(len(t))#Length of the tuple
print(max(t))#Maximum value in the tuple
print(min(t))#Minimum value in the tuple
print(sum(t))#Sum of all elements in the tuple
print(sorted(t))#Returns a new sorted list from the elements of the tuple
print(tuple(reversed(t)))#Returns a new tuple with elements in reverse order