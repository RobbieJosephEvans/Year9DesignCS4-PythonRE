import tkinter as tk

random = tk.Tk()

#_____________________________________________

labMYP = tk.Label(random, text = "MYP Term")

labMYP.pack()

#_____________________________________________

entMYP = tk.Entry(random)

entMYP.pack(pady = (0,0))

#___________________________________________

btnEnter = tk.Button(random, text = "Enter")
btnEnter.pack(pady = (0,10))

#_____________________________________________

labIB = tk.Label(random, text = "IB Definition")

labIB.pack(pady = (0,10))

#____________________________________________

entIB = tk.Entry(random)

entIB.pack(pady = (0,10))

#___________________________________________

labCE = tk.Label(random, text = "Clarified Explanation")

labCE.pack(pady = (0,10))

#____________________________________________

entCE = tk.Entry(random)

entCE.pack(pady = (0,10))

#____________________________________________

labLV = tk.Label(random, text = "Level of Question seen in")

labLV.pack(pady = (0,10))

#____________________________________________

entLV = tk.Entry(random)

entLV.pack(pady = (0,10))

#_____________________________________________



#______________________________________________

random.mainloop()

#Basic:
#1: Contruct
#2: Configure
#3: Pack

#btn.Enter = tk.Button(random, text = "Search")

#btn.Enter.pack()

