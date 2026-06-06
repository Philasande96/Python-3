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
