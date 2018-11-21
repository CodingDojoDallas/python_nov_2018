class Animal:
    def __init__(self):
        self.name = "cat"
        self.health = 70
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print(str(self.health))
        return self

cat = Animal()
cat.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = "Dog"
        self.health = 150
    def pet(self):
        self.health += 5
        return self
dog = Dog()
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self):
        super().__init__()
        self.name = "Dragon"
        self.health = 150
    def fly(self):
        self.health -= 10
        return self
    def healthDisplay(self):
        print(str(self.health))
        print("I am a Dragon")
        return self
dragon = Dragon()
dragon.walk().walk().run().fly().healthDisplay()
