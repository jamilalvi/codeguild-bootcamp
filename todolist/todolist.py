'''
   This module implements the classes for the todo list application
'''

import datetime, uuid


class TodoItem(object):
   """Manage a single ToDo item"""
   #
   # Data to store:
   # text - the task the we want to do
   # date - the task was made
   # duedate - the date the task is due
   # status - what is the task's status. how do you want to track this state?
   #
   # Behaviors:
   # constructor - create a todo item
   # change status - set the status 
   # get data - return info about this item
   
   # Possible todo statuses
   STATUS_NEW      = 'new'
   STATUS_COMPLETE = 'done'

   @classmethod
   def create_from_dict(cls, jd):
      '''Alternate constructor. Re-create the object from a dictionary'''
      newobj = cls(jd['text'], jd['duedaysahead'])
      newobj._creation_date = datetime.datetime.strptime(jd['creationdate'], "%Y-%m-%dT%H:%M:%S.%f")
      newobj._status = jd['status'] 
      newobj._id = jd['id']
      
      # Reuse this code to update the due datetime
      newobj._update_due_date()
      return newobj
      
      
   def __init__(self, text=None, due_date_days_ahead=None):
      '''Create a new TodoItem.
      parameters:
      text: todo text
      due_date_days_ahead: number of days when this is due. If
      0, the item is due on the same day it was created. If > 0, 
      the item is due that many days forward. If none, there is no
      due date.'''

      # Save the text
      self._todo_text = text.strip()
      if not self._todo_text:
         raise ValueError("Todo item text cannot be empty")
         
      if (hasattr(due_date_days_ahead, 'lower') and len(due_date_days_ahead) > 0) or isinstance(due_date_days_ahead, int):
         # This will raise a ValueError if the supplied string is not a number
         self.due_date_days_ahead = int(due_date_days_ahead)
      else:
         self.due_date_days_ahead = None

      self._check_assigned()
      self._creation_date = datetime.datetime.today()
      
      # All newly created items have the status of new
      self._status = TodoItem.STATUS_NEW 
      
      # Create a unique id
      self._id = uuid.uuid4()
      
      # Validate any supplied due date
      self._update_due_date()
         
         
   def __repr__(self):
      '''For debugging'''
      return '<TodoItem: {0}> {1}'.format(self._id, self.__str__())
      
   def __str__(self):
      '''String representation for simple console printout'''
      dueInfo = self._due_date.strftime("%b %d") if self._due_date else '[none]' 
      return "{1}\t{2}\t{0}".format(self._todo_text, dueInfo, self._status)
         
         
   def _update_due_date(self):
      '''Validate the current days ahead due date'''
      if self.due_date_days_ahead is None or self.due_date_days_ahead == -1:
         self._due_date = None
      else:
         # Save the due date 
         if self.due_date_days_ahead >= 0:
            self._due_date = self._creation_date + datetime.timedelta(days=self.due_date_days_ahead)
         else:
            # Throw an error
            raise ValueError("Due date cannot be in the past")
            
         
   def serialize(self):
      '''Return a simplified representation suitable for serialization'''
      return {'id': str(self._id), 'text':self._todo_text, 
              'duedaysahead': self.due_date_days_ahead if self.due_date_days_ahead else -1, 
              'status': self._status, 'creationdate': self._creation_date.isoformat()}
              
   def _check_assigned(self):
      '''Check if this todo item should be assigned to someone else'''
      if '@' in self._todo_text:
         pass
      
      
   def mark_complete(self):
      ''''Mark this to-do item as complete'''
      self._status = TodoItem.STATUS_COMPLETE
      
   def mark_incomplete(self):
      '''Mark this to-do item as new (again)'''
      self._status = TodoItem.STATUS_NEW
      
   @property
   def text(self):
      return self._todo_text
      
   @text.setter
   def text(self, txt):
      self._todo_text = txt
      
   @property
   def status(self):
      return self._status
   
   @status.setter
   def status(self, sta):
      self._status = sta
      
   @property
   def due_date(self):
      '''Returns a datetime if this todo item has a real due date. If there is 
      no due date, return None'''
      return self._due_date
      
   @due_date.setter
   def due_date(self, dd_days):
      self.due_date_days_ahead = dd_days
      self._update_due_date()
      
      
      
   
class TodoCollection(object):
   """Manage a collection of ToDo items"""
   def __init__(self):
      self.items = []
      self._iter_idx = 0
      
   def add(self, tditem):
      self.items.append(tditem)
      
   def __iter__(self):
      self._iter_idx = 0
      return self
      
   def __len__(self):
      return len(self.items)
      
   def __getitem__(self, idx):
      '''Access by zero-based index'''
      return self.items[idx]
      
   def next(self):
      '''Iterator to return todo items'''
      try:
         itm = self.items[self._iter_idx]
         self._iter_idx += 1
         return itm         
      except IndexError:
         raise StopIteration

   def sort(self):
      def cmp(a, b):
         # Some values might be None
         if a and not b:
            return -1
         elif b and not a:
            return 1
         elif a and b:   
            if a > b:
               return 1
            elif a == b:
               return 0
            else:
               return -1
         else:
            return 0
         
      # Sort list inplace on item due date
      self.items.sort(key=lambda itm: itm._due_date, cmp=cmp)
      
   def save(self, storage):
      # Just send the list of objects to the storage write method
      storage.write(self.items)
   
   def load(self, storage):
      '''Load the list of objects using the storage's read method'''
      # Get the list of items as a list of dicts & replace any existing items 
      loadedList = storage.read()
      if loadedList:
         self.items = [TodoItem.create_from_dict(itmData) for itmData in loadedList]
         
      

   