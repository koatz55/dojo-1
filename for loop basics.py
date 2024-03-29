#Moise Pierre-Louis
#7/16/2022

"""
Basic - Print all integers from 0 to 150.
Multiples of Five - Print all the multiples of 5 from 5 to 1,000
Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, 
print "Coding" instead. If divisible by 10, print "Coding Dojo".
Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and 
going through highNum, print only the integers 
that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, 
the loop should print 3, 6, 9 (on successive lines)
"""

#basics
for i in range(151):
    print(i)

#Multiples of Five
for i in range(0,1001,5):
    print(i)

#counting the Dojo way
for i in range(1,100):
    if i%10 == 0:
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else:
        print(i)

#Whoa. That Sucker's Huge
hugenum = 0
for i in range(0,500000):
    hugenum+=i
print(hugenum)

#Countdown by Fours
for i in range(2018,0,-4):
    print(i)

#Flexible counter
hightnum = 134
lownum = 23#for MJ
multi = 23
for i in range(lownum,hightnum, multi):
    print(i)