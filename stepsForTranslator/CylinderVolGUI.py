import tkinter as tk
import math



#All your functions, which in python are titled def
#for definition, should be at the  top
def submit():

	print("Submit pressed")
	r = float(entr.get())
	h = float(enth.get())

	v = math.pi*r*r*h
	v = round(v,3)

	output.config(state="normal")
	output.insert(tk.INSERT,v)
	output.config(state="disabled")


#***MAIN CODE BELOW ALL YOUR FUNCTIONS****




#construct a root window
root = tk.Tk() #Special function called a constructor
root.title("Volume of a Cylinder:")
#Create widgets/objects/elements
#Step 1: Construct the widget
labr = tk.Label(root, text="radius", height = 1)
#Step 2: Configure the widget
labr.config()
#Step 3: Pack the widget in the root
labr.pack()

entr = tk.Entry(root, background = "yellow")
entr.pack()

labh = tk.Label(root, text="height")
labh.pack()

enth = tk.Entry(root, background = "yellow")
enth.pack()

#We bind a function to a button
btn = tk.Button(root, text="Submit", background="yellow", command = submit)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()




#Nothing goes after this line
root.mainloop() #Pop up window and waits for you to close it




















