from UIManager import MainWindow
import tkinter
from player import health
from threading import Thread, Event

temp = health

class TestThread(Thread):
    def __init__(self):
        super().__init__()
        self.event = Event()
        self.window = MainWindow()


    def stop(self):
        self.event.set()

    def run(self):
        if not self.event.is_set():
            print(health)
            self.window.mainloop()


if __name__ == '__main__':
    #thread = TestThread()
    #thread.run()
    window = MainWindow()
    window2 = MainWindow()

    window.mainloop()
    window2.mainloop()