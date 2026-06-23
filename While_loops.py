
#learn about while loops
"""
What we know about loops? 
-Loops are used to repeat a block of code multiple times
-For Loops: They are used to repeat a block of code a fixed number of times
-While Loops: They are used to repeat a block of code until a condition is met
Lets learn about while loops

Instuctor: Philasande Mathafeni
Date: 22/06/2026 South Africa
"""

#lets print number 1 to 5 using while loop

current_number = 1 #set the current number to 1 or start
while current_number <= 5:#condition to evaluate if the current number is less than or equal to 5
    print(current_number)#print the current number/ first number on the loop
    current_number += 1#increment the current number by 1
print('\n\n')#open spaces by using new line

# lets print number 1 to 5 using for loop
for current_number in range(1,6):
    print(current_number)
print('\n\n')

#Letting user to choose when the loop should stop
prompt  ="I am a loop, I will keep going until you stop me. Do you want to stop me?"
choice = input(prompt)
if choice == 'yes' or choice == 'Yes':
    print('Okay, I will stop now')
elif choice == 'no' or choice == 'No':
    print('Okay, I will keep going')
    choice = input(prompt)
else:
    print('Invalid input')
    print(prompt)
print('\n\n')

# Lets print number 1 to 5 using while loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
    
#using flag  in the while loop

state = True
while state:
    print('I am a loop, I will keep going until you stop me. Do you want to stop me?')
    choice = input()
    if choice == 'yes' or choice == 'Yes':
        print('Okay, I will stop now')
        state = False
        break
    elif choice == 'no' or choice == 'No':
        print('Okay, I will keep going')
        choice = input()
    else:
        print('Invalid input')
        print('I am a loop, I will keep going until you stop me. Do you want to stop me?')
        choice = input()
print('\n\n')
