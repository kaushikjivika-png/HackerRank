# Hackerrank basic Questions : 

""" Question 1 :    Task : The provided code stub reads two integers, a and b from STDIN
                           Add logic to print two lines. 
                           1. integer division, (a // b)
                           2. float division, (a / b).
                           No rounding or formatting is necessary.

                           Example:

                           a = 3                        The result of the integer division 3 // 5 = 0                                                        
                           b = 5                        The result of the float division is 3 / 5 = 0.6  """

# Solution:

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)                             # integer division (a//b)
    print(a/b)                              # float division (a/b)

""" Question 2:       Task : Given an integer, n, perform the following conditional actions:
                             1. If n is odd, print Weird.
                             2. If n is even and in the inclusive range of 2 to 5, Print Not Weird.
                             3. If n is even and in the inclusive range of 6 to 20, Print Weird.
                             4. If n is even and greater than 20, Print Not Weird.  """  

# solution:

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        print("Weird")
    elif 2<=n<=5 :
        print("Not Weird")
    elif 6<=n<=20:
        print("Weird")
    else:
        print("Not Weird")
    
""" Question 3:         Task : The provided code stub reads an integer,n from STDIN. For all non-negative integers i < n, print i**2.
                                
                                Example:

                                n = 3
                                The list of non-negative integers that are less than n = 3 is [0,1,2].  Print the square of each number on a separate line. """

# Solution:

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i**2)

""" Question 4:          Task : Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
                                Three conditions are used to identify leap years:
                                
                                1. The year can be evenly divided by 4, is a leap year, unless:
                                2. The year can be evenly divided by 100, it is NOT a leap year, unless:
                                3. The year is also evenly divisible by 400. Then it is a leap year. """

# solution:

def is_leap(year):
    leap = False
    if(year % 4 == 0 and year % 100 != 0):
        return True
    elif(year % 400 == 0 and year % 100 == 0):
        return True
    else:
        return leap
year = int(input())

""" Question 5:         Task : The included code stub will read an integer, n from STDIN Without using any string methods, try to print the following:   123....n
                               
                               Example :      n = 5 
                                              Print the string 12345 """

# solution:

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")

""" Question 6:         Task :   You are given three integers x,y, and z representing the dimensions of a cuboid along with an integer n.
                                Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. 
                                Here, 0<=i<=x; 0<=j<=y; 0<=k<=z
                                
                                Example : x=1, y=1, z=1, n=2
                                          All permutations of (i,j,k) are:
                                          (0,0,0)
                                          (0,0,1)
                                          (0,1,0)
                                          (0,1,1)
                                          (1,0,0)
                                          (1,0,1)
                                          (1,1,0)
                                          (1,1,1)
                                          Print an array of the elements that do not sum to n=2 :
                                          [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]] ."""

# solution:

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
result = [[i,j,k] 
                  for i in range(x+1)
                  for j in range(y+1)
                  for k in range(z+1)
                  if  i + j + k != n]

print(result)






