import pymongo
from pymongo.errors import ConnectionFailure, OperationFailure

def test_mongodb_connection_and_fetch_collections(connection_string: str, database_name: str):
    """
    Tests the MongoDB connection and fetches the collections from the specified database.

    Args:
        connection_string: The MongoDB Atlas connection string.
        database_name: The name of the database to check.
    """
    client = None
    try:
        # Create a connection using MongoClient. The constructor returns immediately
        # and launches the connection process in background threads.
        client = pymongo.MongoClient(connection_string)

        # The ping command is a cheap way to check if the connection is alive and authorized.
        client.admin.command('ping')
        print("Connection to MongoDB Atlas successful!")

        # Access the specified database
        db = client[database_name]

        # Fetch and print the list of collection names in the database
        collections = db.list_collection_names()
        if collections:
            print(f"Collections in database '{database_name}':")
            for collection in collections:
                print(f"- {collection}")
        else:
            print(f"No collections found in database '{database_name}' or the database does not exist.")

    except ConnectionFailure as e:
        print(f"MongoDB connection failed: {e}")
    except OperationFailure as e:
        print(f"Operation failed (e.g., authentication error or invalid database): {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Close the connection
        if client:
            client.close()
            print("MongoDB connection closed.")

# Your MongoDB Atlas connection string with credentials
MONGO_URI = "mongodb+srv://ayanahmadkhan1165_db_user:ayan123@cluster0.metp2qs.mongodb.net/Proj0?retryWrites=true&w=majority"
# The specific database name you want to access
DB_NAME = "Proj0"

# Run the test function
test_mongodb_connection_and_fetch_collections(MONGO_URI, DB_NAME)

from pymongo import MongoClient

uri = "mongodb+srv://ayanahmadkhan1165_db_user:ayan123@cluster0.metp2qs.mongodb.net/Proj0?retryWrites=true&w=majority"
client = MongoClient(uri)

# Access the specific database and collection
db = client["Proj0"]
collection = db["Proj0-Data"]

# 1. Peek at just one document to see the structure
print("--- Single Document Preview ---")
first_doc = collection.find_one()
print(first_doc)

# 2. Fetch and print all documents (limit to 10 for safety)
print("\n--- Listing Documents (Limit 10) ---")
cursor = collection.find().limit(10)
for document in cursor:
    print(document)

client.close()

