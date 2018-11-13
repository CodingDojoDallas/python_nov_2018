import unittest
def reverseArray(arr):
    for i in range (0,int(len(arr)/2)):
        arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
    return(arr)
def palindrome(arr):
    for i in range (0,len(arr)):
        if arr[i]!=arr[len(arr)-1-i]:
            return False
    return True

def coins(cents):
    change=[0,0,0,0]
    cents=cents%100
    change[0]=cents//25
    change[1]=(cents-25*change[0])//10
    change[2]=(cents-(25*change[0])-(10*change[1]))//5
    change[3]=cents-(25*change[0])-(10*change[1])-(5*change[2])
    return change

def factorial(x):
    if x==1:
        return 1
    else: x= x* factorial(x-1)
    return x

def fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else: x= fib(x-1)+fib(x-2)
    return x

class reversetests(unittest.TestCase):
    def test1(self):
        return self.assertEqual(reverseArray([3,2,1]),[1,2,3])
    def test2(self):
        return self.assertEqual(reverseArray([1]),[1])
    def test3(self):
        return self.assertEqual(reverseArray([1,2,3,4,5,6]),[6,5,4,3,2,1])

class palindrometests(unittest.TestCase):
    def test1(self):
        return self.assertEqual(palindrome([3,2,1]),False)
    def test2(self):
        return self.assertEqual(palindrome([3,2,3]),True)
    def test3(self):
        return self.assertEqual(palindrome('abba'),True)
    def test4(self):
        return self.assertEqual(palindrome('amanaplanacanalpanama'),True)
    def test4(self):
        return self.assertEqual(palindrome("955559"),True)

class coinstests(unittest.TestCase):
    def test1(self):
        return self.assertEqual(coins(1),[0,0,0,1])
    def test2(self):
        return self.assertEqual(coins(99),[3,2,0,4])
    def test3(self):
        return self.assertEqual(coins(50),[2,0,0,0])
    def test4(self):
        return self.assertEqual(coins(69),[2,1,1,4])
    def test5(self):
        return self.assertEqual(coins(100),[0,0,0,0])
    def test6(self):
        return self.assertEqual(coins(0),[0,0,0,0])

class factorialtests(unittest.TestCase):
    def test1(self):
        return self.assertEqual(factorial(4),24)
    def test2(self):
        return self.assertEqual(factorial(1),1)

class fibtests(unittest.TestCase):
    def test1(self):
        return self.assertEqual(fib(5),5)
    def test2(self):
        return self.assertEqual(fib(1),1)
    def test3(self):
        return self.assertEqual(fib(0),0)
    def test4(self):
        return self.assertEqual(fib(10),55)
    
  
 

if __name__=="__main__":
    unittest.main()