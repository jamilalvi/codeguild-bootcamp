from todolist import TodoList, TodoItem


class ToDoListApp(object):
   
   def show_banner(self):
      """Display the application welcome banner"""
      print "\n\nWelcome to the ToDo list application\n\n"
      
      
   def add_command(self, todolist):
      print "add"
      
      
   def command_loop(self):
      """Main command loop for todo list application"""
      
      self.show_banner()
      
      # This class manages my todo list
      tdlist = TodoList()
      
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
            self.add_command(tdlist)
            
            
         else:
            print "Unknown command:", command
         
         
      print "Goodbye"
         


# Bootstrap the application
tdlist = ToDoListApp()
tdlist.command_loop()
