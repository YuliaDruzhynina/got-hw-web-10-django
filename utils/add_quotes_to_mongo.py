import json
from bson.objectid import ObjectId
from pymongo import MongoClient
#from pymongo.server_api import ServerApi
#import certifi


# Local MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client.hw

# mongo_uri = "mongodb+srv://goitlearn:Goit2023@cluster0.p3tvwqy.mongodb.net?ssl=true&ssl_cert_reqs=CERT_NONE"
# client = MongoClient(mongo_uri, tlsCAFile=certifi.where())


print('Loading quotes to mongo...')
with open ('utils/quotes-09.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })    

print('Quotes loaded!')
