from SimpleThreadingTest import GameLoop, GameLoop2



print("Before Creating GameLoop")
gameloop = GameLoop()
print("After Creating GameLoop")


print("Start Game Loop 1")
gameloop.start()
print("start")
print("before Join")
gameloop.join()
print("join")
print("End Game Loop 1\n\n")






print("Before Creating GameLoop 2")
gameloop2 = GameLoop2()
print("After Creating Game Loop 2")


print("Start Game Loop 2")
if not gameloop2.is_alive():
    gameloop2.start()
print("start")
print("before Join")
if gameloop2.is_alive():
    gameloop2.join()
    pass
print("join")
print("End Game Loop 2\n\n")