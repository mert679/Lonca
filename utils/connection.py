import json
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError, OperationFailure

def get_mongo_connection(config_file="config.json"):
    """
    Establishes a connection to MongoDB using credentials from a JSON configuration file.
    
    Args:
        config_file (str): Path to the configuration file (default is 'config.json').
        
    Returns:
        tuple: MongoDB database object and collection object.
    """
    try:
        # Load configuration from JSON
        with open(config_file, 'r') as file:
            config = json.load(file)
            username = config.get('username')
            password = config.get('password')
            database_name = config.get('database') 
            collection_name = config.get('collection') 
            
            # Create the connection string
            connection = f"mongodb+srv://{username}:{password}@cluster0.lmwk4.mongodb.net/"
            
            # Attempt to connect to MongoDB
            cluster = MongoClient(connection)
            
            # Verify the connection by pinging the server
            cluster.admin.command('ping')
            
            # Access the database and collection
            db = cluster[database_name]
            collection = db[collection_name]
            
            print("Database connection established successfully.")
            return db, collection

    except FileNotFoundError:
        print(f"Error: {config_file} not found.")
        exit()
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the configuration file.")
        exit()
    except ConnectionFailure:
        print("Error: Could not connect to MongoDB. Check your network or server.")
        exit()
    except ConfigurationError:
        print("Error: Invalid MongoDB configuration. Check the connection string.")
        exit()
    except OperationFailure as e:
        print(f"Error: Authentication failed. {e}")
        exit()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit()
