import pymongo
from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
print(client.database_names())
database = client.movies
print(database.collection_names())
collection = database.movies
print(collection)
woop = collection.find({}).count()
print(woop)
# Find movies with rating: 'NOT RATED' and update to "Pending rating"
cursor = collection.find({"rated": "NOT RATED"})
print(cursor.count())
for document in cursor:
	collection.update({"_id":document["_id"]},{"rated": "Pending rating"})
print(cursor.count())


