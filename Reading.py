
# we can also called reading as querying or finding
import pymongo

# creating connection: 27017 is the id of local host on your computer of installed MongoDB. it can be checked with MongoDB compass as well

client = pymongo.MongoClient("mongodb://localhost:27017")

# make a database. MongoDB has its own DBs. if you give the name of db that doesnt exit,
# it will create the database of that name. if it exist, then it will create the connection with that DB
db = client['lib'] # lib means database for the library management system

# make a collection in db
# note: db has collections -> collections has records
books = db['books'] # here books is not a collection

# the following line just print the memory location where the records of the collection lies
print(books.find())

# the following line will display all the records of the collection books
print([*books.find()])

# the following line will find a specific record from collection: find() ki () bracket k andr dena eh jo find krna eh in form of dictionary: {}
print("\n\n finding a specific record:")
print([*books.find({
    "name": "atomic habits"
    
    })])

# suppose we want to show only the published year, instead of showing whole dictionary in the output
# for it, we will set "published": 1, and all remaining will be automatically zero. we do not need to write the remainings.

print("\n\n finding with selection:")
print([*books.find({
    "name": "atomic habits"
    },
    # this is called the "selection" area
    {
    "published": 1               
    # if we want to show two things on:
    # {
    # "published": 1 , # use comma here             
    # "author": "jims clear"
    # }
    # id is always returned. but you can also set id: 1 to show up must
        }                   
    )])


# to sort according to a specific attribute name
print("\n\n sorting: ")
print([*books.find().sort("published")])

# if we pass 1 it will sort from smaller to bigger: ascending order
# if we pass -1 it will sort from bigger to smaller: descending order
print("\n\n ascending sorting: ")
print([*books.find().sort("published", 1)])

print("\n\n descending sorting: ")
print([*books.find().sort("published", -1)])

print("\n\nto show specific results after finding:\n ")
# to show specific results after finding: suppose we want to show 2 results
print([*books.find().sort("published", -1).limit(2)])

# we can make a query
query = {
    "name": "atomic habits"
   }
print("\n\nmaking a query: ")
# now add it to the books.find()
print([*books.find(query)])