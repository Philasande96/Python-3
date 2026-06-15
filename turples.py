# Turples are immutable, ordered collections of items. They are similar to lists, but they cannot be modified after they are created. Tuples are defined using parentheses () and can contain any type of data, including other tuples. Here is an example of how to create and use tuples in Python:

real_numbers = (1, 2, 3, 4, 5) #create a tuple of real numbers
print(real_numbers) #print the tuple of real numbers


nums = real_numbers #assign the tuple of real numbers to a new variable 


print("\nThe cubes of the real numbers are: \n")
#create a tuple of cubes of real numbers
for i in nums:
    print(i**3)
    
print(nums) #print the tuple of cubes of real numbers

#we will make the dimensions of the rectangle and use the area formula to calculate the area of the rectangle
length = 500 #declare and assign the value of length dimension
width = 300 
area = length * width #calculate the area of the rectangle
print("\nThe area of the rectangle is: ", area) #print the area of the rectangle
dimensions =(length, width) #declaring the tuple and assign the values initialized and declared ealier on.
print(f'\n length is : {dimensions[0]}')

#Looping through the  tuples
#loop instructions works the same way as list

#create a list and the convert to turple. 
mylist = [values**2 for values in range(10,30)]
print(mylist)
#declare a tuple and add the 'mylist' elements
new_tuple = mylist
print('\nNEW TUPLE \n')
for i in new_tuple:
    print(i) #printing all members or elements of the new tuple
    
#How to change a member of a tuple? 
"""
tuples cannot be changed (immutable)
Instead you can override the tuple, by rewriting new values in the same variable name.

i'll show you how in the example below 
"""

#Lets create a tuple for  integers from 1-10
old_real_nums =(1,2,3,4,5,6,7,8,9,10) #declare tuples
print("\nOld tuples: \n")
print(old_real_nums)
#now lets override the tuple
old_real_nums = (2,4,6,8,10,12)
print('\nOverriden tuple: \n ')
print(old_real_nums)
#Code is expected to execute with ease without any error but display newly assigned values.
