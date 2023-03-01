import pymongo
from backpack_tf2.app.config import MONGODB_IP, MONGODB_PORT, MONGO_DB_NAME


db_connect = pymongo.MongoClient(MONGODB_IP, MONGODB_PORT)

db = db_connect[MONGO_DB_NAME]
