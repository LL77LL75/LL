import random
thing = input(f"what do you want to do")
class Fighter:
    def __init__(self,name,health,strength,amour,skill,mana,Mionon):
        self.name = name
        self.health = health
        self.strength = strength
        self.amour= amour
        self.skill =skill
        self.mana = mana
        self.mionon = Minion
        if random.randint(100)<=20:
            damage*=1.2
        self.isAlive = True
    def attack(self,target):
        damage_done = self.damage + random.randint(-2,2) - target.amour
        target.health -= damage_done
        print(f"{target.name} has recieved {damage_done} damage from {self.name}")
    def use_skill(self,target):
        if self.mana >=5:
            if self.skill == "power slash":
                damage_done = self.damage + random.randint(-2,2) - target.amour
                target.health -= damage_done
                self.mana -=5
            if self.skill == "double damage":
                damage_done = 2*self.damage + random.randint(-2,2) - target.amour
                target.health -= damage_done
                self.mana -=5
        else:
            print(f"insufficient mana to use {self.skill}")
    def Mionion_attack(mionon):
        mionon.attack()
    def Mionion():
        if Minion >=1:
            return True
        else:
            return False
class Minion:
    def __init__(self,name,health,strength,amour):
        self.name = name
        self.health = health
        self.strength = strength
        self.amour= amour
        if random.randint(100)<=20:
            damage*=1.2
        self.isAlive = True
    def minion_attack(self,target):
        damage_done = self.damage + random.randint(-2,2) - target.amour
        target.health -= damage_done
        print(f"{target.name} has recieved {damage_done} damage from {self.name}")
my_guy = Fighter("my guy",100,10,5,"double damage",10)
enemy_guy = Fighter("dragon night",150,8,8,"power slash",15)
turn = "my_guy"
while my_guy.isAlive() == True and enemy_guy.isAlive() == True:
    if turn == "my_guy":
        thing = input(f"what do you want to do")
        if thing == "attack":
            if enemy_guy.Mionion():
                my_guy.attack(my_guy,enemy_guy.Mionion)
            my_guy.attack(my_guy,enemy_guy)
