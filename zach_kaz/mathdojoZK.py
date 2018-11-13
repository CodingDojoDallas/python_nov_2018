# def varargs(arg1, *args):
#     print("Got "+arg1+" and "+ ", ".join(args))
# varargs("one") # output: "Got one and "
# varargs("one", "two") # output: "Got one and two"
# varargs("one", "two", "three") # output: "Got one and two, three"
# varargs("one","two","three","four","infinity")

class MathDojo:
    def __init__(self):
        self.value=0
    def add(self,arg1,*args):
        self.value+=arg1+sum(args)
        return self
    def subtract(self,arg1,*args):
        self.value-=(arg1+sum(args))
        return self
    def result(self):
        return self.value


md=MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result()
print(x)
# print(something.value)
# something.add(3,4,5,6)
# print(something.value)