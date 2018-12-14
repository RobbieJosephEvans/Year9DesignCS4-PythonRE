#This file will go through the basics of 
#String Manipulation

#Strings are collections of characters
#String are enclosed in "" or ''

# "Paul"

#two things we need to talk about when we think about strings
#index - always starts at 0
#length

#Example
#  0123     012345
# "Paul"   "Monkey"
#len("paul") = 4
#len("menkey") = 6

name = "Paul"

print(name) #I can print strings
sentence = name + " is cool!"
print(sentence)

#I can access specific letters
fLetter = name[0]
print(fLetter)
letters1 = name [0:2] #inclusice:exclusive
print(letters1)
letters2 = name [2:len(name)]
print(letters2)
letters3 = name[:2]
print(letters3)

#if I want to print out all letters
for i in range(len(name)):
	print(name[i])
