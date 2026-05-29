import random
class Tamagochi:
    
    def __init__(self,name,happiness,hunger,energy,craziness, discipline):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        self.energy = energy
        self.craziness = craziness
        self.discipline = discipline
        global traits
        traits = [happiness,hunger,energy,craziness,discipline]
    def feed(self):
        print(f"you fed {self}")
        self.hunger+=random.randint(1,2)
        self.happiness-=random.randint(1,2)
    def play(self):
        self.happiness+=random.randint(1,2)
        self.energy -= random.randint(1,2)
        print(f"{self.name} has been played with")
    def smack(self):
        self.happiness -= 10+random.randint(1,5)
        self.discipline += 1 + random.randint(1,2)
        print(f"{self.name} has been smacked")
    for i in traits:
            if i>100:
                i=100
            elif i <0:
                print(f"died of {i}")
                death = True
Tamagochis = [Tamagochi("fluffy",0,0,0,-1)]
for i in Tamagochis:
    print(i)
ans = input("wat")
while True:
    if ans == "feed":