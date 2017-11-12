import pymongo

from menu import Menu
from models.blog import Blog
from database import Database
from models.post import Post

__author__ = "codeninja55"

Database.initialize()

menu = Menu()
menu.run_menu()
