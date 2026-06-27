#Working with user input and while loop
"""
for user inputs
- Will write a program that will ask a user an input and work with that input
-Will use input() function to get the user input
"""
#Program below ask  user their age and check if the user is legible to vote, please note  standard age is 18 years old
current_year = 2026
user_age = input("When are you born? (Please enter a year): ") #input() function will take the input from the user and store it in the variable user_age
user_age = int(user_age) if user_age else current_year
age = (abs(current_year - user_age))
age_to_vote = abs(age - 18)
if age >= 18:
    print("You can proceed to voting station")
else:
    print(f"You are NOT old enough to vote \nTry in {age_to_vote} years, in {user_age+age_to_vote} instead")
#This program above will ask the user the year at which user was born, and then check if the user is old enough to vote, if not it will tell the user how many years they need to wait and how many years they have already waited.
#This is a simple input() function program.
"""
Try it yourself
7-1. Rental Car: Write a  program that asks the user what kind of rental  car they would like. Print a message about that car, such as 'Let me see if i can find you a {user's car choice} car.'

7-2. Restaurant: Write a program that asks the user how many people are in  their dinner group. If the answer is more than 8, print message saying  they'll have to wait for a table. Otherwise, report that their table is ready.

7-3. Multiples of Ten:  Ask the user for a number, an then report whether the number is a multiple of ten or not.

"""

#7-1

car_choice = input("What kind of car would you like to rent? ")
print(f"Let me see if i can find you a {car_choice} car.")

#7-2
pep_in_group= input("How many people are in your group? ")
pep_in_group = int(pep_in_group) if pep_in_group else 0
if pep_in_group > 8:
    print("You'll have to wait for a table")
else:
    print("Your table is ready")
    
#7-3
multiple_of_ten = input("What is the number? ")
multiple_of_ten = int(multiple_of_ten) if multiple_of_ten else 0
if multiple_of_ten % 10 == 0:
    print("It's a multiple of ten")
else:
    print("It's not a multiple of ten")
print('\n \n')
"""
Working with while loop
"""
#For loop  iterates through the list or collection. OR For loop iterates through the range of numbers, OR For loop  is used when you know the end value.

#For Loop to print out the list of vegetable 
vegetable_list = ["carrot", "potato", "tomato", "cucumber", "onion", "lettuce", "pepper", "spinach"]
for vegetable in vegetable_list:
    print(vegetable)
print('\n \n')
#This program above will print out the list of vegetable and not going to repeat that again when the last vegetable 'Spinach' is printed out.
#OR 
#For loop to print numbers from 0 to 10
for i in range(10): #or you can  add the starting value which 0
    print(i)
    
print('\n \n')
#Lets  print 1 to 5 in while loop
start_number = 1
end_value = 10
while start_number <= end_value:
    print(start_number)
    start_number += 2 #to avoid infinite loop use incremental value


#Letting user choose when to quit the program
prompt ='\nTell me something, and I will repeat it back to you:'
prompt +="\n Enter 'quit' to quit the program " #this prompt statement iterate
message ='' #this variable will store the user input
while message != 'quit': #Set condition to quit the program
    message = input(prompt)
    print(message)
#We will introduce flags in the next lesson.
#flag is a variable that is used to store a boolean value, which can be either True or False. we use it if our system or program has many  conditions to check inside while loop.
#we will use the above program 'quit'   but we will use the flag

active = True #declate the flag
print('Welcome to version 2 program of user inputs to exit program')
while active: #Set condition to quit the program
    message = input(prompt)
    if message == 'quit':
        active = False
        print("Goodbye, thanks for using the program")
    else:
        print(message)  

#using break to exit the loop
#To exit the loop immediate without running other remaining code  irregardless of the condition
#We will break the loop when our counter is equal to 10
counter = 0
while counter < 20:
    counter += 1
    print(counter)
    if counter == 10:
        print(f"program stopped to count at {counter}")
        break
print('\n \n')



