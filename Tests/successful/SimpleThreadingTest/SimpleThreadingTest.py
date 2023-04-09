import threading
import time

#t = threading.Thread(target= lambda: gameLoop())

#def gameLoop(*args):
#    print("hello World")
    
#t.start()
#print("started")

#t.join()
#print("joined")


class GameLoop():
    def __init__(self):
        self.thread = threading.Thread(target= lambda: self.task())
        
    def task(*args):
        print("1")
        print("2")
        print("3")
        print("4")
        print("5")
        print("6")
        print("7")
        print("8")
        print("9")
        print("10")
        
        
    def start(self):
        if not self.thread.is_alive():
            self.thread.start()
            
    def join(self):
        if self.thread.is_alive():
            self.thread.join()
        
        
        
        
def task():
        print("0")
        print("2")
        print("3")
        print("4")
        print("5")
        print("6")
        print("7")
        print("8")
        print("9")
        print("10")
        
class GameLoop2(threading.Thread):
    def __init__(self):
        super().__init__()
        print("thread Initialisation has begun")
    
    def task(self):
        print('100')
    
    def run(self, *args):
        super().run(*args)
        task()
        self.task()
        
        
class GameLoop3(threading.Thread):
    def __init__(self):
        super().__init__()
        
        print("Thread Initialised.")        
        
    def task(self):
        global PLAYERS_TURN
        for i in range(10):
            print(f"Loop Count: {i}")
            time.sleep(0.5)
            if i == 9:
                PLAYERS_TURN = True
                print(f"Players Turn is now {PLAYERS_TURN}")
            
    def run(self, *args):
        self.task()
#gameloop = GameLoop()
#gameloop2 = GameLoop2()

#gameloop.start()
#gameloop2.start()
#gameloop2.join()

PLAYERS_TURN = False

gameloop = GameLoop3()
print(f"Players Turn: {PLAYERS_TURN}")
gameloop.start()
print(f"Players Turn: {PLAYERS_TURN}")

gameloop.join()
print(f"Players Turn: {PLAYERS_TURN}")

print('Hello World')
print(f"Players Turn: {PLAYERS_TURN}")


           




