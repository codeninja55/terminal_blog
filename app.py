import pymongo
from models.blog import Blog
from database import Database
from models.post import Post

__author__ = "codeninja55"

# This is how to create and connect a MongoDB database
# uri = "mongodb://127.0.0.1:27017"
# client = pymongo.MongoClient(uri)
# database = client["fullstack"]
# collection = database['students']

# How to retrieve collections from a NoSQL database
# students = collection.find({})
# List comprehension to retrieve data objects from a NoSQL database
# student_list = [student for student in students if student['name'] == "Andrew"]

Database.initialize()

blog = Blog(author="codeninja55", title="Sample title", description="Sample description")
cn55_blog_id = "f515e6e226674ed7a27996cd58da32d3"

blog.new_post()
blog.save_to_database()
from_database = Blog.get_from_database(blog_id=blog.blog_id)
print(from_database.get_posts())
