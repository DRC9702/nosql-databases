# Put the use case you chose here. Then justify your database choice:
# Hackernews and mongodb. Mongodb allows for rich data models and complex queries which is incredibly useful
# in many of the usecases where you want to query/sort on nested documents. Additionally, the development time
# is typically much shorter because of the query model.
#
# Explain what will happen if coffee is spilled on one of the servers in your cluster, causing it to go down.
# There are two things that prevent data loss. Firstly, member replica sets provide redundancy to the network 
# to make it resilient to system failures. Secondly, when a collection becomes unavailable, a "Submit Queue"
# mechanism flushes captured data to the local harddisk and a background worker process submits the data back
# when the collection becomes available
#
# What data is it not ok to lose in your app? What can you do in your commands to mitigate the risk of lost data?
# User and credential information are the most crucial data that has to be maintained. Actual article and job posting
# is still important but not as much. In order to mitigate the risk of lost data, redundancy can be built into the network
# and the commands should be made automic to prevent incomplete mutations from being made.

import pymongo
from pymongo import MongoClient
from pprint import pprint
from time import gmtime, strftime

client = MongoClient()
print(client.database_names())
database = client.final_proj

# Action 1: A user publishes an article
def publishArticle(database,title,url,domain,user_id):
    #Get new article id
    board_collection = database.boards
    user_collection = database.users
    article_collection = database.articles

    articles_board = board_collection.find_one({"name": "news"})
    user = user_collection.find_one({"user_id": user_id})
    new_art_id = len(articles_board['articles'])+1
    #Get time
    new_time = strftime("%m//%d//%Y:%H:%M:%S", gmtime())
    #Make new article item

    new_article = {"article_id": new_art_id,
	"title": {"text": title,
		"url": url,
		"domain": domain},
	"author": user_id,
	"comments": [],
	"stats": {"points": 0,
		"time": new_time}}

    article_collection.insert(new_article)
    user_collection.update({"user_id":user_id},{"$set": {"submissions": user["submissions"]+[new_art_id]}})
    board_collection.update({"name":"news"},{"$set": {"articles": articles_board["articles"]+[new_art_id]}})

print("ACTION 1")
publishArticle(database,"ARTICLE","URL","DOMAIN",1)

# Action 2: A user publishes a job
def publishJob(database,title,url,domain):
    #Get new article id
    board_collection = database.boards
    job_collection = database.jobs

    job_board = board_collection.find_one({"name": "jobs"})
    new_job_id = len(job_board['jobs'])+1
    #Get time
    new_time = strftime("%m//%d//%Y:%H:%M:%S", gmtime())
    #Make new article item

    new_job = {"job_id": new_job_id,
	"title": {"text": title,
		"url": url,
		"domain": domain}}

    job_collection.insert(new_job)
    board_collection.update({"name":"jobs"},{"$set": {"jobs": job_board["jobs"]+[new_job_id]}})

print("ACTION 2")
publishJob(database,"JOB","URL","DOMAIN")

# Action 3: A user adds a comment to an article
def addCommentToArticle(database,article_id,user_id,text):
    #Ge the user
    user_collection = database.users
    user = user_collection.find_one({"user_id": user_id})

    #Get the article 
    article_collection = database.articles
    article = article_collection.find_one({"article_id": article_id})

    #Get new comment id
    comment_collection = database.comments
    new_comment_id = comment_collection.count({}) + 1

    #Get time
    new_time = strftime("%m//%d//%Y:%H:%M:%S", gmtime())
    #Make new article item

    new_comment = {"comment_id": new_comment_id,
	"author": user_id,
	"comments": [],
	"text": text,
	"time": new_time}

    comment_collection.insert(new_comment)
    article_collection.update({"article_id":article_id},{"$set": {"comments": article["comments"]+[new_comment_id]}})
    user_collection.update({"user_id":user_id},{"$set": {"comments": user["comments"]+[new_comment_id]}})

print("ACTION 3")
addCommentToArticle(database,15,1,"COMMENT")

# Action 4: A user adds a reply comment to another comment
def addCommentToComment(database,old_comment_id,user_id,text):
    #Ge the user
    user_collection = database.users
    user = user_collection.find_one({"user_id": user_id})

    #Get the old comment 
    comment_collection = database.comments
    old_comment = comment_collection.find_one({"comment_id": old_comment_id})

    #Get new comment id
    new_comment_id = comment_collection.count({}) + 1

    #Get time
    new_time = strftime("%m//%d//%Y:%H:%M:%S", gmtime())
    #Make new article item

    new_comment = {"comment_id": new_comment_id,
	"author": user_id,
	"comments": [],
	"text": text,
	"time": new_time}

    comment_collection.insert(new_comment)
    comment_collection.update({"comment_id":old_comment_id},{"$set": {"comments": old_comment["comments"]+[new_comment_id]}})
    user_collection.update({"user_id":user_id},{"$set": {"comments": user["comments"]+[new_comment_id]}})

print("ACTION 4")
addCommentToComment(database,5,1,"COMMENT-REPLY")

# Action 5: Get all articles from a user
def getUserArticles(database,user_id):
    user_collection = database.users
    article_collection = database.articles

    #Get user
    user = user_collection.find_one({"user_id": user_id})
    
    #Get the article ids from that user
    article_id_lst = user["submissions"]

    agg = article_collection.find({"article_id":{"$in":article_id_lst}})
    articles = list(agg)

    return articles

print("ACTION 5")
pprint(getUserArticles(database,1))

# Action 6: Get top 10 articles
def getTop10Articles(database):
    article_collection = database.articles

    #Get user
    # pipeline = [{"$unwind": "$stats"}, {"$max": "$points"}]
    agg = article_collection.find({}).sort("stats.points", -1)
    top10 = list(agg)[:10]
    return top10

print("ACTION 6")
pprint(getTop10Articles(database))

# Action 7: Get user with the most karma
def getTopKarmaUser(database):
    user_collection = database.users

    #Get user
    # pipeline = [{"$unwind": "$stats"}, {"$max": "$points"}]
    agg = user_collection.find({}).sort("karma", -1)
    topUser = list(agg)[0]
    return topUser

print("ACTION 7")
pprint(getTopKarmaUser(database))

# Action 8: Get top 3 most popular articles from a user
def getTop3UserArticles(database,user_id):
    user_collection = database.users
    article_collection = database.articles

    #Get user
    user = user_collection.find_one({"user_id": user_id})
    
    #Get the article ids from that user
    article_id_lst = user["submissions"]

    agg = article_collection.find({"article_id":{"$in":article_id_lst}}).sort("stats.points", -1)
    articles = list(agg)
    top3 = articles[:1]

    return top3

print("ACTION 8")
pprint(getTop3UserArticles(database,1))
