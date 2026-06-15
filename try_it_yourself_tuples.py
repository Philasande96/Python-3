
#Try it yourself in tuples.
"""
4-13: buffet: A buffet-style restraurant offers only five  basic foods.

Think of five smple foods, and store them in a tuple.

a. use for loop to print ach food the restaurant offers
b. Try to modify one of the items, and make sure that Python rejects the change.
c. The restaurant changes its menu, replacing two of the items with different foods. Add a blovk of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
"""

#declare the menu of the restaurant
buffet_menu = ('Fish','Bread', 'Mutton','Rice','Roasted Chicken') #create the menu tuple
#question a. 
#looping around the food menu and display 
print("\nAvailable Menu \n")
for x in buffet_menu:
    print(x)

#question b.
#Unlawful modifications of the tuple (I will comment this for the sake of not disturbing compiler from displaying the next line)
#buffet_menu[0]='Coffee'


#question c.
#Restaurant  is replacing two  items in their old menu 

print('\nUpdated Menu: \n')
buffet_menu =('Coffee','Cold Drink','Pap','Mutton','Rice','Roasted Chicken')
for z in buffet_menu:
    print(z)