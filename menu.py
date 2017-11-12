from database import Database
from models.blog import Blog

__author__ = "codeninja55"


class Menu(object):
    def __init__(self):
        self.user = input("Enter your author name: ")
        self.user_blog = None
        # _ before method name is a convention for private methods
        if self._user_has_account():
            print("Welcome back {user}".format(user=self.user))
        else:
            self._prompt_user_for_account()

    def run_menu(self):
        # User read or write blog?
        read_or_write = input("Do you want to read (R) or write (W) blogs? (Default=R): ")
        if read_or_write == 'R' or read_or_write == "":
            self._list_posts()
            self._view_post()
        elif read_or_write == 'W':
            self._prompt_write_post()
        else:
            print("Thank you for blogging!")

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.get_from_database(blog_id=blog['blog_id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.user, title=title, description=description)
        blog.save_to_database()
        self.user_blog = blog

    def _prompt_write_post(self):
        self.user_blog.new_post()

    def _list_posts(self):
        counter = 1
        blogs = Database.find(collection='blogs', query={})

        for blog in blogs:
            print("[{counter}] -> ID: {blog_id} | Author: {author} | Title: {title}\n"
                  .format(counter=counter, blog_id=blog['blog_id'], author=blog['author'], title=blog['title']))
            counter = counter + 1

    def _view_post(self):
        blog_to_view = input("Enter the ID of the blog posts to read: ")
        blog = Blog.get_from_database(blog_to_view)
        posts = blog.get_posts()

        for post in posts:
            print("Date: {date}\nTitle: {title}\n\n{content}"
                  .format(date=post['created_date'], title=post['title'], content=post['content']))
