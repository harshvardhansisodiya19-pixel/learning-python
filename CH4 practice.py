#Problem 1 write a program to store seven in a list entered by the user
#edited same list for marks using edit all occurences PROBLEM 2
marks = []

f1 = int(input("Enter marks here: "))
marks.append(f1)

f2 = int(input("Enter marks here: "))
marks.append(f2)

f3 = int(input("Enter the marks here: "))
marks.append(f3)

f4 = int(input("Enter the marks here: "))
marks.append(f4)

f5 = int(input("Enter the marks here: "))
marks.append(f5)

f6 = int(input("Enter the marks here: "))
marks.append(f6)

f7 = int(input("Enter the marks here: "))
marks.append(f7)

print(marks)

#problem 3

# a=(34,234,"Harry") error=> tupple cannot be changed
# a=[2]="Larry"

#Problem 4

l=[34,23,645,123]
print(sum(l))

# Write a problem to count the number of zeroes in following tuple
a=(7,8,0,82,4,0,3,4,0,0,0,2,4,9,1,3,2,0,0,0,0,0,)
print(a.count(0))
#Result -10

# SUGGESTION OF CHAT GPT
marks = []

for i in range(7):
    mark = int(input(f"Enter marks {i+1}: "))
    marks.append(mark)

print(marks)