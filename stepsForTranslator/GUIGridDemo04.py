import tkinter as tk

root = tk.Tk()	#Tk() is a special method called a constructor




lab = tk.Label(root, text = "Enter a number;")


lab.grid(row = 0, column = 0)


ent = tk.Entry(root)

ent.grid(row = 1, column = 0)


btn = tk.Button(root, text = "Press Me")
btn.grid(row = 2, column = 0)

output = tk.Text(root)
output.configure(state = "disabled")
output.grid(row = 1, column = 1, rowspan = 3)







root.mainloop()