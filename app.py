import pymongo
from models.blog import Blog
from database import Database
from models.post import Post

__author__ = "codeninja55"

Database.initialize()

blog = Blog(author="codeninja55", title="Sample title", description="Sample description")
cn55_blog_id = "f515e6e226674ed7a27996cd58da32d3"

blog.new_post()
blog.save_to_database()
from_database = Blog.get_from_database(blog_id=blog.blog_id)
print(blog.get_posts())
