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


""" Question 3:     Task :  You are given two integer arrays of size NXP and MXP (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.

                            Input Format : The first line contains space separated integers N, M and P.
                                           The next  lines contains the space separated elements of the P columns.
                                           After that, the next  lines contains the space separated elements of the P columns.
                                           
                            Sample Input :  4 3 2
                                            1 2
                                            1 2 
                                            1 2
                                            1 2
                                            3 4
                                            3 4
                                            3 4
                                             
                            Sample Output : [[1 2]
                                            [1 2]
                                            [1 2]
                                            [1 2]
                                            [3 4]
                                            [3 4]
                                            [3 4]]  """

# solution:

import numpy

N,M,P = map(int, input().split())
arr1 = []
for i in range(N):
    arr1.append(list(map(int, input().split())))
    
arr2 = []
for i in range(M):
    arr2.append(list(map(int, input().split())))
    
arr1 = numpy.array(arr1)
arr2 = numpy.array(arr2)

result = numpy.concatenate((arr1, arr2), axis=0)
print(result)


""" Question 4:           Task : You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, 
                                 your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.
                                 
                           Sample Input : 333
                           Sample Output : [[[0 0 0]
                                            [0 0 0]
                                            [0 0 0]]

                                            [[0 0 0]
                                             [0 0 0]
                                             [0 0 0]]

                                            [[0 0 0]
                                             [0 0 0]
                                             [0 0 0]]]

                                            [[[1 1 1]
                                              [1 1 1]
                                              [1 1 1]]

                                             [[1 1 1]
                                              [1 1 1]
                                              [1 1 1]]

                                             [[1 1 1]
                                              [1 1 1]
                                              [1 1 1]]]"""

# Solution:

import numpy as np 
arr = tuple(map(int,input().split()))
print(np.zeros(arr,dtype=int))
print(np.ones(arr,dtype=int))

""" Question 5:           Task :    You are given a NXM integer array matrix with space separated elements (N = rows and M = columns).
                                    Your task is to print the transpose and flatten results.

                                    Sample Input : 2 2
                                                   1 2
                                                   3 4
                                                   
                                    Sample Output : [[1 3]
                                                     [2 4]]
                                                    [1 2 3 4] """

# solution:

import numpy
N,M = map(int,input().split())
matrix = []
for i in range(N):
    row = list(map(int,input().split()))
    matrix.append(row)
    
arr = numpy.array(matrix)
print(numpy.transpose(arr))
print(arr.flatten())


""" Question 6:            Task : You are given a 1-D array A, . Your task is to print the floor,ceil and rint  of all the elements of A .

                           Sample Input : 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
                           Sample Output : [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
                                           [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
                                           [  1.   2.   3.   4.   6.   7.   8.   9.  10.]"""

# Solution:

import numpy
numpy.set_printoptions(legacy='1.13')

A = numpy.array(list(map(float,input().split())))
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))







