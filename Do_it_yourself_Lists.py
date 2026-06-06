#Try it yourself / exercises in chapter 3 of Python Crash Course book by Eric Matthes

#3-1 Names: Store the names of a few of your friends in a list called names. Print each person's name by accessing each element in the list, one at a time.
names = ['Liqhame', 'Namvura', 'Charlie', 'David', 'Mack', 'Sizwe']

#Method 1 - Individually accessing each element in the list
print(names[0]) #This method will print the first item in the list, which is 'Liqhame'.
print(names[1]) #This method will print the second item in the list, which is 'Namvura'.
print(names[2]) #This method will print the third item in the list, which is 'Charlie'.
print(names[3]) #This method will print the fourth item in  the list, which is 'David'.
print(names[4]) #This method will print the fifth item in the list, which is 'Mack'.
print(names[5]) #This method will print the sixth item in the list, which is 'Sizwe'.   


#Method 2 - Using a for loop to access each element in the list
for i in names:
    print(i) #This method will print each item in the list separately, one at a time.   

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person's name, print a message to them. The text of each message should be the same, but each message should be personalized with the person's name.
for r in names:
    print("Hello " + r + ", how are you doing today?") #This method will print a personalized message for each person in the list, using their name. The message will be the same for each person, but it will be personalized with their name.     
