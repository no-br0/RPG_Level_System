import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create a style object for the label widget
style = ttk.Style()
style.configure("TLabel", background='blue')

# Create the label widget with the desired dimensions
label = ttk.Label(root, text="This is a label widget\nh\nh\nh\nh\nh\nh\nh\nh\nh\nh\nh\nh\nh\nh\nh\nh\nh", style="TLabel", anchor='sw')
label.place(width=800, height=500)

label.config(text='Hello World')


root.mainloop()
