import datetime
import uuid

from database import Database
from models.post import Post

__author__ = "codeninja55"


class Blog(object):
    def __init__(self, author, title, description, blog_id=None):
        self.author = author
        self.title = title
        self.description = description
        self.blog_id = uuid.uuid4().hex if blog_id is None else blog_id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date_str = input("Enter post date, or leave blank for today (DDMMYYYY)")
        date = datetime.datetime.utcnow() if not date_str else datetime.datetime.strptime(date_str, "%d%m%Y")

        post = Post(blog_id=self.blog_id, title=title, content=content,
                    author=self.author, date=date)
        post.save_to_database()

    def get_posts(self):
        return Post.from_blog(self.blog_id)

    def save_to_database(self):
        Database.insert(collection='blogs', data=self.blog_JSON())

    def blog_JSON(self):
        return {'author': self.author,
                'title': self.title,
                'description': self.description,
                'blog_id': self.blog_id
                }

    @classmethod
    def get_from_database(cls, blog_id):
        blog_data = Database.find_one(collection='blogs', query={'blog_id': blog_id})

        return cls(author=blog_data['author'], title=blog_data['title'],
                   description=blog_data['description'], blog_id=blog_data['blog_id'])
