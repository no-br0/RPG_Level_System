from UIManager import MainWindow
import tkinter
from player import health
from threading import Thread, Event
import statWindow

temp = 0

class TestThread(Thread):
    def __init__(self):
        super().__init__()
        self.event = Event()
        self.window = MainWindow(self)


    def stop(self, *args):
        self.event.set()

    def run(self):
        if not self.event.is_set():
            print(health)
            self.window.mainloop()


if __name__ == '__main__':
    thread = TestThread()
    thread.run()
    #thread.stop()

    #window = MainWindow()
    #window.mainloop()
