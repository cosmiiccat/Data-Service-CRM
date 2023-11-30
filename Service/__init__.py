import pymongo 

url = "mongodb+srv://cosmiiccat:Darkerlights16%23@development-local.lbb0lzl.mongodb.net/"
cluster = pymongo.MongoClient(url)

db = cluster["service-providers"]
MongoClient = db["clients-customers"]
