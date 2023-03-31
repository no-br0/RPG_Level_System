import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# create a ttk label without any text
label = ttk.Label(root)

# set the width of the label to a large value
label.configure(width=10, background='blue')

# set the anchor option to 'n'
label.configure(anchor='n')

# pack the label into the root window
label.place(height=100, x=100, y=100)

root.mainloop()
