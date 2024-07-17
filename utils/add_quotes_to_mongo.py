
import json
from bson.objectid import ObjectId
from pymongo import MongoClient

client=MongoClient("mongodb://localhost") 

db=client.hw
   
print('Loading quotes to mongo...')

with open('utils/quotes-09.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)
    #db.quotes.delete_many({})#lazytest:Очистка коллекции перед вставкой новых данных

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })
    else:
        print(f"Author '{quote['author']}' not found. Skipping quote: {quote['quote']}")

