"""
Alex Chaban
Due 02-09-2023
Prof. Ionut Cardei
COP4045
Problem 3
"""
import csv


contacts = []

"""
Part C: Find contact
Conditions: A name or a nickname, the default value for both is an empty string, and will search both.
Returns None if a name or nickname is not found to a contact.
This is defined first in the program because the other functions can use it.
"""
def find_contact(name = "", nickname = ""):
    try:
        for i in contacts:
            if name in i or nickname in i:
                contact = i
        return(contact)
    except:
        return None
"""
Part A: Adding a contact
Conditions: A name, nickname, and a phone number.
Will replace any existing contact with the same name or nickname.
"""
def add_contact(name, nickname, phone):
    contact = find_contact(name)
    if contact == None:
        contacts.append([name, nickname, phone])
        contacts.sort()
        return True
    else:
        contacts.remove(contact)
        contacts.append([name, nickname, phone])
        contacts.sort()
        return False

"""
Part B: Removing a contact
Conditions: Contact exists
"""
def remove_contact(name):
    contact = find_contact(name)
    if contact == None:
        print("Contact not found.")
        return False
    else:
        contacts.remove(contact)
        contacts.sort()
        return True

"""
Part D: Saving to CSV file
Conditions: A CSV file name.
"""
def to_csv(file_name):
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Nickname", "Phone Number"])
        writer.writerows(contacts)
    f.close()

"""
Part E: Reading a CSV file
Conditions: A CSV File name.
"""
def read_csv(file_name):
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(','.join(row))
    f.close()

"""
Main Function
"""
def main():
    add_contact("Alex C", "anitsocial", "123-456-7890")
    add_contact("Spamton G Spamton", "DO NOT CALL", "999-999-9999")
    add_contact("Brock Samson", "Venture Brother", "111-111-1111")
    add_contact("Sam and Max", "Freelance Cops", "888-888-8888")
    add_contact("CL4P-TR4P", "Annoying Robot", "555-555-5555")
    add_contact("Ash Williams", "Zombie Exterminator", "222-222-2222")
    add_contact("GLADoS", "Aperture Admin", "000-000-0000")

    remove_contact("Alex C")
    remove_contact("DO NOT CALL")

    to_csv("contacts.csv")
    read_csv("contacts.csv")

main()