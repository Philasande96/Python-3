#learn more about Python strings

"""
String in Python are referred to the sequence of characters, which can be of any length. Strings are enclosed in either single quotes (') or double quotes (").
Strings can be concatenated using the + operator.
Strings can be indexed and sliced.
"""
#Example 1
my_name = "Philasande"
print(my_name) #output Philasande

#Example 2: Combining two strings 
name = 'Philasande'
surname= 'Mathafeni'

print (name + " " + surname) #Output Philasande Mathafeni

#NB: Strings in Python can be sorrounded by single or double quotation marks
#example 3
single_quote = 'I am a single quote'
double_quote = "I am a double quote"

#Strings  variables contain literals. In Short, string value  in Python is referred to literal 

#NB: You can used quotes inside string  as long they don't match the quotes surrounding the entire literal 

#example 4

my_self = "I'm Philasande Mathafeni, Liqhame's father"
print(my_self) #Output I'm Philasane Mathafeni, Liqhame's father


#Multiline string. Let's say you want to assign a paragraph to your variable, you can do that by using triple/three  double or single  quotes 

about_Me = """
Philasande Mathafeni is a South African software engineer, entrepreneur, and tech innovator based in Queenstown. He is the founder and CEO of Macro-soft (Pty) Ltd, a technology company offering IT infrastructure solutions, web and app development, and technical support.
"""
print(about_Me) #Output Philasande Mathafeni is a South African software engineer, entrepreneur, and tech innovator based in Queenstown. He is the founder and CEO of Macro-soft (Pty) Ltd, a technology company offering IT infrastructure solutions, web and app development, and technical support.

#In Python strings are arrays, unlike any other language. Python does not have single character data type.
town = "Johannesburg"
#we can access any character using square brackets and the index number of the character in the name of  town assigned above. 
print(town[0]) #Output J
print(town[1]) #Output o

#Since we have agreed that strings are arrays in disguise, we can then loop through the string using a for loop.
for i in town:
    print(i) #Output J o h a n n e s b u r g
    
#Calculates how many characters are in the string using the built-in len() function
print(len(town)) #Output 11

#To check if a character or phrase in a string is present, we can the 'in' key work
#Lets check if we do have phila in the town literal
print("phila" in town) #Output False 
print('J' in town) #Output True

#We can emply the above code using if statement
if "phila" in town:
    print("We have phila in the town")
else:
    print("We don't have phila in the town")

#Lets check 'J' using for loop and if statement

for k in town:
    if('k' in town):
        print("We have k in the town")
    else:
        print("Nothing")
print("done!")

#To check if a certain character or Phrase IS NOT in the string literal we will use 'not in' key word

for y in town:
    if('J' not in town):
        print("We don't have y in the town")
        break #if you want the loop to check once and stop, you can use break statement to stop the loop from executing further
    else:
        print("We have J in the town")
        break
print("\nCompleted execution!\n")

#Use If 
real_numbers = "1234567890"
val='3405'
if val not in real_numbers:
    print(f"We don't have {val} in the real_numbers")
else:
    print(f"We have {val} in the real_numbers")
    
#Slicing strings 
#Slicing is a way to extract a portion of a string. In Python, you can slice strings using the colon (:) operator.

my_son="Liqhame"

print(my_son[0:3]) #Output Liq
print(my_son[3:]) #Output hame --> same as (3:len(my_son))
print(my_son[3:6]) #Output ham

#Negative index and slicing 

myString = "Python"
print(len(myString))   #Output 6
print(myString[-5:-2]) #Output yth

"""
| P    |  y   |  t   |  h   |  o   |  n |
| --- | --- | --- | --- | --- |--- |---|
|  0   |  1   |  2   |  3   |  4   |  5  | #Positive index
| -6   | -5   | -4   | -3   | -2   | -1  | #Negative index
"""
