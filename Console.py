from tkinter import Frame, Canvas

class Console(Frame):
    def __init__(self, parent, width, height, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.text_x = 20
        self.text_y = height - 30
        self.move_y = -20
        
        self.text_bbox = []
        
        self.canvas = Canvas(self, width=width, height=height, background='#1f1f1f', relief="sunken")
        self.canvas.pack(anchor='nw', ipady=10, ipadx=10)

    
    
    def move_text(self):
        for i in self.text_bbox:
            self.canvas.move(i, 0, self.move_y)
    
    def clear_console(self):
        self.canvas.delete('all')
        self.text_bbox.clear()
    
    def add_text(self,text):
        self.move_text()
        text = ("> " + text)
        
        self.text_bbox.append(self.canvas.create_text(
            self.text_x, self.text_y,
            anchor='nw',
            text=text, fill='lightgreen', font='Times 12 bold'))
        