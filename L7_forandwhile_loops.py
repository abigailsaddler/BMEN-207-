# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 12:24:02 2022

@author: abbys
"""
# for and while loops 


nums = [1,2,3,4,5]

for i in nums:
    print(i)

# break keyword and continue keyword

for i in nums:
    if i == 3: 
        print("we found it")
        break #breaks before 3 was printed because print statemnent is after the loop
    print(i)
    
for i in nums:
    if i == 3: 
        print("we found it")
        continue #breaks before 3 was printed because print statemnent is after the loop
    print(i)
    
for num in nums:
    for letter in 'abc':
        print(num, letter)
        
        
for i in range(0,11):
    print(i)
    
    
x = 0
while x < 10:
    if x == 5:
        break
    x +=1 
    print(x)
    
#infinate loop
while True:
    if x == 5:
        break 
    print(x)
    x+=1