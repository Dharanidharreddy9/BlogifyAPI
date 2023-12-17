from pymongo import MongoClient



uri = "mongodb+srv://admin:root@cluster0.sqz0be3.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

db = client.blog_db


blog_posts_collection = db["blog_posts"]
users_collection = db["users"]
comments_collection = db["blog_comments"]
tags_collection = db["blog_tags"]


SECRET_KEY = "TechActive@123"
ALGORITHM = "HS256"