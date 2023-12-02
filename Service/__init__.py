import pymongo 

url = "mongodb+srv://<username><password>@development-local.lbb0lzl.mongodb.net/"
cluster = pymongo.MongoClient(url)

db = cluster["service-providers"]
MongoClient = db["clients-customers"]
