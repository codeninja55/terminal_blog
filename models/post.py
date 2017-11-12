import datetime
import uuid
from database import Database

__author__ = "codeninja55"


class Post(object):

    def __init__(self, blog_id, title, content,
                 author="codeninja55", date=datetime.datetime.utcnow(), post_id=None):  # note: parameter=DefaultValue
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.post_id = uuid.uuid4().hex if id is None else post_id
        self.created_date = date

    def save_to_database(self):
        Database.insert(collection='posts', data=self.post_JSON())

    def post_JSON(self):
        return {
            'post_id': self.post_id,
            'blog_id': self.blog_id,
            'author': self.author,
            'title': self.title,
            'content': self.content,
            'created_date': self.created_date
        }

    @classmethod
    def from_database(cls, post_id):
        post_data = Database.find_one(collection='posts', query={'post_id': post_id})
        return cls(blog_id=post_data['blog_id'], title=post_data['title'],
                   content=post_data['content'], author=post_data['author'],
                   date=post_data['date'], post_id=post_data['post_id'])

    @staticmethod
    def from_blog(blog_id):
        return [post for post in Database.find(collection='posts', query={'blog_id': blog_id})]
