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
        break
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

#Python Modify strings 
#Python has set of of built-in methods that can be used to modify strings.

#Upper case-> used to return the literal in upper case 

First_name = 'philasande mathafeni'
print(First_name.upper()) #Output PHILASANDE

#Lower case -> used to return string literal in lower case 
print(First_name.lower()) #Output philasande

#Capitalize -> used to capitalize the first character in  a string\sentence
print(First_name.capitalize()) #Output Philasande mathafeni

#Removing the Whitespace
#Whitespace are the spaces left before and after (beginning or end) of the string
#use strip() method to perform such activity 
example = " Philasande Mathafeni "
print(len(example)) #Output 22 -> Note this includes spaces 
stripped_example = example.strip()
print(len(stripped_example)) #Output 20 -> Note this does not include spaces, meaning  2 spaces are removed

#Replacing a string with another string. 
#We will use replace() method to do so. Replace method takes to arguments\parameters  to  successfully perform this duty, string to be replaced and the string to replace with

names = "Liqhame Nqobile"
replaced_names = names.replace('Liqhame', 'Philasande')
print(replaced_names) #Philasande Nqobile
#We will use for loop and if statement to check if the string has been replaced successfully
for i in names:
    if 'Philasande' in names:
        print("String has been replaced successfully \n")
        print(names.replace('Liqhame', 'Philasande'))
        #Output Philasande Nqobile
        print('\n \n')
        break
    else:
        print("String has not been replaced successfully")
        break
        
#Splitting a string into a list of substrings.
#We will use split() method to perform this activity. The split() method splits a string
naming = 'Philasande mathafeni dlamini'
print(naming.split()) #Output ['Philasande', 'mathafeni', 'dlamini'] -> Note that the default separator is any whitespace

#String concatinating\merging 
#We will use the + operator to concatinate two strings or to combine  strings 

name = 'Philasande'
surname = 'Mathafeni'

fullname = name + " " + surname #concatinating two strings using + operator
print(fullname) #Output Philasande Mathafeni

#NOTE : String formatting and character escape, I have dealt with in Python 3 main folder


#String Methods

#capitalize() : converts the first character in the string 
txt = 'i am fine, i hope you are enjoying  your day'
print(txt.capitalize() + "\n") #Output I am fine, i hope you are enjoying  your day
#casefold(): converts the string into lower case
txt = 'I AM FINE, I HOPE YOU ARE ENJOYING  YOUR DAY'
print(txt.casefold()) #Output i am fine, i hope you are enjoying  your day

#center(): returns centerd string

names = 'Philasande'
print(names.center(20)) #Output '     Philasande      ' -> Note that the string is centered in a field of 20 characters wide, with spaces added to the left and right

#count(): returns the number of times a specified value occurs in a string
txt = 'I am fine, I hope you are enjoying your day'
print(txt.count('I')) #Output 2 -> Note that the count() method is case-sensitive, so it will only count the occurrences of the exact string specified.

#encode(): returns encoded version of a string 
mine = 'Philasande'
print(mine.encode()) #Output b'Philasande' -> Note that the encode() method returns a bytes object, which is a sequence of bytes. The bytes object is then encoded into a string using the encoding specified.

#endswith(): returns True if the string ends with the specified value, otherwise returns False
mine = 'Philasande'
print(mine.endswith('nde')) #Output True

#expandtabs(): returns a copy of the string with tabs expanded
mine = 'I\tam\tfine'
print(mine.expandtabs()) #Output I        am        fine

#format(): formats specified values in a string
txt = 'I am {} and I am {} years old'
print(txt.format('Philasande', 30)) #Output I am Philasande and I am 30 years old

#find(): returns the index of the first occurrence of the specified value in the string, or -1 if the value is not found
mine = 'Philasande'
print(mine.find('nde')) #Output 7 -> Note that the find() method is case-sensitive, so it will only find the first occurrence of the exact string specified.