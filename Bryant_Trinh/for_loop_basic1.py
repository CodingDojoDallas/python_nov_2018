#1
for i in range(151):
	print(i)
#2
for i in range(5,1000001,5):
	print(i)
#3
for i in range(1,101):
	if i % 5==0:
		print("Coding")
	if i % 10==0:
		print("Dojo")
	else: 
		print(i)
#4
sum=0
for i in range(1,500000,2):
	sum+=i
print(sum)
#5
for i in range(2018,0,-4):
	print(i)
#6
def function(lowNum, highNum, mult):
	for i in range(lowNum, highNum, mult):
		print(i)
function(3,10,3)		