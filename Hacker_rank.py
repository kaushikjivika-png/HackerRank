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

""" Question 7:         Task :  Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. 
                                Store them in a list and find the score of the runner-up. """

# solution:

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    unique_score = set(arr) 
    max_score = max(unique_score)
    unique_score.remove(max_score) 
    print(max(unique_score))    

""" Question 8:         Task :  The provided code stub will read in a dictionary containing key/value pairs of name: [marks] for a list of students. 
                                Print the average of the marks array for the student name provided, showing 2 places after the decimal.

                                Example:    marks key : value pairs are
                                            'alpha' : [20,30,40]
                                            'beta'  : [30,50,70]
                                            query_name = 'beta'
                                            The average of beta's marks is (30 + 50 + 70) / 3 = 50.00  """

# solution:

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

average = sum(student_marks[query_name]) / len(student_marks[query_name])
print(f"{average:.2f}")


    
""" Question 9:          Task :  Consider a list (list = []). You can perform the following commands:
                                 1. insert i e: Insert integer e at position i.
                                 2. print: Print the list.
                                 3. remove e: Delete the first occurrence of integer e.
                                 4. append e: Insert integer e at the end of the list.
                                 5. sort: Sort the list.
                                 6. pop: Pop the last element from the list.
                                 7. reverse: Reverse the list.

                                 Initialize your list and read in the value of n followed by n lines of commands where each command will be of the types listed above. 
                                 Iterate through each command in order and perform the corresponding operation on your list. 
                                 
                                 Example: n=4
                                           append 1
                                           append 2
                                           insert 3 1
                                           print

                                           Output: [1,3,2] """


# solution:

if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        command = input().split()
        
        if(command[0] == "insert"):
            lst.insert(int(command[1]) , int(command[2]))
        elif(command[0] == "print"):
            print(lst)
        elif(command[0] == "remove"):
            lst.remove(int(command[1]))
        elif(command[0] == "append"):
            lst.append(int(command[1]))
        elif(command[0] == "sort"):
            lst.sort()
        elif(command[0] == "pop"):
            lst.pop()
        elif(command[0] == "reverse"):
            lst.reverse()
        

""" Question 10:         Task :  Given an integer,n and n space-separated integers as input, create a tuple,t of those n integers.
                                 Then compute and print the result of hash(t). 

                                 Input Format:
                                 The first line contains an integer,n, denoting the number of elements in the tuple.
                                 The second line contains n space-separated integers describing the elements in tuple t. """

# solution:

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
   







