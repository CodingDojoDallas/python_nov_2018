class MathDojo:
    def __init__(self,):
        self.num = 0
        self.sum = 0
    def add(self, *num):
        sum = 0
        for n in num:
            self.sum = self.sum+n
        return self
    def subtract(self, *num):
        sum = 0
        for n in num:
            self.sum = self.sum-n
        return self
md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).sum
print(x)

