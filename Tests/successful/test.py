import tkinter as tk

# Create a Tkinter window
window = tk.Tk()
window.title("Text-Based Game Console")


text_x = 20
text_y = 470

move_y = -20


output_bbox = []

# Create a Canvas widget to display the text
console = tk.Canvas(window, width=1000, height=500, background='#1f1f1f')
console.pack(anchor='nw')


# Define a function to add text to the console
def add_text(text):
    global text_x, text_y
    global output_bbox
    
    move_text()
    
    output_bbox.append(console.create_text(
        text_x, text_y, 
        anchor='nw', 
        text=text, fill='lightgreen', font="Times 12 bold"))

# Define a function to clear the console
def clear_console():
    console.delete("all")

# Define a function to handle user input
def handle_input(input_text):
    # Process the user's input
    add_text("> " + input_text)
    input_entry.delete(0,tk.END)


def move_text():
    for i in output_bbox:
        console.move(i, 0, move_y)
    

# Display some text in the console
#add_text("Welcome to the Text-Based Game!")

# Create an entry widget for the user's input
input_entry = tk.Entry(window, width=100, background='lightgray')
input_entry.pack(side=tk.BOTTOM, anchor='s')

# Bind the Return key to the input_entry widget to handle user input
input_entry.bind("<Return>", lambda event: handle_input(input_entry.get()))


# Start the Tkinter event loop
window.mainloop()
