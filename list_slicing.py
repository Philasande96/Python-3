#Slicing lists: the process of extracting portion of the members of the list. The syntax for slicing lists is as follows:
#the use colon operator (:) to specify the start and end index of the portion of the list to be extracted. The start index is inclusive, while the end index is exclusive. Here is an example of how to slice a list in Python:

#Exercise | Practice

#4-10. Slices 
"""
Question 1.
Print the message, 'the first three items in  the list are': then use slice to print the first three items from  the lists
"""
my_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #create a list of integers
#Answer
print('the first  three items in the list are: ', my_integers[:3])

"""
Question 2.
Print the message, Three items from the middle of the list are: then use slice to print three items from the middle of the list    
"""
print ('Three items from the middle of the lists are :' , my_integers[3:6]) #print three items from the middle of the list

"""
Question 3 
Print the message, the last three items in the list are, use slice to print the last three items in the list
"""
print('The last three items in the list are : ', my_integers[7:10])

#List comprehension : same as for loop and using range method to create a list of squares of numbers from 1 to 10

myold_list = [value**2 for value in range(1,11)] #create a new list of squares of numbers from 1 to 10    
print(myold_list)
    