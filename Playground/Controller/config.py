import pymongo 

url = "mongodb+srv://<username>:<password>16%23@development-local.lbb0lzl.mongodb.net/"
cluster = pymongo.MongoClient(url)

db = cluster["service-providers"]
MongoClient = db["clients-customers"]

TWILIO_ACCOUNT_SID = "Use your SID"
TWILIO_AUTH_TOKEN = "Use your Auth token"