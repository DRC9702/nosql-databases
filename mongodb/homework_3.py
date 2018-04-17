import pymongo
from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
database = client.movies
collection = database.movies
woop = collection.find({}).count()

# A. Find movies with rating: 'NOT RATED' and update to "Pending rating"
print("PART A")
cursor = collection.find({"rated": "NOT RATED"})
#print(cursor.count())
for document in cursor:
	collection.update({"_id":document["_id"]},{"rated": "Pending rating"})
print("\t ...All 'not rated' ratings updated to 'pending rating'")
#print(cursor.count())

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


#D. Use aggregation to find number of movies made in Mexico in 1995 with rated:"Pending rating"
print("PART D")
pipeline = [	{"$match": {"year": 1995}},
		{"$unwind": "$countries"},
		{"$group": {"_id": {"countries": "Mexico", "rated": "Pending rating"}, "count": {"$sum": 1}}}]
#		{"$group": {"_id": {"countries": "Mexico", "year": "1995"}, "count": {"$sum": 1}}}]

agg = collection.aggregate(pipeline)
pprint(list(agg))

#E. Use $lookup operator
