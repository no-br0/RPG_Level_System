#from tkinter import Tk, Toplevel, END
#from tkinter.ttk import Progressbar, Style, Label, Button, Frame
import player
import time
#from customtkinter import CTkButton
#import tkinter as tk
from Console import Console
import threading
import queue
from MainWindow import MainWindow
from StatWindow import StatWindow

_statwin = True

class Util():
    def __init__(self):
        self.console_width = 1300
        self.console_height = 700
    
    
    
    def damage_player_button(*args):
        print_health = False
        if player.ALIVE:
            print_health = True
            if player.remove_health(9):
                player.vitality += 1
        else:
            mainWindow.console.add_text(f"Player Already Dead!")
                
        if print_health:
            mainWindow.console.add_text(f"Player Health: {player.health}")
            
        mainWindow.update_window()
        if _statwin and statWindow.winfo_exists():
            statWindow.update_window()
            
        
            
    def restore_player_button(*args):
        if player.health < player.maxHealth():
            player.restore_health(30)
            mainWindow.update_window()
            if _statwin and statWindow.winfo_exists():
                statWindow.update_window()
        else:
            mainWindow.console.add_text("Already at full health!")
            
                
    def player_step(*args):
        pass
        
        
    def clear_console(*args):
        mainWindow.console.clear_console()
        




class GameLoop(threading.Thread):
    def __init__(self):
        super().__init__()
        
        
    def run(self):
        pass




util = Util()

mainWindow = MainWindow(util)


if _statwin:
    statWindow = StatWindow()

mainWindow.mainloop()

if _statwin:
    statWindow.mainloop()
    