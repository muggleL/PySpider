import pymongo

from code.config import db_host, db_port, db_name, client_name
client = pymongo.MongoClient(host=db_host, port=db_port)
db = client[client_name]
collection = db[db_name]


def save_to_mongo(content):
    data = {
        "user_name": content[0],
        "user_url": content[1],
        "star": content[2],
        "date": content[3],
        "comment": content[4]
    }
    collection.insert_one(data)



