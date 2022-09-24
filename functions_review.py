# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 12:04:16 2022

@author: abbys
"""

#functions 

def hello_func(greeting,name='you'):
    return '{} , {}'.format(greeting,name)


print(hello_func("hi", name="abby"))#how to execute function dont forget parethesis 
#benifits - keeps your code dry - dont repeat yourself 
#you can treat the return value just like the variable output 
#you can treat the element and run functions for the variable type ex. .upper()


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
    
courses = ['math', 'art']
info = {'name':"abby", 'age':"20"}
    
student_info(*courses, **info) #use the stars to run through the function

