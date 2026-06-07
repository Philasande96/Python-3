#Add|remove | change the elements of a list

#Add elements to a list
items = [] #creating an empty lists
items.append("apple") #adding an element to the end of the list
items.append("banana")
print(items) #output: ['apple', 'banana']

#Adding  elements using insert() method
items.insert(1, "orange") #inserting an element at index 1
items.insert(4, "grape") #inserting an element at index 4 (which is out of range, so it will be added at the end)
print(items) #output: ['apple', 'orange', 'banana']


#Removing elements  from a list
#using remove() method
items.remove("orange") #removing the element "orange" from the list
print(items) #output: ['apple', 'banana', 'grape']

#using del method 
#use del method when you know the index number/ position of the item you want to remove
del items[1] #removing the element at index 1 (which is "banana")
print(items) #output: ['apple', 'grape']

#Using pop() method
#use pop() method when you want to remove an element and also want to use it later
#e.g You may want to remove the user to the list of active user and add to the list of inactive users, in this case pop() method is ideal.