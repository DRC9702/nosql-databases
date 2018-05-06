import pymongo
from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
client.drop_database("final_proj")
print(client.database_names())
database = client.final_proj

# Adding 3 users
user_collection = database.users
users = [None] * 3
users[0] = {"user_id": 1,
	"create_date": "01/01/2018",
	"karma": 107,
	"about": "Studies nosql at Columbia",
	"submissions": [1,2,3,4,5],
	"comments": [1,3],
	"favorites": [1,6,11],
	"credentials": {"username": "david", "password": "david1"}}
users[1] = {"user_id": 2,
	"create_date": "01/02/2018",
	"karma": 23,
	"about": "Also in the nosql class",
	"submissions": [6,7,8,9,10],
	"comments": [2,4],
	"favorites": [2,7,12],
	"credentials": {"username": "victor", "password": "victor2"}}
users[2] = {"user_id": 3,
	"create_date": "01/03/2018",
	"karma": 67,
	"about": "3rd person in nosql class",
	"submissions": [11,12,13,14,15],
	"comments": [5],
	"favorites": [3,8,13],
	"credentials": {"username": "lalka", "password": "lalka3"}}

for i in range(3):
	user_collection.insert(users[i])

#Viewing Users
print("USERS:")
cursor = user_collection.find({})
print(cursor.count())
for document in cursor:
	print(document)

# Adding Articles
article_collection = database.articles
articles = [None] * 15
articles[0] = {"article_id": 1,
	"title": {"text": "	California to become first U.S. state mandating solar on new homes",
		"url": "https://www.ocregister.com/2018/05/04/california-to-become-first-u-s-state-mandating-solar-on-new-homes/",
		"domain": "ocregister.com"},
	"author": 1,
	"comments": [],
	"stats": {"points": 54,
		"time": "02/01/2018:12:01:01"}}

articles[1] = {"article_id": 2,
	"title": {"text": "Subscription Hell",
		"url": "https://techcrunch.com/2018/05/06/subscription-hell/",
		"domain": "techcrunch.com"},
	"author": 1,
	"comments": [],
	"stats": {"points": 213,
		"time": "02/01/2018:12:02:01"}}

articles[2] = {"article_id": 3,
	"title": {"text": "Gitea: Open source, self-hosted GitHub alternative",
		"url": "https://gitea.io/en-US/",
		"domain": "gitea.io"},
	"author": 1,
	"comments": [],
	"stats": {"points": 303,
		"time": "02/01/2018:12:03:01"}}

articles[3] = {"article_id": 4,
	"title": {"text": "Researchers have developed a water-based battery to store solar and wind energy",
		"url": "https://news.stanford.edu/2018/04/30/new-water-based-battery-offers-large-scale-energy-storage/",
		"domain": "stanford.edu"},
	"author": 1,
	"comments": [],
	"stats": {"points": 64,
		"time": "02/01/2018:12:04:01"}}

articles[4] = {"article_id": 5,
	"title": {"text": "Show HN: Refjar.com – bookmark links and fetch online discussions",
		"url": "https://refjar.com",
		"domain": "refjar.com"},
	"author": 1,
	"comments": [],
	"stats": {"points": 28,
		"time": "02/01/2018:12:05:01"}}

articles[5] = {"article_id": 6,
	"title": {"text": "NASA advisers say SpaceX rocket technology could put lives at risk",
		"url": "http://www.chicagotribune.com/news/nationworld/ct-nasa-spacex-rocket-elon-musk-20180505-story.html",
		"domain": "chicagotribune.com"},
	"author": 2,
	"comments": [],
	"stats": {"points": 68,
		"time": "02/01/2018:12:06:01"}}

articles[6] = {"article_id": 7,
	"title": {"text": "Sidepact: start a company with a full-time job",
		"url": "https://www.sidepact.com/",
		"domain": "sidepact.com"},
	"author": 2,
	"comments": [],
	"stats": {"points": 36,
		"time": "02/01/2018:12:07:01"}}

articles[7] = {"article_id": 8,
	"title": {"text": "Origins of the finger command (1990)",
		"url": "https://groups.google.com/forum/#!msg/alt.folklore.computers/IdFAN6HPw3k/Ci5BfN8i26AJ",
		"domain": "groups.google.com"},
	"author": 2,
	"comments": [],
	"stats": {"points": 98,
		"time": "02/01/2018:12:08:01"}}

articles[8] = {"article_id": 9,
	"title": {"text": "Cells Talk in a Language That Looks Like Viruses",
		"url": "https://www.quantamagazine.org/cells-talk-in-a-language-that-looks-like-viruses-20180502/",
		"domain": "quantamagazine.org"},
	"author": 2,
	"comments": [],
	"stats": {"points": 158,
		"time": "02/01/2018:12:09:01"}}

articles[9] = {"article_id": 10,
	"title": {"text": "A woman’s brain stimulator stopped working after her home struck by lightning",
		"url": "https://www.nytimes.com/2018/05/03/health/lightning-brain-implants.html",
		"domain": "nytimes.com"},
	"author": 2,
	"comments": [],
	"stats": {"points": 32,
		"time": "02/01/2018:12:10:01"}}

articles[10] = {"article_id": 11,
	"title": {"text": "Java’s Mysterious Interrupt",
		"url": "https://carlmastrangelo.com/blog/javas-mysterious-interrupt",
		"domain": "carlmastrangelo.com"},
	"author": 3,
	"comments": [],
	"stats": {"points": 76,
		"time": "02/01/2018:12:11:01"}}

articles[11] = {"article_id": 12,
	"title": {"text": "How Harvey Karp Turned Baby Sleep into Big Business",
		"url": "https://www.nytimes.com/2018/04/18/magazine/harvey-karp-baby-mogul.html",
		"domain": "nytimes.com"},
	"author": 3,
	"comments": [],
	"stats": {"points": 66,
		"time": "02/01/2018:12:12:01"}}

articles[12] = {"article_id": 13,
	"title": {"text": "The Micronesian island of Yap has stone money too heavy to move",
		"url": "http://www.bbc.com/travel/story/20180502-the-tiny-island-with-human-sized-money",
		"domain": "bbc.com"},
	"author": 3,
	"comments": [],
	"stats": {"points": 28,
		"time": "02/01/2018:12:13:01"}}

articles[13] = {"article_id": 14,
	"title": {"text": "How I got my first thousand users",
		"url": "https://www.indiehackers.com/@RickVanHaasteren/how-i-got-my-first-1000-users-47d06edc3d",
		"domain": "indiehackers.com"},
	"author": 3,
	"comments": [],
	"stats": {"points": 21,
		"time": "02/01/2018:12:14:01"}}

articles[14] = {"article_id": 15,
	"title": {"text": "How I got my first thousand users",
		"url": "https://www.wsj.com/articles/unlocking-the-business-secrets-of-escape-rooms-1524838226",
		"domain": "wsj.com"},
	"author": 3,
	"comments": [],
	"stats": {"points": 21,
		"time": "02/01/2018:12:15:01"}}

for i in range(15):
	article_collection.insert(articles[i])

#Viewing Articles
print("ARTICLES:")
cursor = article_collection.find({})
print(cursor.count())
for document in cursor:
	print(document)

# Adding 5 comments
comments_collection = database.comments
comments = [None] * 5

comments[0] = {"comment_id": 1,
	"author": 1,
	"comments": [2],
	"text": "Wow! That's a good idea",
	"time": "02/02/2018:12:00:01"}

comments[1] = {"comment_id": 2,
	"author": 2,
	"comments": [5],
	"text": "No, it's not",
	"time": "02/02/2018:12:00:02"}

comments[2] = {"comment_id": 3,
	"author": 1,
	"comments": [4],
	"text": "I like this",
	"time": "02/02/2018:12:00:03"}

comments[3] = {"comment_id": 4,
	"author": 2,
	"comments": [],
	"text": "That is an insightful comment",
	"time": "02/02/2018:12:00:04"}

comments[4] = {"comment_id": 5,
	"author": 3,
	"comments": [],
	"text": "Yeah, it's not a good idea",
	"time": "02/02/2018:12:00:05"}

for i in range(5):
	comments_collection.insert(comments[i])

#Viewing Comments
print("COMMENTS:")
cursor = comments_collection.find({})
print(cursor.count())
for document in cursor:
	print(document)

# Adding 2 jobs
jobs_collection = database.jobs
jobs = [None] * 2

jobs[0] = {"job_id": 1,
	"title": {"text": "The Muse Is Hiring a PM for Data and Analytics",
		"url": "https://www.themuse.com/jobs/themuse/product-manager-data-analytics-8fa79a",
		"domain": "themuse.com"},
	"about": "02/03/2018:12:00:01"}

jobs[1] = {"job_id": 2,
	"title": {"text": "VoiceOps is hiring in SF to build AI for B2B voice data",
		"url": "https://voiceops.com/careers.html",
		"domain": "voiceops.com"},
	"about": "02/03/2018:12:00:02"}

for i in range(2):
	jobs_collection.insert(jobs[i])

#Viewing Comments
print("JOBS:")
cursor = jobs_collection.find({})
print(cursor.count())
for document in cursor:
	print(document)

#Creating the boards
# Adding 2 jobs
board_collection = database.boards

news = {"board_id": 1,
	"name": "news",
	"articles": list(range(1,16)),
	"jobs": []}

jobs = {"board_id": 2,
	"name": "jobs",
	"articles": [],
	"jobs": [1,2]}

board_collection.insert(news)
board_collection.insert(jobs)

#Viewing Comments
print("BOARDS:")
cursor = board_collection.find({})
print(cursor.count())
for document in cursor:
	print(document)