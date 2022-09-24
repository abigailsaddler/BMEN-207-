# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 14:37:57 2022

@author: abbys
"""

#NumPy arrays

#why use array instead of list 
#they save you coding time - single lines of code for itterations 
#ececutes faster but is let faster 
#uses less memory 
#it stores the data at one memory address and the list saves another memory location then with one data


import numpy as np 

# a = np.array([2,3,4])
# b = np.arange(1,12,2)
# print(b)
# c = np.linspace(1, 12,6)
# print(c)
# c=c.reshape(3,2)
# print(c)
# print(c.size)
# print(c.shape)
# print(c.dtype)
# print(c.itemsize) #how many bytes of memory is being used 
# b = np.array([(1.5,2,3) , (4,5,6)])
# print(b)
# print(a<4)
# print(a*3) #doesnt save changes 
# a *= 3 #edits the array 
# print(a)
# a = np.zeros((3,4))
# print(a)
# print(a.dtype)
# a = np.ones((2,3))
# print(a)
# a = np.ones(10)
# print(a)

# a = np.array([2,3,4], dtype=np.int16)
# print(a)
# print(a.dtype)
# print(a.itemsize)
# a = np.random.random((2,3))
# print(a)
# a = np.random.randint(0,10,5)
# print(a)
# print(a.sum())
# print(a.min())
# print(a.mean())
# print(a.var())
# print(a.std())

# a = np.random.randint(1,10,6)
# a = a.reshape(3,2)
# print(a.sum(axis=1))#row
# print(a.sum(axis=0))#column

#how to import data as an array 
# data = np.loadtype("data.txt", dtype=np.uint8, delimter=",", skiprows=1)
#load text doesnt handle execptions well -- genfromtxt helps with exceptions 

a = np.arange(10)
print(a)
np.random.shuffle(a)
print(a)
print(np.random.choice(a))
np.random.random_integers(5,10,2)
