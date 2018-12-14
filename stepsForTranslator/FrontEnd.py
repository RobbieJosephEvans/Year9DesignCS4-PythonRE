
import tkinter as tk

#use pack (all elements are vertically alligned)

#Main Window
root = tk.Tk() #creates standard window
#Tk() is called a contructor (due to capital letter)

#1: Contruct
#2: Configure
#3: Pack

labUN = tk.Label(root, text = "User Name")

labUN.pack()

entUN = tk.Entry(root)
entUN.pack()

labPassword = tk.Label(root, text = "Password")
labPassword.pack()

labPassword = tk.Entry(root, show = "*")
labPassword.pack()



btnSubmit = tk.Button(root, text = "Submit")
btnSubmit.pack()

root.mainloop() #starts the program (EVENT DRIVEN -
#it waits for an event like the user's enter)

#Basic:
#1: Contruct
#2: Configure
#3: Pack