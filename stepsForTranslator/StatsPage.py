import tkinter as tk

root = tk.Tk()

output = tk.Text(root, background = "blue", height = 10, width = 50)
output.config(state = "disable")
output.grid(row = 0, column = 0, columnspan = 2)



root.mainloop()