class mathDojo:
	def __init__(self):
		self.result = 0
	def add(self, *args):
		self.add = 0
		for i in args:
			self.add += i
		self.result += self.add
		return self
	def subtract(self, *args):
		self.subtract = 0
		for j in args:
			self.subtract += j
		self.result -= self.subtract
		return self
md = mathDojo().add(2,3,4,5,6).subtract(1,2,4,2).result
print(md)