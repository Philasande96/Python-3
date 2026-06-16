#learning about dictionaries in Python 
#What is a dictionary? A Python dictionary is a collection of items, similar to lists and tuples. However, unlike lists and tuples, each item in a dictionary is a key-value pair (consisting of a key and a value).
#We use curly braces {} to declare the dictionary

my_son = {'Name': 'Liqhame', 'Surname': 'Mathafeni', 'age': 3, 'Gender': 'Male', 'Location': 'Dutywa'} #Declaring the dictionary 
print(f'hellow {my_son['Name']} {my_son['Surname']} we have discovered that you are {my_son["age"]}yrs,{my_son['Gender']} type of gender and you are living in {my_son['Location']} \n')

#Dictionary in simple terms can be defined as : A collection of  key-value pairs 

value_list =[1,2,3,5,6,]
value_tuple =(3,4,5,6,7,8,81,23)

my_new_dict = {'real_numbers':  value_list, 'any_nums': value_tuple }

#Embedding lists and tuples inside a dictionary and access the members 

print(my_new_dict['any_nums'])

#A key-value pair is a set of values associated to each other.
#when you call a key, Python will return the value associated with that key.
#Dictionaries are dynamic, meaning you can add or introduce new members (key-value pairss) at anytime.
#Let's create a food list dictionary and amend or add new members

hotel_menu ={'morning': ['coffee','tea','milk','bread','corn flakes','coco pops'], 'lunch':['chicken','mutton','pork','rice','pap'],'dinner':['rice','pap','samp', 'beef stew','mutton stew'], 'extras':['dessert','biscuits','juice','pop corns']}

print('\nWe have the following  extras')
print('\n', hotel_menu['extras'], '\n')#display the items in an extras  menu, but this include the square brackets and ' '
for i in hotel_menu['extras']:
    print(i)#display items in the extras menu omitting the square brackets and ' '

#Now lets add  new  items in the menu
hotel_menu['beverages'] = ['beer','mqombothi','ginger','whiskey','brandy']
print(hotel_menu)

#Sometimes you can start with an empty dictionary. To start with an empty dictionary, declare the  dictionary name followed by  empty curley braces.
#e.g dictionary_name={} --> empty braces {}
domestic_animals ={} #declaring the empty dictionary 

#add new animals in the domestic animals dictionary
domestic_animals['bipedals']=['Hen','ostrich']#add two animals in the bipedals value-pair key
domestic_animals['quard-pedals']=['cow','dog','horse','cat']
print(domestic_animals['bipedals'])

