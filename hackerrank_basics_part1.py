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
   

""" Question 11:         Task : You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

                                Sample Input 0 : HackerRank.com presents "Pythonist 2".
                                Sample Output 0 : hACKERrANK.COM PRESENTS "pYTHONIST 2". """

# solution:

def swap_case(s):
       return s.swapcase()
 
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

""" Question 12:     Task : You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
                            Hello firstname lastname! You just delved into python.
                            
                            Sample Input : Ross
                                           Taylor
                                            
                            Sample Output : Hello Ross Tailor! You just delved into python."""

# Solution:

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")    

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


""" Question 13:     Task :  Read a given string, change the character at a given index and then print the modified string.
                            
                            Sample Input : STDIN           Function
                                            -----           --------
                                          abracadabra     s = 'abracadabra'
                                            5 k             position = 5, character = 'k'

                            Sample Output : abrackdabra """

# solution:

def mutate_string(string, position, character):
    new_str = string[:position] + character + string[position+1:]
    return new_str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

""" Question 14:     Task :   In this challenge, the user enters a string and a substring. You have to print the number of times that
                              the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
                              
                              Sample Input : ABCDCDC
                              Sample Output : CDC """

# solution:

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
         if(string[i:i+len(sub_string)]) == sub_string:
           count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
                              
""" Question 15:      Task :   You are given a string .
                               Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters,
                               digits, lowercase and uppercase characters.
                               
                               Sample Input :  qA2
                               Sample Output : True
                                               True
                                               True
                                               True
                                               True """

# solution:

if __name__ == '__main__':
    s = input()
    print(any(ch.isalnum()for ch in s))
    print(any(ch.isalpha()for ch in s))
    print(any(ch.isdigit()for ch in s))
    print(any(ch.islower()for ch in s))
    print(any(ch.isupper()for ch in s))

""" Question 16:          Task : you are given a partial code that is used for generating the HackerRank Logo of variable thickness.
                                 Your task is to replace the blank (______) with rjust, ljust or center.
                                 
Sample Input : 5

Sample Output :    

    H                              
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H """

thickness = int(input())  
c = 'H'

for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

""" Question 15:        Task :   You are given a string s and width w.
                                 Your task is to wrap the string into a paragraph of width .
                                 
                                 Sample Input : ABCDEFGHIJKLIMNOQRSTUVWXYZ
                                                4
                                 Sample Output : ABCD
                                                 EFGH
                                                 IJKL
                                                 IMNO
                                                 QRST
                                                 UVWX
                                                 YZ """

# solution:

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)








