#Introduction to lists in Python
#Lists are ordered collections of items that can be of different types. They are mutable, meaning you can change their contents after they have been created.

#Create and initialize a list
provinces =['Eastern Cape', 'Free State', 'Gauteng', 'KwaZulu-Natal', 'Limpopo', 'Mpumalanga', 'North West', 'Northern Cape', 'Western Cape']

#print the list
print(provinces) #This method will print the entire list as it is, includind characters and brackets.
"""
    Print Output:
['Eastern Cape', 'Free State', 'Gauteng', 'KwaZulu-Natal', 'Limpopo', 'Mpumalanga', 'North West', 'Northern Cape', 'Western Cape']
"""
print(" ") #This method will print the first item in the list, which is 'Eastern Cape'.")


#To print each item in the list separately, we can use a for loop:
for i in provinces:
    print(i) #The title() method capitalizes the first letter of each word in the string.
    
"""
Eastern Cape
Free State
Gauteng
KwaZulu-Natal
Limpopo
Mpumalanga
North West
Northern Cape
Western Cape
"""
    
    #Modifying the list
    
towns =['Port Elizabeth', 'Bloemfontein', 'Johannesburg', 'Durban', 'Polokwane', 'Nelspruit', 'Mahikeng', 'Kimberley', 'Cape Town']

print(towns) #This method will print the entire list as it is, includind characters and brackets.
#Changing the town in position(index 0)
towns[0] = 'East London' #This method will change the first item in the list, which is 'Port Elizabeth', to 'East London'.
print(towns) #This method will print the modified list with 'East London' instead of 'Port Elizabeth'.
"""
Original
['Port Elizabeth', 'Bloemfontein', 'Johannesburg', 'Durban', 'Polokwane', 'Nelspruit', 'Mahikeng', 'Kimberley', 'Cape Town']

Newly implemented
['East London', 'Bloemfontein', 'Johannesburg', 'Durban', 'Polokwane', 'Nelspruit', 'Mahikeng', 'Kimberley', 'Cape Town']
"""

#Append
towns.append('Mthatha') #This method will add 'Mthatha' to the end of the list.
print(towns) #This method will print the modified list with 'Mthatha' added at the end.
"""
['East London', 'Bloemfontein', 'Johannesburg', 'Durban', 'Polokwane', 'Nelspruit', 'Mahikeng', 'Kimberley', 'Cape Town', 'Mthatha']
"""
#insert method
towns.insert(0, 'Matatiel') #This method will insert 'Matatiel' at the beginning of the list (index 0).
print(towns) #This method will print the modified list with 'Matatiel' added at the beginning.
"""
['Matatiel', 'East London', 'Bloemfontein', 'Johannesburg', 'Durban', 'Polokwane', 'Nelspruit', 'Mahikeng', 'Kimberley', 'Cape Town', 'Mthatha']
"""
#Insert method does not replace the item at the specified index, but rather shifts the existing items to the right to make room for the new item. In this case, 'Matatiel' is inserted at index 0, and all other items are shifted one position to the right.


