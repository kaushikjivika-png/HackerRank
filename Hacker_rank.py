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
    
