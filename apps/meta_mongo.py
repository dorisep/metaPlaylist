import pymongo

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

print('hello world')