from todolist import TodoList, TodoItem


class ToDoListApp(object):
   
   def __init__(self):
      self.tdlist = TodoList()
      
   def show_banner(self):
      """Display the application welcome banner"""
      print "\n\nWelcome to the ToDo list application\n\n"
      
   def delete_command(self, todo_list):
      print "this is delete_command"
      
   def add_command(self):
      '''Implement the add todo item operation'''
      # Collect all to-do item info from user
      raw_input( )
      
      # Create a TodoItem & populate it with the data
      
      # Store it to out to-do list
      self.tdlist.add( ?? )
      
      print "add"
      
      
   def command_loop(self):
      """Main command loop for todo list application"""
      
      self.show_banner()
      
      # This class manages my todo list
      #tdlist = TodoList()
      
      # Current command the user entered
      command = ""
      
      # Main command loop - ask for the command and execute it. Quit if user enters 'quit'
      while command != "quit":
         command = raw_input("What is your command: ").strip().lower()
         if not command:
            continue
            
         if command == "quit":
            break
            
         #print "Executing", command
         
         if command == 'add':
            self.add_command()
            
         elif command == 'delete':
            self.delete_command()
            
         else:
            print "Unknown command:", command
         
         
      print "Goodbye"
         


# Bootstrap the application
tdlist = ToDoListApp()
tdlist.command_loop()










