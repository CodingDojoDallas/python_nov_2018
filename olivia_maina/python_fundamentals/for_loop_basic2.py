# Biggie Size - Given an array, write a function that changes all positive numbers in the array to 
# "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].
def biggie(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = 'Big'
    return arr
print(biggie([-1,3,5,-5]))

#Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, 
# countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).
def positives(arr):
    total = 0
    for i in range(len(arr)):
        if arr[i]>0:
            total += 1
    arr[len(arr)-1] = total
    return arr 
print(positives([-1,1,1,1]))

#SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  
# For example sumTotal([1,2,3,4]) should return 10
def sumtotal(arr):
    sum=0
    for i in range(len(arr)):
        sum += arr[i]
    return sum
print(sumtotal([1,2,3,4]))

#Average - Create a function that takes an array as an argument and returns the average of all the values in the
#  array.  For example multiples([1,2,3,4]) should return 2.5

def average(arr):
    avg=0
    for i in range(len(arr)):
        avg += arr[i]
    return avg/len(arr)
print(average([1,2,3,4]))

#Length - Create a function that takes an array as an argument and returns the length of the array. 
#  For example length([1,2,3,4]) should return 4
def length(arr):
    return len(arr)
print(length([1,2,3,4]))

# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array
#  is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def minimum(arr):
    min = arr[0]
    if len(arr) < 1:
        return False
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min
print(minimum([1,2,3,4]))

#Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If 
# the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4;
#  maximum([-1,-2,-3]) should return -1.
def maximum(arr):
    max = arr[0]
    if len(arr) < 1:
        return False
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max
print(maximum([1,2,3,4]))

# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, 
# average, minimum, maximum and length of the array.
def UltimateAnalyze(arr):
    dict = {'sumTotal'= 0, 'average' = 0, 'minimum' = 0, 'maximum' = 0, 'length'=len(arr)}
    for count in range(len(arr)):
        dict['sumtotal'] += arr[count]
        if arr[count] > dict['max']:
            dict['max'] = arr[count]
        if arr[count] < dict['min']:
            dict['min'] = arr[count]
    dict['average'] = dict['sumtotal']/len(arr)
    return dict
print(UltimateAnalyze([82, 1, -4, 7,12]))

#ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.
#   Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return 
# [4,3,2,1]. This challenge is known to appear during basic technical interviews.

def reverse(arr):
    for count in range(round(len(arr)/2)):
        x = arr[count]
        arr[count] = arr[len(arr)-1-count]
        arr[len(arr)-1-count] = x
    return arr
print(reverse([1,2,3,4,5]))

