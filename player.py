
ALIVE = True

vitality = 0
strength = 0
agility = 0
dexterity = 0

health = 50
maxHealth = lambda: (50 + (vitality // 10))

moveSpeed = lambda: (1 + (agility // 20))

def remove_health(num):
    global health, ALIVE
    if ALIVE:
        if (health - num) >= 0:
            health -= num
            if health == 0:
                ALIVE = False
            return True
        else:
            health = 0
            ALIVE = False
            return False
    else:
        print("player already dead")
        return False
        
def restore_health(num):
    global health, ALIVE
    if (health + num) <= maxHealth():
        health += num
        if not ALIVE:
            ALIVE = True
    else:
        if health < maxHealth():
            health = maxHealth()
        else:
            print("Full Health")