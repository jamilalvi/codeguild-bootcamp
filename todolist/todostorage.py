import json
import csv
from pymongo import MongoClient

# Compose.io url
MONGOHQ_URL = "mongodb://codeguild2:pleese-keep-secret@dharma.mongohq.com:10023/qscfadm"


def get_storage_class(format):
   '''Given a file type, return a class that can store that format'''
   kStgMap = {
      'json' : TodoListJsonFileStorage,
      'csv' : TodoListCSVFileStorage,
      'cloud' : TodoListCloudStorage
   }
   
   try:
      return kStgMap[format.lower()]
   except KeyError:
      return None
      

class TodoListJsonFileStorage(object):
   """Used by TodoList, this class takes care or saving a loading todo lists as a json file"""
   def __init__(self, filename):
      self._filename = filename + '.json'
      
   def write(self, todolist):
      with open(self._filename, 'w') as fp:
         json.dump([itm.serialize() for itm in todolist], fp)
      
   def read(self):
      with open(self._filename, 'r') as fp:
         return json.load(fp)
         


class TodoListCloudStorage(object):
   def __init__(self, colName):
      # For cloud storage, we must make filename (as a collection name) unique... (os.getlogin())
      self._collectionName = 'jamil_' + colName[6:]

   def _connect(self):
      # Connect & get a ref to the database & collection. These attributes dynamically added to client object
      self._mongo_client = MongoClient(MONGOHQ_URL)
      self._mongo_db = self._mongo_client.qscfadm
      
   def write(self, todolist):
      self._connect()
      
      # Remove al existing documents 
      self._mongo_db[self._collectionName].remove({})
   
      # Convert to serialized format, then insert all the todo items in the list
      self._mongo_db[self._collectionName].insert_many([itm.serialize() for itm in todolist])
      
   def read(self):
      # Fetch all the items into the cursor & turn into a list
      self._connect()
      return list(self._mongo_db[self._collectionName].find({}))
   
   
class TodoListCSVFileStorage(object):
   '''Used by TodoList, this class saves & loads to a CSV file'''
   def __init__(self, filename):
      self._filename = filename + '.csv'
      
   def write(self, todolist):
      with open(self._filename, 'wb') as csvfile:
         cwriter = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
         for itm in todolist:
            d = itm.serialize()
            cwriter.writerow((d['id'], d['text'], d['status'], d['duedaysahead'], d['creationdate']))

   def read(self):
      with open(self._filename, 'rb') as csvfile:
         creader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
         return [{'id':row[0], 'text':row[1], 'status':row[2], 'duedaysahead':int(row[3]), 'creationdate':row[4]} for row in creader]

