
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