#----
# Jay C. Parangalan, CIT-95 Fall 2023
# Python Program Three assignment
#----

#==== configuration
contact_file = "contacts.dat"

#==== functions

#----
# Get contact info from user and add a contact dict to the given list.
#
def add_contact(contact_list):
    contact = {}    # create new blank contact
    contact["Name"] = input("Name: ")   # get input data from user
    contact["Phone"] = input("Phone: ")
    contact["Email"] = input("Email: ")
    contact_list.append(contact)        # add new contact to given list

#----
# Display each contact in the given list of contacts.
#
# Since the dict keys are already in human readable format,
# we can just display key, value pairs.
#
def view_contacts(contact_list):
    if len(contact_list) == 0:  # check if any contacts to display
        print("")
        print("No contacts entered yet.")
    else:
        for contact in contact_list:    # display all contacts in the list
            view_contact(contact)

#----
# Display a single contact.
#
def view_contact(contact):
    print("")
    for k,v in contact.items(): # just print key, value pairs
        print(k, ":", v)

#----
# Search the given list for contact names by substring.
#
def search_contact(contact_list):
    for contact in contact_list:
        found = 0
        print("")
        search = input("Search contacts for: ") # get substring to search  for
        if contact["Name"].find(search) >= 0:
            view_contact(contact)   # display all contacts with substring
            found += 1
    if found == 0:      # friendly note if substring not found anywhere
        print("No contacts found.")

#==== main
contacts = []   # no contacts yet

try:    # read any contacts already stored in the data file
    with open(contact_file, "r") as input_file:
        contacts = eval(input_file.read())
    input_file.close()
except:
    print("No previous contacts found.")

input_mode = True
while input_mode:
    print("")   # display the main menu
    print("1. List all contact details")
    print("2. Add a contact")
    print("3. Find a contact")
    print("4. Exit and save contacts to file.")
    try:
        selection = int(input("Enter your selection: "))
    except:
        selection = -1  # just treat as an invalid selection

    if selection == 1:  # big list of all contact details
        view_contacts(contacts)
    elif selection == 2:
        add_contact(contacts)   # get new contact and add to global list
    elif selection == 3:
        search_contact(contacts)
    elif selection == 4:
        input_mode = False
    else:
        print("")
        print("Invalid selection, please try again.")

print("")
if len(contacts) > 0:   # no point creating a file if nothing to write
    try:
        with open(contact_file, "w") as output_file:     # overrite if exists
            output_file.write(str(contacts))
            output_file.close()
        print("Saved", len(contacts), "contacts to data file.")
    except Exception as e:
        print("ERROR: unable to write updates to contact data file")
        print(e)

