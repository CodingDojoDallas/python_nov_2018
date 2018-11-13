def biggie(arr):
    for i in arr:
        if i>0:
            arr[i]="big"
    return arr

def countpos(arr):
    temp=0
    for i in arr:
        if arr[i]>0:
            temp+=1
    arr[len(arr)-1]=temp
    return arr

def sumtotal(arr):
    x=0
    for i in arr:
        x+=i
    return x

def average(arr):
    x=0
    for i in arr:
        x+=1
    return x/len(arr)

def length(arr)
    x=0
    for i in arr:
        x+=1
    return x

def minimum(arr)
    if arr==[]:
        return false
    x=arr[0]
    for i in arr:
        if x>arr[i]:
            x=arr[i]
    return x

def maximum(arr)
    if arr==[]:
        return false
    x=arr[0]
    for i in arr:
        if x<arr[i]:
            x=arr[i]
    return x

def ultimateAnalyze(arr):
    dic={sumtotal:0,average:0,minimum:arr[0],maximum:arr[0],length:0}
    for i in arr:
        dic['sumtotal']+=i
        dic['length']+=1
        if i<dic['minimum']:
            dic['minimum']=i
        if i>dic['maximum']:
            dic['maximum']=i
    dic['average']=dic['sumtotal']/dic['length']

def reverselist(arr):
    for i in range(0, len(arr)/2):
        temp=arr[i]
        arr[i]=arr[len(arr)-1-i]
        arr[len(arr)-1-i]=temp
    return arr

    
        