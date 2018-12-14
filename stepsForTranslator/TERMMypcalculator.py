import tkinter as tk
import os
import threading
#import threading

#big problem that I faced: I had a different file named threading.py that messed it all up

random = tk.Tk() #random to emphasize that this can be anything

def colour_contrast():
	random.configure(background="blue")
	#btnNormal = tk.Button(random, text = "     Normal Mode    ", command = colour_normal) #command = speechThread
	#btnNormal.configure(bg = "red")
	#btnNormal.grid(row = 8, column = 1, sticky = "NESW")
	#btnContrast.config(row = 8, column = 0, columnspan = 1, sticky = "NESW")
	btnContrast.config(text="Normal Mode", command = colour_normal)
	#textMYP.config(random, background="yellow", height = 3, width = 20)
	textCExp.config(state = "disabled")

def say_term():
	term = var.get()
	toSay = "say " + term
	os.system(toSay)

random.configure(background="light blue")

def colour_normal():
	random.configure(background="light blue")
	btnContrast.config(text="Contrast Mode", command = colour_contrast)

def speechThread():
	t = threading.Thread(target = speech)
	t.start()

def colour_blue():
	random.configure(background="light blue")


def speech():
	os.system("say Select an MYP term")

def change(*args):
	#Since every definition starts with the name of the command term.  
	#always followed by a :
	#Step 1: 
	#store the var term in a temp variable called term
	term = var.get() #Analyse

	#Loop through the list definitions and pull out all the character before the :
	#When I find the value matches term I will print to the Text box
	

	definitions = {
		"Select": "", #clears everything // make sure to add comma (this was a problem I fell into while developing the code)
		"Analyse": "Definition for Analyse",
		"Apply": "Definition for Apply",
		"Annotate": "Definition for Annotate",


	}

	clarExplanation = {
		"Select": "", #clears everything
		"Analyse": "Explanation for Analyse",
		"Apply": "Explanation for Apply",
		"Annotate": "Explanation for Annotate",
	}

	questionlevel = {
		"Select": "",
		"Analyse": "Level for Analyse",
		"Apply": "Level for Apply",
		"Annotate": "Level for Annotate",
	}
	#reason why this is not ideal is because it would be hard to add several different terms when i fully develop the idea
	textMYP.config(state = "normal") #allowing for the text box to be editable
	textMYP.delete("1.0",tk.END) #deletes everything in the box
	textMYP.insert("1.0",definitions.get(term)) #python3 dictionaries - Looks up term in definitions{}, then returns what's beside it
	textMYP.config(state = "disabled") #makes the text box not-editable once again


	textCExp.config(state = "normal")
	textCExp.delete("1.0",tk.END)
	textCExp.insert("1.0",clarExplanation.get(term))
	textCExp.config(state = "disabled")

	textQLevel.config(state = "normal")
	textQLevel.delete("1.0",tk.END)
	textQLevel.insert("1.0",questionlevel.get(term))
	textQLevel.config(state = "disabled")




	#for i in range(0,len(definitions),1):
	#	colLoc = definitions[i].index(":")
	##	if (cterm == term):
	#		textMYP.config(state = "normal")
	#		textMYP.delete("1.0",tk.END)
	#		textMYP.insert("1.0",definitions[i])
	#		textMYP.config(state = "disabled")
	
#definitions = [
#	"Analyse:\ndefinition1\n",
#	"Apply:\ndefinition2\n",
#	"Annotate:\ndefinition3\n"

#



#_____________________________________________

labMYP = tk.Label(random, text = "MYP Term:", background="light blue")

labMYP.grid(pady = (0,0), row = 0, column = 0, sticky = "NESW")

#____________________________________________



#_____________________________________________

COMMANDTERM = [
	"Select",
	"Analyse",
	"Annotate",
	"Apply"
]

var = tk.StringVar() #Special variable that holds what is in the drop down
var.set(COMMANDTERM[0])
var.trace("w", change)

dropDown = tk.OptionMenu(random, var, COMMANDTERM[0],COMMANDTERM[1],COMMANDTERM[2],COMMANDTERM[3])
dropDown.grid(row = 1, column = 0, columnspan = 2, sticky = "NESW", pady = 10)

#_____________________________________________

btnContrast = tk.Button(random, text = "Contrast Mode", foreground = "black", background = "light blue", command = colour_contrast) #command = speechThread
btnContrast.configure(bg = "red")
btnContrast.grid(row = 11, column = 0, columnspan = 2, sticky = "NESW")

	#if colour_red == True:
	#	btnNormal = tk.Button(random, text = "Normal Mode", command = colour_normal) #command = speechThread
	#	btnNormal.configure(bg = "red")
	#	btnNormal.grid(row = 0, column = 0)

#_____________________________________________

btnEnter = tk.Button(random, text = "Speech", command = speechThread, bg="khaki1") #command = speechThread
btnEnter.grid(row = 0, column = 1)

#_____________________________________________


labTerm = tk.Label(random, text = "Term:", background="light blue")

labTerm.grid(row = 2, column = 0, columnspan = 2, pady = (0,10))

#_________________________________________________

textTerm = tk.Text(random, background="light grey", height = 3, width = 20)
textTerm.config(state = "disabled")

textTerm.grid(row = 3, column = 0, columnspan = 2, sticky = "NESW", pady = (0,10))

#____________________________________________



#_____________________________________________

labIB = tk.Label(random, text = "IB Definition:", background="light blue")

labIB.grid(row = 4, column = 0, columnspan = 2, pady = (0,10))

#_____________________________________________

btnSAY = tk.Button(random, text = "Term", command = say_term)

btnSAY.grid(row = 4, column = 1, pady = (0,10))

#____________________________________________

textMYP = tk.Text(random, background="light grey", height = 3, width = 20)
textMYP.config(state = "disabled")

textMYP.grid(row = 6, column = 0, columnspan = 2, sticky = "NESW", pady = (0,10))

#___________________________________________

labCE = tk.Label(random, text = "Clarified Explanation:", background="light blue")

labCE.grid(row = 7, column = 0, pady = (0,10))

#_____________________________________________
def onclick():
		msg = "How we got our definition?\n"

		msg1 = "Students here at UCC were asked to... "

		popup = tk.Tk()

		popup.wm_title("!")
		label = tk.Label(popup, text = msg, font = ("Arial", 16), background = "light blue")
		label1 = tk.Label(popup, text = msg1, font = ("Arial", 12), background = "light blue")
		label.pack(side = "top", fill = "x")
		label1.pack(side = "top", fill = "x")
		B1 = tk.Button(popup, text = "Back", command = popup.destroy, background = "light blue")
		B1.pack()
		popup.mainloop()

btnInfo = tk.Button(random, text = "Info", command = lambda: onclick())

btnInfo.grid(pady = (0,10), row = 7, column = 1, columnspan = 1, sticky = "NESW")




#____________________________________________

textCExp = tk.Text(random, background="light grey", height = 3, width = 20)
textCExp.config(state = "disabled")

textCExp.grid(row = 8, column = 0, columnspan = 2, sticky = "NESW", pady = (0,10))

#____________________________________________

labLV = tk.Label(random, text = "Level of Question seen in:", background = "light blue")

labLV.grid(row = 9, column = 0, columnspan = 2, pady = (0,10))

#____________________________________________

textQLevel = tk.Text(random, background="light grey", height = 3, width = 20)
textQLevel.config(state = "disabled")

textQLevel.grid(row = 10, column = 0, columnspan = 2, sticky = "NESW")

#_____________________________________________

#textSpace = tk.Text(random, background="light blue", height = 3, width = 20)
#textSpace.config(state = "disabled")

#textSpace.grid(row = 9, column = 0, columnspan = 2, sticky = "NESW", pady = (0,10))

#______________________________________________

random.mainloop()

#Basic:
#1: Contruct
#2: Configure
#3: Pack

#btn.Enter = tk.Button(random, text = "Search")

#btn.Enter.pack()

#******* allows for people on the internet (using a JSON) to add an example of a question with the command term in it (also add this as a text box / output)
#I'd like to add colour to the background of my 