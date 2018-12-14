import tkinter as tk

random = tk.Tk()

def change():
	print(var.get())


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
dropDown.grid(row = 1, column = 0, columnspan = 1, sticky = "NESW", pady = 10)

#_____________________________________________


#_____________________________________________

btnEnter = tk.Button(random, text = "Enter")

btnEnter.grid(row = 0, column = 1)

#_____________________________________________

#if btnEnter == 


#_____________________________________________

labIB = tk.Label(random, text = "IB Definition")

labIB.grid(pady = (0,10))

#____________________________________________

textMYP = tk.Text(random,  background = "light grey", height = 3, width = 20)
textMYP.config(state = "disabled")

textMYP.grid(row = 3, column = 0, columnspan = 1, sticky = "NESW")

#___________________________________________

labCE = tk.Label(random, text = "Clarified Explanation")

labCE.grid(pady = (0,10), row = 5, column = 0)

#_____________________________________________

btnEnter = tk.Button(random, text = "Info")

btnEnter.grid(pady = (0,10), row = 5, column = 1, columnspan = 2, sticky = "NESW")

#____________________________________________

textMYP = tk.Text(random,  background = "light grey", height = 3, width = 20)
textMYP.config(state = "disabled")

textMYP.grid(columnspan = 1, sticky = "NESW")

#____________________________________________

labLV = tk.Label(random, text = "Level of Question seen in")

labLV.grid(pady = (0,10))

#____________________________________________

textMYP = tk.Text(random,  background = "light grey", height = 3, width = 20)
textMYP.config(state = "disabled")

textMYP.grid(columnspan = 1, sticky = "NESW")

#_____________________________________________



#______________________________________________

random.mainloop()

#Basic:
#1: Contruct
#2: Configure
#3: Pack

#btn.Enter = tk.Button(random, text = "Search")

#btn.Enter.pack()

