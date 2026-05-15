import random
class Animal:
    def __init__(self,name,species,food,sound,height,weight):
        self.name = name
        self.species = species
        self.food = food
        self.sound = sound
        self.height = height
        self.weight = weight
    def eat_food(self):
        print(f"{self.name} is eating {self.food}")
    def self_intro(self):
        print(f"I am {self.name}, I am a {self.species} and invite you to eat {self.food}. {self.sound}!")
    def health_checkup(self):
        self.height += (random.randint(-10,10))
        self.weight += (random.randint(-10,10))
        print(f"{self.name} is {self.weight}kg and {self.height}cm tall")
lion = Animal("leo","lion","meat","roars", 100,190)
rabbit = Animal("rebecca","rabbit","vegetables","purrs",50,8)
lion.self_intro()
rabbit.self_intro()
