#1 - basic
for count in range(0,151):
	print (count)

#2 multiples of five
for countF in range(5,1000001,5):
	print (countF)

#3 counting the dojo way
for countD in range(1,101):
	if (countD % 10) == 0:
		print ("Coding Dojo")
	elif (countD % 5) == 0:
			print("Coding")
	else:
		print(countD)

#4 Whoa. That sucker's huge
oddSum = 0;
for countO in range(1, 500001, 2):
	oddSum  += countO
print(oddSum)

#5 countdown by fours
year = 2918
while year > 0:
	print(year)
	year -= 4

#flexible countdown
def flexibleCountdown(lowNum, highNum, mult):
	for countM in range(lowNum, highNum+1):
		if countM % mult == 0:
			print (countM);

flexibleCountdown(2,9,3);