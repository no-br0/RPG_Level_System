from tkinter import Tk, Button, Label, Text
from tkinter.ttk import Progressbar, Frame
import player
import time


def button_click(label:Label):
    player.health -= 1
    player.vitality += 1
    label.config(text=f"Health: {player.health}/{player.maxHealth()}")
    #time.sleep(5)



class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Main Window')
        self.geometry('500x350')
        self.resizable(False,False)


        self.healthLabel = Label(self, border=0, text=f"Health: {player.health}/{player.maxHealth()}")
        self.healthLabel.pack(anchor='w', padx=10, pady=10)


        self.button = Button(self, border=5, text="Click", command= lambda: button_click(self.healthLabel))
        self.button.pack(pady=20, padx=20)
