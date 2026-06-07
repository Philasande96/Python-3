
#3-4 Guest list: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you'd like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

invitees = ['Albert Einstein', 'Marie Curie', 'Leonardo da Vinci','Philasande']#declare a list of invitees
for invitee in invitees:#loop through the list of invitees
    print(f"Dear {invitee}, I would like to invite you to dinner. It would be an honor to have you as my guest.")

#3-5- Changing Guest List: You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
#Start with your program from Exercise 3-4. Add a print statement at the end of your program stating the name of the guest who can’t make it.
#Then modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#Print a second set of invitation messages, one for each person who is still invited.


prev_invites = invitees.copy()#make a copy of the original list of invitees
unable_to_attend = 'Marie Curie'#declare the name of the guest who can't make it
print(f"Unfortunately, {unable_to_attend} can't make it to the dinner.")
invitees.remove(unable_to_attend)#remove the name of the guest who can't make it
new_invitee = 'Nikola Tesla'#declare the name of the new guest
invitees.append(new_invitee)#add the new guest to the list of invitees
for invitee in invitees:#loop through the updated list of invitees
    print(f"Dear {invitee}, I would like to invite you to dinner. It would be an honor to have you as my guest.")    
print()

#using sort and sorted methods to sort the list
new_list_cars = ['Toyota', 'Honda', 'Ford', 'BMW', 'Audi']#declare a list of cars
print("Original list of cars:", new_list_cars)  

print("\n")
new_list_cars.sort(reverse=True)#sort the list of cars in place
print("Sorted list of cars (using sort()):", new_list_cars)

#try it yourself in  Sorting the Lists
#Sort method 
myList = ['banana', 'apple', 'cherry', 'date']#declare a list of fruits
print("Original list of fruits:", myList)
myList.sort()#sort the list of fruits in place
print("Sorted list of fruits (using sort()):", myList)

#Sorted function
myList2 = ['grape', 'fig', 'elderberry', 'honeydew']#declare another list of fruits
print("\nOriginal list of fruits:", myList2)
sorted_list = sorted(myList2)#sort the list of fruits and create a new sorted list
print("Sorted list of fruits (using sorted()):", sorted_list)







