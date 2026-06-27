#We will use the while loop to iterate over a list and the dictionary
x_list = [1,2,3,4,5,6,7,8,9,10]
while x_list:
    print(x_list)
    x_list.pop(0)

x_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
while x_dict:
    print(x_dict)
    x_dict.popitem()    
    
    
#filling dictionary with the user input
students={}
status_system = True
while status_system:
    name = input('Enter your name: ')
    response = input('Are you a student or a teacher? ')
    students[name] = response
    status_system = False
    break
print('\n \n')

#use do while to count  from 0 to 10
number = 0
while number < 10:
    print(number)
    number += 1
print('\n \n')

#use do while to count from 10 to 0
number = 10
while number > 0:
    print(number)
    number -= 1
    

#Example and Exercise number 3
#Using while loop with Lists and Dictionaries
