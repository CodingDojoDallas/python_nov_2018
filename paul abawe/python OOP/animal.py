class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print ("health is " + str(self.health))
        return self

class Dog(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 150

    def pet(self):
        self.health += 5
        return self


class Dragon(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        super().displayHealth()
        print("I am a Dragon")


animal1 = Animal("Oliver", 100)
animal1.walk().walk().walk().run().run().displayHealth()

dog1 = Dog("Sparky", 1)
dog1.walk().walk().walk().run().run().pet().displayHealth()

dragon1 = Dragon("Rooster", 300)
dragon1.fly().fly().displayHealth()