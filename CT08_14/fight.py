import random
class Fighter:
    def __init__(self,name,health,strength,amour,skill,mana):
        self.name = name
        self.health = health
        self.strength = strength
        self.amour= amour
        self.skill =skill
        self.mana = mana
        if random.randint(100)<=20:
            damage*=1.2
        self.isAlive = True
    def attack(self,target):
        damage_done = self.damage + random.randint(-2,2) - target.amour
        target.health -= damage_done
        print(f"{target.name} has recieved {damage_done} damage from {self.name}")
my_guy = Fighter("my guy",100,10,5,"double damage",10)
enemy_guy = Fighter("dragon night",150,8,8,"roar",15)