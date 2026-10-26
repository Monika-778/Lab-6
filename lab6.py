# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:04:54 2026

@author: Monika
"""

#Ques1.
'''print("          Addition Table")

print("     ", end="")

for i in range(1, 10):
    print("%4d" % i, end="")

print()
print("   --------------------------------------")

for i in range(1, 10):
    print("%2d |" % i, end="")

    for j in range(1, 10):
        print("%4d" % (i + j), end="")

    print()
    '''
#Ques2.
'''n = int(input("Enter N: "))
i = 1
while i <= 1000:
    if i % n != 0:
        i = i + 1
        continue

    if i % 4 == 0:
        i = i + 1
        continue

    print(i, end=" ")
    i = i + 1
'''

#Ques3.
#(a)
'''n = int(input("Enter N: "))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end=" ")
        j = j + 1
    print()
    i = i + 1'''
    
 #(b)
'''n = int(input("Enter N: "))
i = n
while i >= 1:
    j = 1
    while j <= i:
        print("*", end=" ")
        j = j + 1
    print()
    i = i - 1   '''
    
#(c)
'''n = int(input("Enter N: "))
i = 1
while i <= n:
    spaces = n - i
    while spaces > 0:
        print("  ", end="")
        spaces = spaces - 1

    j = 1
    while j <= i:
        print("*", end=" ")
        j = j + 1

    print()
    i = i + 1
'''
 
#Ques4.
'''n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Invalid input")
else:
    octal = ""

    while n > 0:
        rem = n % 8
        octal = str(rem) + octal
        n = n // 8

    print("Octal equivalent:", octal)'''
   
    
#Ques5. 
'''n = int(input("Enter number of students: "))
largest = 0
second = 0
i = 1
while i <= n:
    distance = int(input("Enter distance: "))

    if distance > largest:
        second = largest
        largest = distance
    elif distance < largest and distance > second:
        second = distance

    i = i + 1

print(largest)
print(second)'''

#Ques6.
'''n = int(input("Enter N: "))
num = 1
while num <= n:
    temp = num
    digits = 0

    while temp > 0:
        digits = digits + 1
        temp = temp // 10

    temp = num
    total = 0

    while temp > 0:
        rem = temp % 10
        total = total + rem ** digits
        temp = temp // 10
'''
   
#Ques7.
'''print("N      N^2      N^3      Square Root")
i = 1
while i <= 15:
    square = i ** 2
    cube = i ** 3
    root = i ** 0.5

    print(f"{i:2d} {square:8d} {cube:8d} {root:12.4f}")

    i = i + 1'''

#Ques8.
'''n = int(input("Enter N: "))
i = 1
while i <= n:
    spaces = n - i

    while spaces > 0:
        print(" ", end="")
        spaces = spaces - 1

    j = 1
    while j <= i:
        print(i, end=" ")
        j = j + 1

    print()
    i = i + 1'''

#Ques9.
'''n = int(input("Enter N: "))
i = 1
num = 1
while i <= n:
    j = 1
    while j <= i:
        print(num, end=" ")
        num = num + 1
        j = j + 1

    print()
    i = i + 1'''

#Ques10.
'''n = int(input("Enter an odd positive integer: "))
if n <= 0 or n % 2 == 0:
    print("Invalid input")
else:
    mid = (n + 1) // 2
    i = 1
    while i <= mid:
        spaces = mid - i
        while spaces > 0:
            print(" ", end="")
            spaces = spaces - 1

        stars = 1
        while stars <= 2 * i - 1:
            print("*", end="")
            stars = stars + 1

        print()
        i = i + 1

    i = mid - 1
    while i >= 1:
        spaces = mid - i
        while spaces > 0:
            print(" ", end="")
            spaces = spaces - 1

        stars = 1
        while stars <= 2 * i - 1:
            print("*", end="")
            stars = stars + 1

        print()
        i = i - 1'''