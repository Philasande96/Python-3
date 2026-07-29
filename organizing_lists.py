#Sorting a list permanently using sort() method
#This method will sort the list permanentl and cannot be altered and reverted.

sports_cars = ["Volvo", "BMW", "Mercedes", "Audi", "Toyota", "Honda"]
print("original list: ", sports_cars)

sorted_cars = sports_cars.sort() #sort the list permanently
print(sports_cars)

#Sometimes you may want to reverse the order of the list. You can do that by passing the reverse=True argument to the sort() method.
print("\n Reversed list: \n")
sports_cars.sort(reverse=True)
print(sports_cars)

#To revert the reverse order 
sports_cars.sort(reverse=False)
print(sports_cars)

#You can temporarily sort the list by using the sorted() function. This function returns a new list with the sorted elements without affecting the actual list.


cars = ["Volvo", "BMW", "Mercedes", "Audi", "Toyota", "Honda"]
print("\noriginal list:\n ", cars)
sorted_cars = sorted(cars) #sort the list temporarily

print("\n sorted list:\n", sorted_cars)
print(sorted_cars)


#Making numerical lists 

#creating numberical values using range() function
nums = []#create an emopty list
for i in range(1,6):
    print(i) #Output is 1 2 3 4 5 --> This is not a list 
    nums.append(i) #appending the value to the list
print(nums) #Output: [1,2,3,4,5] --> Method 1

#Lets create a list from the range
nums = list(range(1,6)) #Method 2
print(nums) #Output: [1,2,3,4,5]

#Lets create a list using step 
even_nums = list(range(2,11,2)) #Method 3
print(even_nums) #Output: [2,4,6,8,10]

#Insert squares of the even numbers in the squares variable

squares = [] #create an empty list
for i in even_nums:
    squares.append(i**2) #appending the square of the even numbers to the list
    
print(squares) #Output: [4,16,36,64,100]

