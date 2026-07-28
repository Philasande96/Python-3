
#Recap on the Python Lists

#A list is a collection of items that are ordered and changeable.
#Lists are created using the sqaure brackets []
#Lists can contain any value of any data type.

#Declare a list
fruits = ["apple", "banana", "Mango", "grape"] #declare a list with 5 items
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

