

from utils import ADMIN_PRIORITY


class User:

    def __init__(self, name : str, password : str, priority : int) -> None:
        self.name = name
        self.password = password
        self.priority = priority


class Book:
    def __init__(self, title : str, description : str, author : str, id : int) -> None:
        self.title = title
        self.description = description
        self.author = author
        self.id = id

class Content():
    def __init__(self, users: list[User], books : list[Book] ) -> None:
        self.users = users 
        self.books = books

DEFAULT_CONTENT : Content = Content(
    [User("Bruno", "bru123",ADMIN_PRIORITY)],
    [Book("A vida após a morte", "Fala sobre a vida após a morte.", "Pedro", 4642)]
)
