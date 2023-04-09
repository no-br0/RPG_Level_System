from Console import Console
import player
from tkinter import ttk 
#from customtkinter import CTkButton
import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self, util, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('Game Window')
        self.geometry('1400x1000+800+200')
        self.resizable(False,False)
        
        self.config(background=("#404040"))


        self.buttonStyle = ttk.Style()
        self.buttonStyle.configure('TButton',border=3, relief='ridge', anchor='n', background='#404040', foreground='#303030')
        
        self.buttonStyle.map('TButton',
                             foreground=[('active', '#303030')],
                             background=[('active', '#404040')])
        
        
        
        self.buttonFrame_style = ttk.Style()
        self.buttonFrame_style.configure('TFrame', background='#505050', foreground='#303030')

        
        self.console = Console(self, util.console_width, util.console_height)
        self.console.pack()
        
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(pady=20)
        
        #foreground = '#303030'
        #background = '#404040'
        
        self.damage_button = ttk.Button(self.button_frame, 
                                        text="Damage Player",
                                        style='TButton',
                                        command= lambda: util.damage_player_button())
        self.damage_button.pack(padx=10, pady=(10,3))
        
        self.restore_button = ttk.Button(self.button_frame,
                                        text="Drink Health Potion",
                                        style='TButton',
                                        command= lambda: util.restore_player_button())
        self.restore_button.pack(padx=10, pady=3)
        
        self.step_button = ttk.Button(self.button_frame,
                                     text="Step",
                                     style='TButton',
                                     command= lambda: util.player_step())
        self.step_button.pack(padx=10, pady=3)
        
        self.clearConsole_button = ttk.Button(self.button_frame,
                                             text="Clear Console",
                                             style='TButton',
                                             command= lambda: util.clear_console())
        self.clearConsole_button.pack(padx=10, pady=(3,10))

        
    def update_window(self):
        #self.health.config(text=f'Health: {player.health}/{player.maxHealth()}')
        pass
    