
#Recap on the Python Lists

#A list is a collection of items that are ordered and changeable.
#Lists are created using the square brackets []
#Lists can contain any value of any data type.

#Declare a list
fruits = ["apple", "banana", "Mango", "grape", "Pineapple"] #declare a list with 5 items
empty_list =[] #declare empty list.

#Accessing the list.

print(fruits[0]) #this will return the first item in the list
print(fruits) #this will return the entire list, with square brackets and double quotes

for i in fruits:
    print("\n", i.upper()) #this will print each item in the list without the square brackets and the double quotes
    
#Adding, removing and changing elements


#1. Modifying the elements in  a list
    """
    The method of modifying  a list is similar to a method of accessing a single member of a list. However, in the modification of a list, you provide the value of the element you want to assign to the list.
    """
#e.g. Lets add new member  in our Fruits list and modify it

print("Original List", fruits , "\n") #this will return the entire list, with square brackets and double quotes

fruits[0] = "Pineapple" #this will add a new member in the list
#Above statement will add pineapple to the list in the position  of the first element and remove the existing element.

print("Modified list:",fruits)

#Adding data into a list
#By  using append() method, this method doesn't need to know the position of the element, it will append the new element at the end of the list.
fruits.append("Kiwi") #this will add a new member in the list
print("Modified list:",fruits)

#Adding a member using insert() method. This method will insert the new member at the specified position without removing exisiting member, instead it will shift existing members to the right.

fruits.insert(0,"Watermelon") #this will add a new member in the list
print("\nModified list:",fruits)

print("\n \n ")

#Removing list elements
#Removing item using del() method. This method will remove the item from the list using position\index number of the item. It is best for situations where you know the position of the element you want to remove.
print("Original list:", fruits) 
del fruits[0] #this will remove the first element from the list
print("Modified list:", fruits)
# del() method deletes element permanently from the list.

print("\n \n")
#remove  elements using del() method

Users = ["John", "Mary", "Tom", "James", "Jack", "Jill"]
del Users[0] #this will remove the first element from the list
print("Modified users list:")
for i in Users:
    print(i)

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
print("\nPositive integers: ")
for i in integers:
    if i > 0:
        print(i)
print("\n")
print("\nNegative integers:\n")
for x in integers:
    if x < 0:
        print(x)
#removing element using pop() method. This method allows  you to remove or delete the item in the list  and able to use it in another list.

cars = ["BMW", "Mercedes", "Audi", "Toyota", "Volvo"]
popped_car = cars.pop() #this will remove the first element from the list
print(popped_car) #output: Volvo

print((f"last car to own is {popped_car} ").title())

#removing item for another use using index
countries = ["South Africa", "USA", "UK", "Germany", "France", "Japan"]
popped_country = countries.pop(0) #this will remove the first element from the list
print(popped_country) #output: South Africa

#Another method to  remove the element is by value. You can remove the element in the list by using the value of the element.  Use remove() method.
fruits = ["apple", "banana", "Mango", "grape"]
removed_val = fruits.remove("Mango") #this will remove the first element from the list
print(removed_val) #this will return none, because the remove() function removes item completely from the list.

#Recap about removing list
"""
1. Use del() method to remove  element from the list completely.
2. pop() method to remove the element from the list and able to use it in another list.
3. remove() method to remove the element from the list by value.
"""
#NB: remove will remove first occurence of the element in the list. If element appears more than once, it will remove the first. To remove all occurrences you'll need to use for loop.

months=["January", "February", "March", "January","April", "May", "June", "July", "August", "September", "October", "January","November", "December"]

#Try it yourself

"""
3.1 Names: store the names of few of your friends in a list called names. Print each person's name by accessing each element in the list, one at a time.

"""

names = ["Liqhame", "Phila", "Jack", "Tom", "James", "Jill"]
for i in names:
    print(i)

"""
3.2. Greetings: Start with the list you used in the previous exercise. Print each person's name followed by a greeting. Use the greeting "Hello" for the first person and "Goodbye" for the last person.
"""

for i in names:
    print(f"Hellow {i}")
    

removed_friends = names.remove("Liqhame")
print(removed_friends) #answer is None