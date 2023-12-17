from pymongo import MongoClient


# MongoDB connection URI.
uri = "mongodb+srv://admin:root@cluster0.sqz0be3.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)


# Select the 'blog_db' database from the MongoDB client.
db = client.blog_db


# Collections in the 'blog_db' database.
blog_posts_collection = db["blog_posts"]
users_collection = db["users"]
comments_collection = db["blog_comments"]
tags_collection = db["blog_tags"]



# Secret key and algorithm for JWT token generation.
SECRET_KEY = "TechActive@123"
ALGORITHM = "HS256"