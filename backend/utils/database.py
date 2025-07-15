from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_db():
    """
    Establishes a connection to the MongoDB database and returns the database object.

    Returns:
        MongoClient: A connection to the MongoDB database.
    """
    # Retrieve the MongoDB connection string from environment variables
    mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')

    # Connect to the MongoDB server
    client = MongoClient(mongo_uri)

    # Access the specific database
    db = client.get_database('dataset_catalog')

    return db
