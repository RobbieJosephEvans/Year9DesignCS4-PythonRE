import tkinter as tk
import os 
#import threading

random = tk.Tk()

#def speechThread():
#	t = threading.Thread(target = speech)
#	t.start()


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

	for i in range(0,len(definitions),1):
		colLoc = definitions[i].index(":")
		cterm = definitions[i][0:colLoc]
		if (cterm == term):
			textMYP.config(state = "normal")
			textMYP.delete("1.0",tk.END)
			textMYP.insert("1.0",definitions[i])
			textMYP.config(state = "disabled")
	
definitions = [
	"Analyse:\ndefinition1\n",
	"Apply:\ndefinition2\n",
	"Annotate:\ndefinition3\n"

]

#_____________________________________________

labMYP = tk.Label(random, text = "MYP Term")

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


#_____________________________________________

btnEnter = tk.Button(random, text = "Speech", command = speech) #command = speechThread

btnEnter.grid(row = 0, column = 1)

#_____________________________________________

#if btnEnter == 


#_____________________________________________

labIB = tk.Label(random, text = "IB Definition")

labIB.grid(row = 2, column = 0, columnspan = 2, pady = (0,10))

#____________________________________________

textMYP = tk.Text(random,  background = "light grey", height = 3, width = 20)
textMYP.config(state = "disabled")

textMYP.grid(row = 3, column = 0, columnspan = 2, sticky = "NESW")

#___________________________________________

labCE = tk.Label(random, text = "Clarified Explanation")

labCE.grid(pady = (0,10), row = 4, column = 0)

#_____________________________________________
def onclick():
		msg = "How we got our definition?\nStudents here at UCC were asked to... "

		popup = tk.Tk()

		popup.wm_title("!")
		label = tk.Label(popup, text = msg)
		label.pack(side = "top", fill = "x")
		B1 = tk.Button(popup, text = "Back", command = popup.destroy)
		B1.pack()
		popup.mainloop()

btnInfo = tk.Button(random, text = "Info", command = lambda: onclick())

btnInfo.grid(pady = (0,10), row = 4, column = 1, columnspan = 1, sticky = "NESW")




#____________________________________________

textCExp = tk.Text(random,  background = "light grey", height = 3, width = 20)
textCExp.config(state = "disabled")

textCExp.grid(row = 5, column = 0, columnspan = 2, sticky = "NESW")

#____________________________________________

labLV = tk.Label(random, text = "Level of Question seen in")

labLV.grid(row = 6, column = 0, columnspan = 2, pady = (0,10))

#____________________________________________

textQLevel = tk.Text(random,  background = "light grey", height = 3, width = 20)
textQLevel.config(state = "disabled")

textQLevel.grid(row = 7, column = 0, columnspan = 2, sticky = "NESW")

#_____________________________________________



#______________________________________________

random.mainloop()

#Basic:
#1: Contruct
#2: Configure
#3: Pack

#btn.Enter = tk.Button(random, text = "Search")

#btn.Enter.pack()

