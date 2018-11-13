def countDown(num):
    list = []
    for i in range(num,-1,-1):
            # print(i)
        list.append(i)
        print(list)
        return list        
countDown(9)

def printReturn(num):
    print(num[0])
    return(num[1])
printReturn([9,1])


def firstPlusLength(list):
    sum = 0
    for i in range(len(list)):
        sum = list[0] + len(list)
    print(sum)
    return sum  
firstPlusLength([1,2])


def valGreaterSecond(list1):
    if len(list1) < 2:
        print("false!!")
        return False
    else:
        list2 = []
        for i in list1:
            if i > list1[1]:
                list2.append(i)
        print(list2)
        return list2        
valGreaterSecond([2,3,2,5,7,8,6])

def lengthAndValue(size,value):
    list = []
    for i in range(size):
        list.append(value)
    print(list)
    return list        
lengthAndValue(4,7)



