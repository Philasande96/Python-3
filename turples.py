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