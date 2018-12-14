import tkinter as tk

random = tk.Tk()

#_____________________________________________

labMYP = tk.Label(random, text = "MYP Term")

labMYP.grid(pady = (0,0), row = 0, column = 0)

#_____________________________________________

textMYP = tk.Text(random,  background = "light grey", height = 10, width = 50)
textMYP.config(state = "disabled")

textMYP.grid(row = 1, column = 0, columnspan = 2)

#___________________________________________

btnEnter = tk.Button(random, text = "Enter")

btnEnter.grid(row = 0, column = 1, sticky = "NESW")

#_____________________________________________

labIB = tk.Label(random, text = "IB Definition")

labIB.grid(pady = (0,10))

#____________________________________________

entIB = tk.Entry(random)

entIB.grid(pady = (0,10))

#___________________________________________

labCE = tk.Label(random, text = "Clarified Explanation")

labCE.grid(pady = (0,10), row = 5, column = 0)

#_____________________________________________

btnEnter = tk.Button(random, text = "Info")

btnEnter.grid(pady = (0,10), row = 5, column = 1)

#____________________________________________

entCE = tk.Entry(random)

entCE.grid(pady = (0,10))

#____________________________________________

labLV = tk.Label(random, text = "Level of Question seen in")

labLV.grid(pady = (0,10))

#____________________________________________

entLV = tk.Entry(random)

entLV.grid(pady = (0,10))

#_____________________________________________



#______________________________________________

random.mainloop()

#Basic:
#1: Contruct
#2: Configure
#3: Pack

#btn.Enter = tk.Button(random, text = "Search")

#btn.Enter.pack()

