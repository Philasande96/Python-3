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
#Football teams in the world
teams = ['Kaizer Chiefs', 'Orlando Pride', 'New York Red Bulls', 'Los Angeles Galaxy', 'Columbus Crew'] 
#Accessing the list member
print(teams[0]) #Output Kaizer Chiefs
print(teams[1]) #Output Orlando Pride

#changing the list member

#lets change  2nd member to Orlando Pirates
teams[1] = 'Orlando Pirates'
print(teams) #Output ['Kaizer Chiefs', 'Orlando Pirates', 'New York Red Bulls', 'Los Angeles Galaxy', 'Columbus Crew']


#Accessing all members  through loop
for i in teams:
    print(i) #Output Kaizer Chiefs, Orlando Pirates, New York Red Bulls, Los Angeles Galaxy, Columbus Crew
    
#Another method to add a new member to the list is to use the append() method. Append() method you do not have to specify the position of the new member, instead newly added member will be placed at the end of the list.
teams.append('Golden Arrows FC')

print(teams) #Output ['Kaizer Chiefs', 'Orlando Pirates', 'New York Red Bulls', 'Los Angeles Galaxy', 'Columbus Crew', 'Golden Arrows FC']
print(teams[-1]) #will print out the last item  in the list called teams

#another way of adding a new member to the list is to use the insert() method. Insert method   allows you to add member at any position in the list, you provide the position and the value off the new member. Insert() Method  does not  change  or remove the a valuee/member in said position rather it shifts subsequent members to the right.

countries = ['India', 'China', 'United States', 'Indonesia', 'Brazil']
countries.insert(2, 'Pakistan') #will insert 'Pakistan' at position 2 and shift all subsequent members to the right
print(countries) #Output ['India', 'China', 'Pakistan', 'United States', 'Indonesia', 'Brazil']
print ("length of the countries lis is " , len(countries)) #Output length of the countries lis is 6

#Removing elements from a list
#You can remove an item or member in the list by its index or by value.
#Removing an item by its index
#If you know the position of the member you want to remove, you can use the del keyword to remove it.
countries = ['India', 'China', 'United States', 'Indonesia', 'Brazil']
del countries[2] #will remove 'United States' from the list
print(countries) #Output ['India', 'China', 'Indonesia', 'Brazil']

del countries[0] #will remove 'India' from the list
print(countries) #Output ['China', 'Indonesia', 'Brazil']

del countries[-1] #will remove 'Brazil' from the list
print(countries) #Output ['China', 'Indonesia']
#Above examples you can no longer access the deleted item. It is permanently deleted 






