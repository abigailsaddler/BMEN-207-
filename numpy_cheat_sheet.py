"""
numpy cheat sheet
Created on Wed May 27 11:29:10 2020
@author: john.hanks
version 1.0
"""

import numpy as np

a = [0,1,2.0,3,4,5,6,7,8]       # list
a = np.array(a, dtype='uint')   # create an 8-bit unsigned integer array from list
print(a)
a = np.asfarray(a)              # convert to floating point array
print(a)
a = np.arange(0,10,1)           # step by 1, from 0 to 9
print(a)
a = np.linspace(0,8,9)          # 9 even number of stepts from 0 to 8
print(a)
b = np.reshape(a,(3,3))         # create 2D array
print(b)
b = b < 4                       # array of booleans
print(b)
print('shape',b.shape)          # size of array (number of rows and columens)
print('bytes', a.itemsize)      # lenth in bytes of 1 element
b = np.zeros(10)                # array with all zeros
b = np.ones(10)                 # array with all ones
print('min', np.min(a))         # min of a
print('mean',np.mean(a))        # mean of a
a = np.random.randint(0,10,5)   # array of 5 rand ints from 0 to 9 
print('random',a)
a *= 3                          # mutiply each element by 3, no for loop necessary
print(a)
print('sum',np.sum(a))          # sum of all elements in a

# matrix operations
A = [[10, 20, 30],
     [-23, 14, -8],
     [15, 32, 80]]

B = [2,3,5]

A_matrix = np.array(A)
B_matrix = np.array(B)          # Convert 2D list to an numpy array
inv_A = np.linalg.inv(A_matrix) # inverse
x = inv_A.dot(B_matrix)         # dot product
np.set_printoptions(precision=2)# set print options to show precision of 3
print('solve linear equation',x)


