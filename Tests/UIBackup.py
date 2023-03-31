from tkinter import Tk, Text, Toplevel, END
from tkinter.ttk import Progressbar, Frame, Style, Label, Button
import player
import time
from customtkinter import CTkButton


_statwin = True



def damage_player_button():
    if player.remove_health(9):
        player.vitality += 1
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
    

class Console(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        #self.output = []
        
        #self.output = Text(self, width=100, height=15)
        #self.output.insert(END,"Hello World\n")
        #self.output.insert(END,"Hello World\n")
        #self.output.pack()
        
        #for i in range(20):
        #    self.output.append(Label(self,width=150))
        #    self.output[i].pack()
            
        #self.set_output(0,"Hello World")
        
        self.output_style = Style()
        self.output_style.configure('output.TLabel', height=100, width=50)
        
        self.output = Label(self, style='output.TLabel', text="Hello World\nh\nh")
        self.output.place(anchor='sw', height=100, width=100)
        
        self.style = Style()
        self.style.configure('frame.TFrame',background='black', ipadx=10, height=20, width=20, border=10, relief='ridge')
        
        self.config(style='frame.TFrame')
        
    def set_output(self, num, txt):
        num = (10-1)-num
        self.output[num].config(text=txt)
        


class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Game Window')
        self.geometry('1000x800+800+200')
        self.resizable(False,False)
        
        self.config(background=("grey"))


        #self.health = Label(self, border=0, text=f"Health: {player.health}/{player.maxHealth()}", background="#d3d3d3")
        #self.health.pack(padx=(15,0), pady=(15,0), anchor='w')
        self.buttonStyle = Style()
        self.buttonStyle.configure('basic.TButton',border=3, relief='ridge', outline = 'red', anchor='nw')

        
        self.console = Console(self)
        self.console.place(height=100, width=100, x=450)
        
        
        self.damage_button = CTkButton(self, 
                                        text="Damage Player", 
                                        command= lambda: damage_player_button())
        self.damage_button.pack(pady=(5,5), padx=20, anchor='w')
        
        self.restore_button = CTkButton(self,
                                        text="Drink Health Potion",
                                        command= lambda: restore_player_button())
        self.restore_button.pack(pady=(5,5), padx=20, anchor='w')
        
        self.step_button = CTkButton(self,
                                     text="Step",
                                     command= lambda: player_step())
        self.step_button.pack(pady=(5,20), padx=20, anchor='w')
        
    def update_window(self):
        #self.health.config(text=f'Health: {player.health}/{player.maxHealth()}')
        pass




class StatWindow(Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Stat Window')
        self.geometry('550x800+200+200')
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