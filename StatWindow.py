from tkinter import Toplevel
from tkinter.ttk import Style, Frame, Label
import player

class StatWindow(Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Stat Window')
        self.geometry('600x1000+100+200')
        self.resizable(False,False)
        
        self.config(background='#303030')
        
        self.bg1 = '#505050'
        
        self.style= Style()
        self.style.configure('Border.TFrame', 
                             background=self.bg1)
        
        
        self.statStyle = Style()
        self.statStyle.configure("Background.TLabel",background=self.bg1, foreground='lightgreen')
        
        
        
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
