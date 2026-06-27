#learning about dictionaries in Python 
#What is a dictionary? A Python dictionary is a collection of items, similar to lists and tuples. However, unlike lists and tuples, each item in a dictionary is a key-value pair (consisting of a key and a value).
#We use curly braces {} to declare the dictionary

my_son = {'Name': 'Liqhame', 'Surname': 'Mathafeni', 'age': 3, 'Gender': 'Male', 'Location': 'Dutywa'} #Declaring the dictionary 
print(f'hellow {my_son['Name']} {my_son['Surname']} we have discovered that you are {my_son["age"]}yrs,{my_son['Gender']} in gender and you are living in {my_son['Location']}')

#Dictionary in simple terms can be defined as : A collection of  key-value pairs 

value_list =[1,2,3,5,6,]
value_tuple =(3,4,5,6,7,8,81,23)

my_new_dict = {'real_numbers':  value_list, 'any_nums': value_tuple }

#Embedding lists and tuples inside a dictionary and access the members 

print(my_new_dict['any_nums'])
