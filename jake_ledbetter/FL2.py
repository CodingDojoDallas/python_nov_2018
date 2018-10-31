# 1 - Biggie Size(
def makeItBig(arr):
	for i in range(len(arr)):
		if (arr[i] > 0):
			arr[i] = "big"
	return arr

mib = makeItBig([1,0,-3,3,3])
print(mib)

# 2 - Count Positives
def countPositives(arr):
	count = 0
	for i in range(len(arr)):
		if arr[i] > 0 :
			count += 1
	arr[len(arr)-1] = count
	return arr
cp = countPositives([1,2,-2,-5,4])
print(cp)

# 3 - sumTotal
def sumTotal(arr):
	sumA = 0
	for i in range(len(arr)):
		sumA += arr[i]
	return sumA

st = sumTotal([1,2,3,4,5,6,7])
print(st)

# 4 - Average
def average(arr):
	avg = 0
	for i in range(len(arr)):
		avg += arr[i]
	return avg / len(arr)

a = average([1,2,3,4])
print(a)

# 5 - Length
def length(arr):
	return len(arr)

l = length([1,2,3,4,5])
print(l)

# 6 - Minimum
def minimum(arr):
	if len(arr) == 0:
		return false
	else:
		min = arr[0]
		for i in range(len(arr)):
			if arr[i] < min:
				min = arr[i]
		return min

m = minimum([12,3,45,32,2,7,8])
print(m)

# 7 - Maximum
def maximum(arr):
	if len(arr) == 0:
		return false
	else:
		max = arr[0]
		for i in range(len(arr)):
			if arr[i] > max:
				max = arr[i]
		return max

mx = maximum([12,3,45,32,2,7,8])
print(mx)

# 8 UltimateAnalyze

def ultimateAnalyze(arr):
	min = arr[0]
	max = arr[0]
	avg = 0
	sumTotal = 0
	dictionary={}
	for i in range(len(arr)):
		if min > arr[i]:
			min = arr[i]
		if max < arr[i]:
			max = arr[i]
		sumTotal += arr[i]
		avg += arr[i]
	avg = avg / len(arr)
	dictionary["sumTotal"] = sumTotal
	dictionary["average"] = avg
	dictionary["minimum"] = min
	dictionary["maximum"] = max
	dictionary["length"] = len(arr)
	return dictionary

ult = ultimateAnalyze([1,2,3,4,5,6,7,8,9,10,11,12,13])
print(ult)

# 9 Reverse Array
def reverseList(arr):
	for i in range(int(len(arr)/2)):
		temp = arr[i]
		arr[i] = arr[len(arr)-1-i]
		arr[len(arr)-1-i] = temp
	return arr

rl = reverseList([1,2,3,4,5,6,7])
print(rl)