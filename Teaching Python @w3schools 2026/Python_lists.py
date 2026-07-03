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
#To determine how manu members\elements a list has, you can use the len() function.
fruits = ['apple', 'banana', 'orange', 'apple', 'mango']
print(len(fruits)) #Output 5

#Lists datatypes 
#Lists can be of any datatypes.
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

