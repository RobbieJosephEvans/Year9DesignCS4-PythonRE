
#A loop is a programing structure that can repeat a section of code
#A loop can run the same code exactle over and over or
#with some thought it can generate a pattenr.

#The are two broad catagories of loops
#Conditional Loops ( while); These loop as long as a condition is true.

#Counted Loops (for): These loop using a counter to keep trrack of 
#					how many the loop has run
#
#You can use any loop in any situation, but usually from a design
#perspective there is a better loop in terms of coding.

#If you know if advance how many times a loop should run a COUNTED LOOP
#is usually the better choice

#If you don't know how many times a loop should run if a CONDITIONAL LOOP
#is usually the better choice.

print("*************************************")
#Taking Inputs

word = "" #We have to declare and initialize a word so it fails the while loop

while len(word) < 6 or word.isalpha() == False:
	#Loop back
	word = input("Please input a word larger than 5 letters: ")
	
	if (len(word) < 6):
		print("That word has less than 5 letters")
	if (word.isalpha() == False):
		print("That is likely more than one word")

	#When we reach the bottom of the loop block we check the condition again

print(word+" is a seriosly wrong word!")
