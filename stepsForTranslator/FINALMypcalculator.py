import tkinter as tk
import os #only works for macOS
import threading



contrastMode = 0
#import threading

#big problem that I faced: I had a different file named threading.py that messed it all up

random = tk.Tk() #random to emphasize that this can be anything

random.configure(background="light blue")

def colour_contrast():

	global contrastMode #just means that this doesn't only apply in the function (is a variable every where / at the global scope)
	contrastMode = 1

	random.configure(background="black")
	labMYP.configure(background="black", foreground = "yellow") #black and yellow at either end of the colour wheel
	labIB.configure(background="black", foreground = "yellow")
	labCE.configure(background="black", foreground = "yellow")
	labLV.configure(background="black", foreground = "yellow")
	textMYP.configure(background="yellow", foreground = "black")
	textCExp.configure(background="yellow", foreground = "black")
	textQLevel.configure(background="yellow", foreground = "black")
	btnContrast.config(text="Normal Mode", command = colour_normal)
	textCExp.config(state = "disabled")

def colour_normal():

	global contrastMode 
	contrastMode = 0

	random.configure(background="light blue")
	btnContrast.config(text="Contrast Mode", command = colour_contrast)
	labMYP.configure(background="light blue", foreground = "black")
	labIB.configure(background="light blue", foreground = "black")
	labCE.configure(background="light blue", foreground = "black")
	labLV.configure(background="light blue", foreground = "black")
	textMYP.configure(background="light grey", foreground = "black")
	textCExp.configure(background="light grey", foreground = "black")
	textQLevel.configure(background="light grey", foreground = "black")

def speech():
	os.system("say Select an MYP term") #only works for macOS #ios exclusive code (can only be used on ios devices)

def say_term():
	term = var.get()
	toSay = "say " + term
	os.system(toSay)

def speechThread():
	t = threading.Thread(target = speech)
	t.start()

def speechThread1():
	s = threading.Thread(target = say_term)
	s.start() #problem that I faced, I was trying to have two speechThread(s)
	#and bind speechThread to target speech and say_term. I realized that I needed to make a new function

def change(*args):

	term = var.get() #goes into the var (which is all the command terms further down)
	

	definitions = {
		"Select": "", #clears everything // make sure to add comma (this was a problem I fell into while developing the code)
		"Analyse": "Definition for Analyse", #mapping the first string to the definition (analyse to "definition for apply")
		"Apply": "Definition for Apply",
		"Annotate": "Definition for Annotate",
		#add one extra term in video to demonstrate

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
	textMYP.delete("1.0",tk.END) #deletes everything in the box (from the first character ("1.0"), to the end)
	textMYP.insert("1.0",definitions.get(term)) #python3 dictionaries - Looks up term in definitions{}, then returns what's beside it // mapping the first string to the definition
	textMYP.config(state = "disabled") #makes the text box not-editable once again


	textCExp.config(state = "normal")
	textCExp.delete("1.0",tk.END)
	textCExp.insert("1.0",clarExplanation.get(term))
	textCExp.config(state = "disabled")

	textQLevel.config(state = "normal")
	textQLevel.delete("1.0",tk.END)
	textQLevel.insert("1.0",questionlevel.get(term))
	textQLevel.config(state = "disabled")



labMYP = tk.Label(random, text = "   MYP Term:", background="light blue")

labMYP.grid(pady = (0,0), row = 0, column = 0, sticky = "NESW")

#_______________________________________________

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

btnContrast = tk.Button(random, text = "Contrast Mode", foreground = "black", background = "light blue", command = colour_contrast)
btnContrast.configure(bg = "red")
btnContrast.grid(row = 8, column = 0, columnspan = 2, sticky = "NESW")


#_____________________________________________

btnEnter = tk.Button(random, text = "Help", command = speechThread) #command = speechThread
btnEnter.grid(row = 0, column = 1)


#____________________________________________

textMYP = tk.Text(random, background="light grey", height = 3, width = 20)
textMYP.config(state = "disabled")

textMYP.grid(row = 3, column = 0, columnspan = 2, sticky = "NESW", pady = (0,10))

#_____________________________________________

labIB = tk.Label(random, text = "    IB Definition:", background="light blue")

labIB.grid(row = 2, column = 0, columnspan = 1, pady = (0,10))

#________________________________________________

btnSAY = tk.Button(random, text = "Hear it", command = speechThread1)

btnSAY.grid(row = 2, column = 1, pady = (0,10))

#____________________________________________

textMYP = tk.Text(random, background="light grey", height = 3, width = 20)
textMYP.config(state = "disabled")

textMYP.grid(row = 3, column = 0, columnspan = 2, sticky = "NESW", pady = (0,10))

#___________________________________________

labCE = tk.Label(random, text = "Clarified Explanation:", background="light blue")

labCE.grid(pady = (0,10), row = 4, column = 0)

#_____________________________________________
def onclick():
		
		global contrastMode

		msg = "How we got our definition?\n"

		msg1 = "Students here at UCC were asked to... "

		popup = tk.Tk()
		popup.wm_title("!")
		if contrastMode == 0:

			label = tk.Label(popup, text = msg, font = ("Arial", 16), background = "light blue")
			label1 = tk.Label(popup, text = msg1, font = ("Arial", 12), background = "light blue")
		else:
			label = tk.Label(popup, text = msg, font = ("Arial", 16), background = "black", foreground = "yellow")
			label1 = tk.Label(popup, text = msg1, font = ("Arial", 12), background = "black", foreground = "yellow")

		label.grid(row = 0, column = 0, sticky = "NESW")
		label1.grid(row = 1, column = 0, sticky = "NESW")
		B1 = tk.Button(popup, text = "Back", command = popup.destroy) #ios doesn't allow for a button to have a background or colour from what I found,
		#so I just made the whole thing a grid and used sticky for everything (to make the button go all the way across)
		B1.grid(row = 2, column = 0, sticky = "NESW")
		popup.mainloop()

btnInfo = tk.Button(random, text = "Info", command = lambda: onclick())

btnInfo.grid(pady = (0,10), row = 4, column = 1, columnspan = 1, sticky = "NESW")


#____________________________________________

textCExp = tk.Text(random, background="light grey", height = 3, width = 20)
textCExp.config(state = "disabled")

textCExp.grid(row = 5, column = 0, columnspan = 2, sticky = "NESW", pady = (0,10))

#____________________________________________

labLV = tk.Label(random, text = "Level of Question seen in:", background = "light blue")

labLV.grid(row = 6, column = 0, columnspan = 2, pady = (0,10))

#____________________________________________

textQLevel = tk.Text(random, background="light grey", height = 3, width = 20)
textQLevel.config(state = "disabled")

textQLevel.grid(row = 7, column = 0, columnspan = 2, sticky = "NESW")

#________________________________________

random.mainloop()

#Basic:
#1: Contruct
#2: Configure
#3: Pack

#btn.Enter = tk.Button(random, text = "Search")

#btn.Enter.pack()

#******* extension: allows for people on the internet (using a JSON) to add an example of a question with the command term in it (also add this as a text box / output)
#I'd like to add colour to the background of my 