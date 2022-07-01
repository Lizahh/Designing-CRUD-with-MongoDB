import pymongo

# creating connection: 27017 is the id of local host on your computer of installed MongoDB. it can be checked with MongoDB compass as well

client = pymongo.MongoClient("mongodb://localhost:27017")

# make a database. MongoDB has its own DBs. if you give the name of db that doesnt exit,
# it will create the database of that name. if it exist, then it will create the connection with that DB
db = client['lib'] # lib means database for the library management system

# make a collection in db
# note: db has collections -> collections has records
books = db['books'] # here books is not a collection

print(books.update_one({

    # tell her which record to pick to update
    "name": "atomic habits"
    },

    # tell here, what do you want to update
    {
        # suppose we want to change only published
        "$set":{
            "published": 2025 } 
    }).modified_count       # modified_count is added here to check how many items are updated. use it if you want
)

# to update many items at the same time
print(books.update_many({

    # tell her which record to pick to update
    "name": "atomic habits"
    },

    # tell here, what do you want to update
    {
        # suppose we want to change only published
        "$set":{
            "published": 2025 } 
    })
)