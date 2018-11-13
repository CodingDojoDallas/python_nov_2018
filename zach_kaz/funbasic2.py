def countdown(x):
    array=[]
    for i in range (x,-1,-1):
        array.append(i)
    return array

def pandr(x):
    print(x[0])
    return(x[1])

def fpl(x):
    return (x[0]+len(x))

def vgts(x):
    if len(x)<2:
        return false
    new=[]
    for i in x:
        if i>x[1]:
            new.append(x[i])
    print(len(new))
    return new

def tltv(s,v):
    new=[]
    for i in range(0,s):
        new.append(v)
    return new