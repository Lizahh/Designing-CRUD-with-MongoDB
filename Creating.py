
# we can also call creating as inserting
import pymongo

# creating connection

client = pymongo.MongoClient("mongodb://localhost:27017")

# make a database. MongoDB has its own DBs. if you give the name of db that doesnt exit,
# it will create the database of that name. if it exist, then it will create the connection with that DB
db = client['lib'] # lib means database for the library management system

# make a collection in db
# note: db has collections -> collections has records
books = db['books'] # here books is not a collection

# lets add record to this collection: add in the form of dictionary
#books.insert_one({
 #   "name": "atomic habits",
  #  "author": "james clear",
   # "published": 2019
    #})

# we can also insert so many records: for it, we pas list of dictionaries
books.insert_many([
    {
    "name": "Atomic habits",
    "author": "Jimmy Clear",
    "published": 2015
    },
    {
    "name": "The Quirky",
    "author": "Schilling",
    "published": 2019
    }
    
    ])

