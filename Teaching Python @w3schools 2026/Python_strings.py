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

