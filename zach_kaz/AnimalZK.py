class animal:
    def __init__(self,name,health):
        self.name=name
        self.health=health
    def walk(self):
        self.health-=1
        return self
    def run(self):
        self.health-=5
    def displayhealth(self):
        print(self.name+"'s health is "+str(self.health))

mammal=animal("Mammal",50)
mammal.walk()
mammal.walk()
mammal.walk()
mammal.run()
mammal.run()
mammal.displayhealth()

class dog(animal):
    def __init__(self,name,health):
        super().__init__(name,health)
        self.health=150
    def pet(self):
        self.health-=5
        return self

Fido=dog("Fido",10000000)
Fido.walk()
Fido.walk()
Fido.walk()
Fido.run()
Fido.run()
Fido.displayhealth()

class dragon(animal):
    def __init__(self,name,health):
        super().pet(name,health)
        self.health=170
    def fly(self):
        self.health-=10
    def displayhealth(self):
        super().displayhealth()
        print("I am a Dragon")
        return self

dracayrs=dragon('dracayrs',500000)
dracayrs.fly()
dracayrs.fly()
dracayrs.fly()
dracayrs.fly()
dracayrs.displayhealth()

cat=animal("Cat",30)
#cat.fly()
#cat.pet
cat.displayhealth()
#dog.fly()
