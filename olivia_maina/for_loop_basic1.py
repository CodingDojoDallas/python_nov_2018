#1. Print all numbers/integers from 0 to 150.

for i in range(0,151):
    print(i) 

#2. Print all multiples of five from 5 to 1,000,000

for i in range(0,1000005,5):
    print(i)

#3. Print integers 1-100. If divisible by 5, print coding instead, if by 10, also print dojo.

for i in range (1,101):
    if i % 10 == 0:
        print("Coding Dojo") 
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

#4. Add odd integers from 0 to 500,000 and print final sum

x = 0
for i in range(1,50,2):
    x += i 
print (x)

#5. Print positive numbers starting at 2018, counting down by 4(exclude 0)
for i in range(2018,1,-4):
    print(i)

#6.Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)

lowNum  = 2 
highNum = 9
mult = 3

for i in range(lowNum,highNum+1):
        if i%mult ==0:
                print(i)

#A common mistake?

#1.
list = [3,5,1,2]
for i in list:
    print(i)
---> would print 3,5,1,2

#2.
list = [3,5,1,2]
for i in range(list):
    print(i)
---> would throw an error

#3
list = [3,5,1,2]
for i in range(len(list)):
    print(i)
---> would print 0,1,2,3