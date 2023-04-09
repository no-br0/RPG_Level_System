from Console import Console
import player
from tkinter.ttk import Frame, Style
from customtkinter import CTkButton
from tkinter import Tk

class MainWindow(Tk):
    def __init__(self, util, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('Game Window')
        self.geometry('1400x1000+800+200')
        self.resizable(False,False)
        
        self.config(background=("#404040"))


        self.buttonStyle = Style()
        self.buttonStyle.configure('basic.TButton',border=3, relief='ridge', outline = 'red', anchor='nw')

        
        self.console = Console(self, util.console_width, util.console_height)
        self.console.pack()
        
        self.button_frame = Frame(self)
        self.button_frame.pack(pady=20)
        
        
        self.damage_button = CTkButton(self.button_frame, 
                                        text="Damage Player", 
                                        command= lambda: util.damage_player_button(),
                                        fg_color="#303030",
                                        bg_color='#404040')
        self.damage_button.pack()
        
        self.restore_button = CTkButton(self.button_frame,
                                        text="Drink Health Potion",
                                        command= lambda: util.restore_player_button(),
                                        fg_color='#303030',
                                        bg_color='#404040')
        self.restore_button.pack()
        
        self.step_button = CTkButton(self.button_frame,
                                     text="Step",
                                     command= lambda: util.player_step(),
                                     fg_color='#303030',
                                     bg_color='#404040')
        self.step_button.pack()
        
        self.clearConsole_button = CTkButton(self.button_frame,
                                             text="Clear Console",
                                             command= lambda: util.clear_console(),
                                             fg_color="#303030",
                                             bg_color="#404040")
        self.clearConsole_button.pack()

        
    def update_window(self):
        #self.health.config(text=f'Health: {player.health}/{player.maxHealth()}')
        pass
    