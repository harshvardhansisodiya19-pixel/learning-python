#Practice set
#Problem1
input1=input("Enter your name: ")
print(f"Good afternoon {input1}")

#Problem2
letter='''Dear <|Name|>,
You are selected!
Date: <|Date|>'''

print(letter.replace("<|Name|>",input1))
print(letter.replace("<|Date|>","2/7/2026 "))
print(letter.replace("<|Name|>",input1).replace("<|Date|>","2/7/2026 ")) # Now this will be replaced together
#Problem 3 finding double spcae in a string

name ="Harsh is a  good boy"
print(name.find("  "))#output: 10 iss index pe double space -1 implies no double space
print(name.replace("  "," "))#output: Harsh is a good boy string change nhi hui print kre samay new string ka formation hua tha

#Problem 4 Write a program to format the following letter using escape sequence characters
letter='''Dear Harsh,this python course is nice.Thanks!'''
letter2='''Dear Harsh,\n\tthis python course is nice.\nThanks!'''
print(letter)
print(letter2)
#\n  new line \t tab space and capitalise T
#CHAPTER 3 OVER YOHOO