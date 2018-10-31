# print("*"*80)
# def beCheerful(name='', repeat=98):
# 	print(f"good morning {name}\n"*repeat)
# beCheerful()
# beCheerful(name="john")
# beCheerful(name="michael", repeat=5)
# beCheerful(repeat=5, name="kb")
# beCheerful(name="aa")



import random
def randInt(min=0, max=100):
    return int(random.random() * (max-min) + min)
print(randInt())


