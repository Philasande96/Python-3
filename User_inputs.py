#Learn about user inputs
#use of input() function to accept user input

#lets the user to enter their name
name = input("What is your name?")
print("Hello " + name)

#lets the user to enter their age
age = input("What is your age?")
print("You are " + age + " years old")

#lets the user to enter their gender
gender = input("What is your gender?")
print("You are " + gender)

#lets the user to enter their favorite color
color = input("What is your favorite color?")
print("Your favorite color is " + color)

#lets the user to enter their favorite food
food = input("What is your favorite food?")
print("Your favorite food is " + food)
#Now lets check the user is legible to vote. NB: Standard age to vote in South Africa is 18 and Above. 
current_year = 2026#set the current year to 2026
year_born = int(input("What is your year of birth?"))
age = abs(current_year - year_born)
if age < 18:#if the user is less than 18 years old
    print(f'you are {age} yrs this year')
    print("You illegible to vote this year")
else:#if the user is 18 years old or above
    print(f'you are {age} yrs this year')
    print("Welcome to voting system, you are legible to vote.")
    
#This topic is simple, but it is a good way to learn about user inputs
