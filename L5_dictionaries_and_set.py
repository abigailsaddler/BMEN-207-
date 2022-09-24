#video over dictionaries and sets

# assigne a dictionary
student = {'name':'john', 'age':25, 'courses':['Math', "Engineering"]}
print(student)
print(type(student))
# you can combind diferent types of variables in your dictionary 

print(student['name'])
print(student['courses'])
#print(student['phone']) -- produces an error because there is nothing to call 

student["phone"] = '555-555'
print(student)

#adds the phone number to the end of the dictionary 

del student['phone'] #del function deletes an element 
print(student)

print(student.keys()) # prints the keys in dic 
print(student.values()) # prints the values in the dic 
print(student.items()) # prints all the items in your dic 

print(len(student))

for key,item in enumerate(student): # the dictionary is iterable 
    print(key)
    print(item)
    
for k,v in student.items(): # gives the same output as above 
    print(k)
    print(v)
    
#print(student.pop("name")) #deletes the key value pair 
#print(student)

d2 = student 
# in python this points to the same object not a copy of the same object 
print(id(student))
print(id(d2))
# this shows that they are identical 
# if you edit one list both will change 

# to make a copy 

d2 = dict(student) #how to make a dict copy 
student["name"]= 'steve'

print(student)
print(d2)
# shows how to make a copy 



# nested dictionary in a list
x = [
     'a',
     'b',
     {
          'foo':1,
          'bar':
          {
              'john': 80,
              'mike': 90,
              'kristen': 100
          },
          'mary': 70
     },
     'c',
     'd'
    ]

    
#complex nested dictionary in list 
print(x[2]['bar']['john'])
print(x[1])
print(x[2])
