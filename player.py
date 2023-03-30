
ALIVE = True

vitality = 0
strength = 0
agility = 0
dexterity = 0

health = 50
maxHealth = lambda: (50 + (vitality // 10))

moveSpeed = lambda: (1 + agility // 20)

def remove_health(num):
    global health
    global ALIVE
    if ALIVE:
        if (health - num) > 0:
            health -= num
        else:
            health = 0
            ALIVE = False
    else:
        print("player already dead")    
        
def restore_health(num):
    global health
    if health + num < maxHealth():
        health += num
    else:
        health = maxHealth()