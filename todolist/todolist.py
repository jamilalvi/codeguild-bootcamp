'''
   This module implements the classes for the todo list application
'''

import datetime

class TodoItem(object):
   """Manage a single ToDo item"""
   #
   # Data to store:
   # text - the task the we want to do
   # date - the task was made
   # duedate - the date the task is due
   # who - who is to execute to task
   # status - what is the task's status
   #
   # Behaviors:
   # constructor - create a todo item
   # change status - set the status 
   # get data - return info about this item
   
   # Possible todo statuses
   STATUS_NEW = 'new'
   STATUS_COMPLETE = 'done'
   
   def __init__(self, text, owner=None, due_date_days_ahead=None):
      '''Create a new TodoItem.
      parameters:
      text: todo text
      owner: name of the user that owns this item
      due_date_days_ahead: number of days when this is due. If
      0, the item is due on the same day it was created. If > 0, 
      the item is due that many days forward. If none, there is no
      due date.'''

      self._todo_text = text
      
      # Will be None if owned by me
      self._owner = owner
      self._creation_date = datetime.datetime.today()
      
      # All newly created items have the status of new
      self._status = TodoItem.STATUS_NEW 
      
      # Validate any supplied due date
      if due_date_days_ahead is None:
         self._due_date = None
      else:
         # Save the due date 
         if due_date_days_ahead >= 0:
            self._due_date = self._creation_date + datetime.timedelta(days=1)
         else:
            # Throw an error
            raise ValueError("Due date cannot be in the past")
         
         
   def __str__(self):
      dueInfo = 'due: ' + str(self._due_date) if self._due_date else 'no due date' 
      return "ToDoItem: {0}, ({1})".format(self._todo_text, dueInfo)
         
   def mark_complete(self):
      ''''Mark this to-do item as complete'''
      self._status = TodoItem.STATUS_COMPLETE
      
   def mark_incomplete(self):
      '''Mark this to-do item as new (again)'''
      self._status = TodoItem.STATUS_NEW
      
   @property
   def text(self):
      return self._text
      
   @property
   def status(self):
      return self._status
      
   @property
   def owner(self):
      return self._owner
      
   @property
   def due_date(self):
      '''Returns a datetime if this todo item has a real due date. If there is 
      no due date, return None'''
      return self._due_date
      

      
      
   #~ def set_status(self, status):
      #~ if status in (TodoItem.STATUS_NEW, TodoItem.STATUS_COMPLETE):
         #~ self._status = status
      #~ else:
         #~ raise ValueError("Invalid status code: " + status)
      
   

#~ item = TodoItem("Pick up the kids", "jamila", 2)

   
   


class TodoListFileStorage(object):
   """Used by TodoList, this class takes care or saving a loading todo lists"""
   def __init__(self, filename):
      pass
      
   def write(self, todolist):
      pass
      
   def read(self):
      pass
   
   
   
   
class TodoCollection(object):
   """Manage a collection of ToDo items"""
   def __init__(self):
      pass
      
   def save(self, storage):
      # Just send the list of objects to the storage write method
      pass
      
   
   def load(self, storage):
      # Load the list of objects using the storage's read method
      pass
      
   
      
      
      
   
   
   

   