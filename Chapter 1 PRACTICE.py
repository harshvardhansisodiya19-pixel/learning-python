#Problem one write a code to print twinkl twinkle llittle star
print('''Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.
When the blazing sun is set, and the grass with dew is wet. Then you show your little
light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you
are.
Then the traveler in the dark thanks you for your tiny spark. How could he see where to
go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.
As your bright and tiny spark lights the traveler in the dark, though I know not what you
are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are.''')

#''' ''' ko use krke multiline rint krne me use kr skte hai

#Problem two was to use repl for doing multiplication

#qns 3 Install an external module and use it perform a task of your intrest
#Using chatgpt as suggested to know its power but told not to rely until chapter 4 or 5
import pyttsx3
engine = pyttsx3.init()
engine.say("I am on top of the world")
engine.runAndWait()

#qns4  write a python program to print the contents of a directory using the os module. Search online for the function which does that.
import os

# Specify the directory path
path = "."

# Get the list of files and folders
contents = os.listdir(path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)

#qns 5 label it with comments
#Chapter 1 done less goo..