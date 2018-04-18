import pymongo
from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
database = client.test
collection = database.movies

# A. Find movies with rating: 'NOT RATED' and update to "Pending rating"
print("PART A")
cursor = collection.find({"rated": "NOT RATED"})
print(cursor.count())
for document in cursor:
	collection.update({"_id":document["_id"]},{"$set": {"rated": "Pending rating"}})
print("\t ...All 'not rated' ratings updated to 'pending rating'")
print(cursor.count())

# B. Insert movie into database - inserting the movie Pandas(2018)
# I had to make up the values for id and votes
print("PART B")
if collection.find({"title": "pandas"}).count()==0:
	doc = {"title": "pandas",
		"year": 2018,
		"countries": ["USA"],
		"genres": ["documentary", "short"],
		"directors": ["David Douglas", "Drew Fellman"],
		"imdb": {'id': 97029702, 'rating': 7.6, 'votes': 9702}} 
	collection.insert(doc)
cursor = collection.find({"title": "pandas"})
for document in cursor:
	pprint(document)

#C. Use aggregation to find total number of genre:short movies
print("Part C")
pipeline = [{"$unwind": "$genres"}, {"$group": {"_id": "short", "count": {"$sum": 1}}}]
agg = collection.aggregate(pipeline)
pprint(list(agg))


#D. Use aggregation to find number of movies made in Mexico with rated:"Pending rating"
print("PART D")
pipeline = [	#
		{"$match": {"countries" : "Mexico", "rated": "Pending rating"}},
		{"$group": {"_id": {"country": "Mexico", "rating": "Pending rating"}, "count": {"$sum": 1}}}]

agg = collection.aggregate(pipeline)
pprint(list(agg))


#E. Use lookup operator
print("PART E")
collection1 = database['inventory']
collection2 = database['pricetable']
if collection1.find({}).count()==0:
	for i,f in enumerate(['apple','peach','banana','mango']):
		doc = {"fruit_id" : i, "name" : f}
		collection1.insert(doc)
if collection2.find({}).count()==0:
	collection2.insert({"fruit": "mango", "price": 2.00})
	collection2.insert({"fruit": "peach", "price": 1.50})

pipeline = [{"$lookup": {"from": "pricetable", "localField": "name", "foreignField": "fruit", "as": "fruitPrices"}},
		{"$match": { "fruitPrices": { "$ne": [] } }}]
agg = collection1.aggregate(pipeline)
pprint(list(agg))

collection1.aggregate

