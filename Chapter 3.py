#STRINGS
#String is a data type in python
#Seq of characters enclosed in quotes.
#We can primarily right it in 3 ways
#String slicing : A string in python can be sliced for getting a part of the strings.
Name="Harsh"
b='Harsh'
c='''Harsh'''
name_short=Name[0:3]# seedhi 01234 or -5 -4 -3 -2 -1 ulti ginti last one is excludedd
print(name_short)#Har
print(Name[-5:-2])#Har

print(Name[-1:-4])# nothing display somethings wrong?
print(Name[-4:-1])#ars
print(Name[5:1])#looks like it doesnt print backwards
print(Name[1:])#arsh same as Name[1:5] or Name[1:len(Name)]
#Slicing with skip value
word = "amazing" 
print(word[1:7:3]) #output: ai
a="0123456789" 
print(a[1:8:2]) #output: 1357

#String functions
#len() function this function tells about the length of the string
print(len(Name)) #5
print(Name.endswith("sh")) #True
print(Name.startswith("Ha")) #True
print(Name.find("rs")) #2
print(Name.capitalize()) #Harsh only capitalizes first letter
print(Name.upper()) #HARSH
print(Name.lower()) #harsh
print(Name.count("h")) #1how many types in it
print(Name.replace("sh","SH")) #HarSH

#Chat gpt use as per instructor( the multiple comments below this which are continous written by chat gpt are not written by me but by chat gpt)
# lower()          -> Converts string to lowercase
# "HELLO".lower()                  # 'hello'

# upper()          -> Converts string to uppercase
# "hello".upper()                  # 'HELLO'

# title()          -> Capitalizes first letter of each word
# "hello world".title()            # 'Hello World'

# capitalize()     -> Capitalizes only the first letter
# "python".capitalize()            # 'Python'

# strip()          -> Removes leading and trailing whitespace
# " hello ".strip()                # 'hello'

# lstrip()         -> Removes leading whitespace
# " hello".lstrip()

# rstrip()         -> Removes trailing whitespace
# "hello ".rstrip()

# replace(old, new) -> Replaces occurrences of a substring
# "apple".replace("p", "b")        # 'abble'

# split(sep)       -> Splits string into a list
# "a,b,c".split(",")               # ['a', 'b', 'c']

# join(iterable)   -> Joins elements using the string as separator
# "-".join(['a', 'b', 'c'])        # 'a-b-c'

# find(sub)        -> Returns index of first occurrence (-1 if not found)
# "python".find("t")               # 2

# index(sub)       -> Returns index (raises ValueError if not found)
# "python".index("t")              # 2

# count(sub)       -> Counts occurrences of a substring
# "banana".count("a")              # 3

# startswith(prefix) -> Checks if string starts with prefix
# "python".startswith("py")        # True

# endswith(suffix) -> Checks if string ends with suffix
# "python".endswith("on")          # True

# isalpha()        -> True if all characters are alphabetic
# "Hello".isalpha()                # True

# isdigit()        -> True if all characters are digits
# "123".isdigit()                  # True

# isalnum()        -> True if all characters are letters or digits
# "abc123".isalnum()               # True

# isspace()        -> True if all characters are whitespace
# "   ".isspace()                  # True

# center(width)    -> Centers string within given width
# "Hi".center(6)                   # '  Hi  '

# zfill(width)     -> Pads string with leading zeros
# "25".zfill(5)                    # '00025'

# swapcase()       -> Swaps uppercase and lowercase letters
# "PyThOn".swapcase()              # 'pYtHoN'


#Written by me from now on
#Escape sequences in python
a="Harsh is a good boy" \
" but not a bad boy" 
# agar \ "" nhi kroge to new line conder nhi hogi a print hi nhi hoga
print(a)
# agr "" print krna ho
b="Harsh is a good boy but not a bad boy \"but he is a good boy\""
print(b)#lo ho gyi " "print