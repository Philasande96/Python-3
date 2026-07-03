#Learn more about lists in Python

#Lists are used to store multiple values in a single variable.
#Lists are ordered,allow duplicate values and changeable(mutable).
#Lists are indexed starting from 0.
#Lists are using square brackets [ ] to define the start and end of the list.

#Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list) #Output [1, 2, 3, 4, 5]
#Accessing elements in a list
print(my_list[0]) #Output 1
print(my_list[1]) #Output 2

#Lists allow duplicate values
fruits = ['apple', 'banana', 'orange', 'apple', 'mango']
print(fruits) #Output ['apple', 'banana', 'orange', 'apple', 'mango']

#List length
#To determine how many members\elements a list has, you can use the len() function.
fruits = ['apple', 'banana', 'orange', 'apple', 'mango']
print(len(fruits)) #Output 5

#Lists datatypes 
#Lists can be of any datatype.
fruits = ['apple', 10, True, None]
print(type(fruits)) #Output <class 'list'>
print(type(fruits[0])) #Output <class 'str'>
print(type(fruits[1])) #Output <class 'int'>

#type()
#To determine the datatype of a variable, you can use the type() function.
#In Python perspective, lists are defined as objects of type list.

fruits = ['apple', 'banana', 'orange', 'apple', 'mango']
print(type(fruits)) #Output <class 'list'>
print(type(fruits[0])) #Output <class 'str'>


#The list() Constructor
"""
The list() constructor in Python is a built-in function used to instantiate a new list object, either by creating an empty list or by converting an existing iterable into a list
"""
newlist = list((1, 2, 3, 4, 5))#Take note that we used simple parantheses not square.
print(type(newlist)) #Output <class 'list'>
print(newlist) #Output [1, 2, 3, 4, 5]

dup= list([1, 2, 3, 4, 5]) #Take note that we used square brackets not parantheses.
print(type(dup)) #Output <class 'list'>
print(dup) #Output [1, 2, 3, 4, 5]
#list() constructor gives us an opportunity or variety of options on what parantheses to use, square or simple.



