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

#To print each item in the list separately, we can use a for loop:
for i in provinces:
    print(i)
    
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