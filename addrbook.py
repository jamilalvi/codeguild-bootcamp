'''
   Address book challenge
'''

import json

# Constants
ADDRESS_BOOK_FILE = "address_book.dat"

def show_menu():
   '''Display the menu of available commands and return the selected choice'''
   print "\nAvailable commands are:"
   print " add - add a contact"
   print " delete - delete a contact"
   print " find - find a contact by name"
   print " update - update information for a contact"
   print " list - list all contacts"
   print " save - contacts to address book file"
   print " load - load contacts from an address book file"
   print " quit - exit this program\n"
   
   choice = raw_input("Enter address book command: ")
   print ""
   return choice.strip()
   
def add_new_contact(book):
   newinfo = raw_input("Enter name, phone number separated by a comma: ")
   
   # Parse the string into name & phone & add to address book indexed by name
   parts = newinfo.split(',')
   if len(parts) != 2:
      print "Bad record format. Unable to add contact"
   else:
      book[parts[0].strip()] = {'ph':parts[1].strip()}
   
def delete_contact(book):
   name = raw_input("Name of contact to delete: ")
   
   # Look it up & trap for attempt to delete non-existant contact
   try:
      del book[name]
   except KeyError as e:
      print "Contact", name, "not found"
   else:
      print "Contact", name, "deleted"
   
def update_contact(book):
   name = raw_input("Name of contact to update: ")
   
   # Look it up & trap for attempt to update non-existant contact
   if name in book:
      book[name]['ph'] = raw_input("New phone number: ")
      print "Contact", name, "updated"
   else:
      print "Contact", name, "not found"
      
      
def find_contact(book):
   name = raw_input("Name of contact to find: ")
   
   # Look it up
   if name in book:
      display_contact(book, name)
   else:
      print "Contact", name, "not found"
      
      
def display_contact(book, contact_name):
   '''Display a single contact card'''
   print "Name:\t%s\nPh:\t%s\n" % (contact_name, book[contact_name]['ph'])
   
   
def list_contacts(book):
   if len(book) == 0:
      print "\nAddress Book is empty"
   else:
      print "\nContents of Address Book:"
      for contact in book:
         display_contact(book, contact)
         
      
def save_contacts(book):
   output_file = open(ADDRESS_BOOK_FILE, "wb")
   json.dump(book, output_file)
   output_file.close()
   
   
def load_contacts(book, filename):
   '''Load the address book from the specified file. Return the number of loaded contacts'''
   output_file = open(ADDRESS_BOOK_FILE, "rb")
   
   # Overwrite current contents of address book
   book.clear()
   book.update(json.load(output_file))
   
   output_file.close()
   return len(book)
   
   
def main():
   # Address book is stored in this variable
   address_book = {}

   print "\nAddress Book Program\n"
   
   # Keep prompting the user until they enter a command
   while True:
      # Prompt user. If they enter quit, break out of loop
      choice = show_menu()
      if choice == 'quit':
         print "Thanks for using the address book. Goodbye"
         break
         
      elif choice == 'add':
         add_new_contact(address_book)
         
      elif choice == 'delete':
         delete_contact(address_book)
         
      elif choice == 'list':
         list_contacts(address_book)
         
      elif choice == 'update':
         update_contact(address_book)
         
      elif choice == 'find':
         find_contact(address_book)
         
      elif choice == 'save':
         save_contacts(address_book)
         
      elif choice == "load":
         print " Loading address book from file..."
         rec_count = load_contacts(address_book, ADDRESS_BOOK_FILE)
         print " Done. %d contacts loaded" % (rec_count,)
         
      else:
         print "I'm sorry, I don't know that command"
         
         
main()




