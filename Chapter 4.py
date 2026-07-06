friends=["Apple","Orange",5,345.06,False,"Aakash","Rohan"]
print(friends[0])
a="Harry"
print(a[0])
print(a[3])
# a[3]='y'
# print(y)existing string se new bna skte hai but change nhi kr skte existing ko
friends[0]="Banana"#Mutable can be changed
print(friends[0])
#List is uded to store a set of value of any data type
#List can be indexed we did already
#List METHODS
friends.append("Mango")#adds a new value at the end of the list
print(friends)

l1=[1,35,6,98,101]
print(l1)
l1.sort()#sorts the list in ascending order
print(l1)
l1.reverse()#reverses the list
print(l1)
l1.insert(3,67)#inserts the value at the given index
print(l1)
l1.pop(2) # removes the value at the given index
print(l1)
l1.remove(67)#removes the value from the list
print(l1)
#Now i finally understand the difference between pop() and remove()
#and what he meant when he said doesn't return value and returns value
# Create a sample list of numbers
numbers = [10, 20, 30]

# pop() removes the last item (30) AND saves it to the variable 'grabbed'
grabbed = numbers.pop() 

# This will print: 30
print(grabbed)  

# This will print the modified list: [10, 20]
print(numbers)  
# Create the same sample list of numbers
numbers = [10, 20, 30]

# remove() deletes the value 20 from the list entirely
# It does NOT save anything, so the variable 'grabbed' is just empty (None)
grabbed = numbers.remove(20) 

# This will print: None
print(grabbed)  

# This will print the modified list: [10, 30]
print(numbers)  

