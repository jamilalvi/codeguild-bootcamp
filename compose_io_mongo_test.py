import datetime           
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

# Mongo docs: http://docs.mongodb.org/manual/core/crud-introduction/

def mongo_test():

   # Connection url to server includes username, password & database
   MONGOHQ_URL = 'xxxxxxxxxxxxxxxxxxxx'

   # Connect
   client = MongoClient(MONGOHQ_URL)
    
   # Specify the database. Attributes dynamically added to client object
   db = client.qscfadm

   # Print all the collection names in this db
   pprint.pprint(db.collection_names())

   
   # Use the codeguild collection. Can also use db["codeguild"]
   collection = db.codeguild
   print "The number of documents you have in this collection is:", collection.count()
     
   # Find by id
   pprint.pprint(collection.find_one({'_id': ObjectId('54bf02c0fcf43411146f4e77')}))

   
   # Get the to-do list user collection
   pprint.pprint(collection.find_one({'docname': "todo-user-list"}))
   
   # Create a new document
   monster = {
      "name": "Martians",
      "occupation": "Alien abductions",
      "tags": ["little", "green", "men", "outer-space"],
      "date": datetime.datetime.utcnow()
   }
    
   # Insert the monster document into the collection
   monster_id = collection.insert(monster)
   
   # Print out all our documents where there is an occupation key
   for monster in collection.find({"occupation" : {'$exists' : True}} ):
      pprint.pprint(monster)
   
   
   
   
   
   
mongo_test()