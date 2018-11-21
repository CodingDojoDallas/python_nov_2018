#Functions Intermediate I
import random
def randInt():
	return int(random.random()*100)+1

oneTo100 = randInt()
print(oneTo100)

def randIntMax50():
	return int(random.random()*50)+1

oneTo50 = randIntMax50()
print(oneTo50)

def fiftyTo100():
	return int(random.random()*50)+51
fiftyToHund = fiftyTo100()
print(fiftyToHund)

def fiftyTo500():
	return int(random.random()*450)+51
fiftyToFive = fiftyTo500()
print(fiftyToFive)
