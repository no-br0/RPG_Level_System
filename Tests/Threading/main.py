import Console
import tkinter as tk
from GameLoop import GameLoop
import atexit


def action(*args):
    if not gameloop.wait_event.is_set():
        gameloop.wait_event.set()


root = tk.Tk()
root.resizable(False,False)


console = Console.Console(root,500,500)
console.pack()

gameloop = GameLoop(console=console)
gameloop.daemon = True
gameloop.start()


def exit_handler():
    print("Calling Exit Handler")
    gameloop.stop_event.set()
    gameloop.exit_handler()

root.bind('<space>', lambda event: action())
#atexit.register(lambda: exit_handler())

root.mainloop()



