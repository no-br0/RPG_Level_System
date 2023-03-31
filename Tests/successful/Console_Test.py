import tkinter as tk

class Console(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.text_x = 20
        self.text_y = 470
        self.move_y = -20
        
        self.text_bbox = []
        
        self.canvas = tk.Canvas(self, width=1000, height=500, background='#1f1f1f')
        self.canvas.pack(anchor='nw')
        
        self.input_entry = tk.Entry(self, width=100, background='lightgray')
        self.input_entry.pack(side=tk.BOTTOM, anchor='s')
        
        self.input_entry.bind('<Return>', lambda event: self.handle_input(self.input_entry.get()))
    
    
    def move_text(self):
        for i in self.text_bbox:
            self.canvas.move(i, 0, self.move_y)
    
    def clear_console(self):
        self.canvas.delete('all')
    
    def add_text(self,text):
        self.move_text()
        
        self.text_bbox.append(self.canvas.create_text(
            self.text_x, self.text_y,
            anchor='nw',
            text=text, fill='lightgreen', font='Times 12 bold'))
        
    def handle_input(self, input_text):
        self.add_text("> " + input_text)
        self.input_entry.delete(0,tk.END)
        
        
    
    
window = tk.Tk()
window.title("Text-Based-Game-Console")
window.resizable(False,False)
console = Console(window)
console.pack()

window.mainloop()