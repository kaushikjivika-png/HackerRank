# Hackerrank basic numpy questions :

""" Question 1 : Task : You are given a space separated list of numbers.
                        Your task is to print a reversed NumPy array with the element type float.

                        Sample Input :  1 2 3 4 -8 -10
                        Sample Output : [-10.  -8.   4.   3.   2.   1.] """

# Solution: 

import numpy

def arrays(arr):
    return numpy.array(arr[::-1],float)
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

""" Question 2:   Task : You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.

                         Sample Input : 1 2 3 4 5 6 7 8 9
                         Sample Output : [[1 2 3]
                                          [4 5 6]
                                          [7 8 9]] """

# Solution:

import numpy

arr = list(map(int,input().split()))
res = numpy.array(arr)
print(numpy.reshape(res,(3,3)))


                        