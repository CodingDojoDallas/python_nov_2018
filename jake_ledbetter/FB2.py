# 1 - Countdown
def countDown(x):
	array = []
	while x >= 0:
		array.append(x)
		x -= 1
	return array

cd = countDown(5)
print (cd)

# 2 - print and return
def printAndReturn(arr):
	print(arr[0])
	return arr[1]

par = printAndReturn([1,2,3,4,5])
print(par)

#3 - First Plus Length
def firstPlusLen(arr):
	return arr[0] + len(arr)

fpl = firstPlusLen([1,2,3,4,5])
print(fpl)

# 4 - Values Greater than Second
def valsGreaterThanSecond(arr):
	newArr = []
	countA = 0
	if (len(arr) == 1):
		return false
	else:
		for i in range(len(arr)):
			if arr[i] > arr[1]:
				newArr.append(arr[i])
				countA = countA + 1
	print(countA)
	return newArr

vgt2 = valsGreaterThanSecond([1, 7, 8, 12, 4, 9, 3, 10])
print(vgt2)

# 5 - This Length, That value
def lengthAndValue(size, value):
	arr = []
	for i in range(size):
		arr.append(value)
	return arr

lav = lengthAndValue(4,7)
print(lav)