from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
def get_db():
    """
    Establishes a connection to the MongoDB database and returns the database object.

    Returns:
        MongoClient: A connection to the MongoDB database.
    """
    mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
    client = MongoClient(mongo_uri)
    db = client.get_database('dataset_catalog')
    return db
