# from bson import json_util

# def jsonSerialize(data):
#     json_string = json_util.dumps(data) # This will not raise an error
#     data = json_util.loads(json_string)
#     return data

class CustomError(Exception):
    def __init__(self, message):
        self.message = message