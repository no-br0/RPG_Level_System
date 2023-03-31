from tkinter import Tk, Text, Toplevel, END
from tkinter.ttk import Progressbar, Frame, Style, Label, Button
import player
import time
from customtkinter import CTkButton
import tkinter as tk
from Console import Console


_statwin = True

console_width = 1300
console_height = 700


def damage_player_button():
    if player.remove_health(9):
        player.vitality += 1
        mainWindow.console.add_text(f"Player Health: {player.health}")
        
    mainWindow.update_window()
    if _statwin and statWindow.winfo_exists():
        statWindow.update_window()
        
        
        
        
def restore_player_button():
    player.restore_health(10)
    mainWindow.update_window()
    if _statwin and statWindow.winfo_exists():
        statWindow.update_window()
        
        
        

def player_step():
    
    pass
    


        


class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        global console_width, console_height
        
        self.title('Game Window')
        self.geometry('1400x1000+800+200')
        self.resizable(False,False)
        
        self.config(background=("grey"))


        #self.health = Label(self, border=0, text=f"Health: {player.health}/{player.maxHealth()}", background="#d3d3d3")
        #self.health.pack(padx=(15,0), pady=(15,0), anchor='w')
        self.buttonStyle = Style()
        self.buttonStyle.configure('basic.TButton',border=3, relief='ridge', outline = 'red', anchor='nw')

        
        self.console = Console(self, console_width, console_height)
        self.console.pack()
        
        
        self.damage_button = CTkButton(self, 
                                        text="Damage Player", 
                                        command= lambda: damage_player_button())
        self.damage_button.pack()
        
        self.restore_button = CTkButton(self,
                                        text="Drink Health Potion",
                                        command= lambda: restore_player_button())
        self.restore_button.pack()
        
        self.step_button = CTkButton(self,
                                     text="Step",
                                     command= lambda: player_step())
        self.step_button.pack()
        
    def update_window(self):
        #self.health.config(text=f'Health: {player.health}/{player.maxHealth()}')
        pass











class StatWindow(Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Stat Window')
        self.geometry('600x1000+100+200')
        self.resizable(False,False)
        
        self.config(background='grey')
        
        self.bg1 = '#cfcfcf'
        
        self.style= Style()
        self.style.configure('Border.TFrame', background=self.bg1, relief='solid', foreground = "blue", borderwidth = 10)
        
        self.statStyle = Style()
        self.statStyle.configure("Background.TLabel",background=self.bg1)
        
        
        
        self.frame = Frame(self, style='Border.TFrame', padding=(25,15,25,15))
        self.frame.pack(anchor='w', padx=30, pady=30)
        
        
        
        self.frameTitle = Label(self.frame, text=f'Player Stats', style="Background.TLabel")
        self.frameTitle.configure(font=("Times", 14, "bold", "italic"))
        self.frameTitle.pack(padx=0, pady=(0,10), anchor='n')
        
        self.health = Label(self.frame, style="Background.TLabel")
        self.health.configure(font=("Times",10))
        self.health.pack(anchor='w')
        
        self.maxhealth = Label(self.frame, style="Background.TLabel")
        self.maxhealth.configure(font=("Times",10))
        self.maxhealth.pack(anchor='w')
        
        self.movespeed = Label(self.frame, style="Background.TLabel")
        self.movespeed.configure(font=("Times",10))
        self.movespeed.pack(anchor='w')
        
        self.gap1 = Label(self.frame, style="Background.TLabel")
        self.gap1.pack(anchor='w')
        
        self.vitality = Label(self.frame, style="Background.TLabel")
        self.vitality.configure(font=("Times",10))
        self.vitality.pack(anchor='w')
        
        self.strength = Label(self.frame, style="Background.TLabel")
        self.strength.configure(font=("Times",10))
        self.strength.pack(anchor='w')
        
        self.agility = Label(self.frame, style="Background.TLabel")
        self.agility.configure(font=("Times",10))
        self.agility.pack(anchor='w')
        
        self.dexterity = Label(self.frame, style="Background.TLabel")
        self.dexterity.configure(font=("Times",10))
        self.dexterity.pack(anchor='w')
        
        
        self.update_window()
        
        
    #used to update the data for all of the players stats at once
    def update_window(self):
        self.health.config(text=f'Health: {player.health}')
        self.maxhealth.config(text=f'Max Health: {player.maxHealth()}')
        self.movespeed.config(text=f'Move Speed: {player.moveSpeed()}')
        self.vitality.config(text=f'Vitality: {player.vitality}')
        self.strength.config(text=f'Strength: {player.strength}')
        self.agility.config(text=f'Agility: {player.agility}')
        self.dexterity.config(text=f'Dexterity: {player.dexterity}')
        pass







mainWindow = MainWindow()

if _statwin:
    statWindow = StatWindow()

mainWindow.mainloop()

if _statwin:
    statWindow.mainloop()