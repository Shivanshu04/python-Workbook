import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database called "social_media"
db = client["social_media"]

# Create a collection called "twitter_data"
collection = db["twitter_data"]
