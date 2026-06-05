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

