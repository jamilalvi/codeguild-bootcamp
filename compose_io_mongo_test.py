import datetime           
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint


def mongo_test():

   # Connection url
   MONGOHQ_URL = "mongodb://codeguild:AsecretPassw00rd@dharma.mongohq.com:10023/qscfadm"
         
   # Connect
   client = MongoClient(MONGOHQ_URL)
    
   # Specify the database
   db = client.qscfadm

   # Use the codeguild collection
   collection = db.codeguild
   count = collection.count()

   print "The number of documents you have in this collection is:", count
     
   # Find by id
   #print collection.find_one({'_id': ObjectId('54bf02c0fcf43411146f4e77')})
   
   # Get the to-do list user collection
   print collection.find_one({'docname': "todo-user-list"})
   
mongo_test()