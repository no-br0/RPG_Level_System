import threading
import time
import atexit

class GameLoop(threading.Thread):
    def __init__(self, console, *args, **kwargs):
        super(GameLoop, self).__init__(*args, **kwargs)
        self.console= console
        self.wait_event = threading.Event()
        self.stop_event = threading.Event()
        #atexit.register(lambda : self.exit_handler())
        
        
    def run(self):
        
        while not self.stop_event.is_set():
            self.console.add_text("Gameloop Started")
        
            self.wait_event.wait()
            #if self.stop_event.is_set():
            #    continue
            
            print("Loop")
            self.console.add_text("Gameloop Ended")
            time.sleep(0.5)
            self.console.clear_console()
            self.wait_event.clear()
        
        print("ready To Join")
        #doesnt execute when the thread is killed
        #for i in range(10):
        #    print(f"After: {i}")
        #    time.sleep(1)
        #self.join()
            
    
    def exit_handler(self):
        print("Calling Internal Exit Handler")
        self.stop()
    
    def stop(self):
        print("Stop Has Been Called")
        self.stop_event.set()
        self.wait_event.set()
        print('Thread Stopped')
        #self.join()
            


