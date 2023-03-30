from tkinter import Tk, Button, Text, Toplevel
from tkinter.ttk import Progressbar, Frame, Style, Label
import player
import time


_statwin = True



def damage_player_button():
    if player.remove_health(1):
        player.vitality += 1
    mainWindow.update_window()
    if _statwin and statWindow.winfo_exists():
        statWindow.update_window()
        
        
        
def restore_player_button():
    player.restore_health(10)
    mainWindow.update_window()
    if _statwin and statWindow.winfo_exists():
        statWindow.update_window()
    


class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Game Window')
        self.geometry('900x450+700+200')
        self.resizable(False,False)
        
        self.config(background="#d3d3d3")


        self.health = Label(self, border=0, text=f"Health: {player.health}/{player.maxHealth()}")
        self.health.configure(background="#d3d3d3")
        self.health.pack(padx=(15,0), pady=(15,0), anchor='w')


        self.damage_button = Button(self, 
                             border=3, 
                             relief='ridge', 
                             text="Damage Player", 
                             command= lambda: damage_player_button())
        self.damage_button.pack(pady=(5,5), padx=20, anchor='w')
        
        self.restore_button = Button(self,
                                     border=3,
                                     relief='ridge',
                                     text="Drink Health Potion",
                                     command= lambda: restore_player_button())
        self.restore_button.pack(pady=(5,20), padx=20, anchor='w')
        
    def update_window(self):
        self.health.config(text=f'Health: {player.health}/{player.maxHealth()}')




class StatWindow(Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Stat Window')
        self.geometry('400x600+200+200')
        self.resizable(False,False)
        
        self.config(background='#d3d3d3')
        
        self.bg1 = '#e1e1e1'
        
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
        self.health.pack(anchor='w')
        
        self.maxhealth = Label(self.frame, style="Background.TLabel")
        self.maxhealth.pack(anchor='w')
        
        self.gap1 = Label(self.frame, style="Background.TLabel")
        self.gap1.pack(anchor='w')
        
        self.vitality = Label(self.frame, style="Background.TLabel")
        self.vitality.pack(anchor='w')
        
        self.strength = Label(self.frame, style="Background.TLabel")
        self.strength.pack(anchor='w')
        
        self.agility = Label(self.frame, style="Background.TLabel")
        self.agility.pack(anchor='w')
        
        self.dexterity = Label(self.frame, style="Background.TLabel")
        self.dexterity.pack(anchor='w')
        
        
        self.update_window()
        
        
    #used to update the data for all of the players stats at once
    def update_window(self):
        self.health.config(text=f'Health: {player.health}')
        self.maxhealth.config(text=f'Max Health: {player.maxHealth()}')
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