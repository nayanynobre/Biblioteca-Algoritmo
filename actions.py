from utils import USER_PRIORITY, ask, ask_int, ask_dict, filter_dict_list_by_value, say_listed
from contents import Book, User
import importlib
import random

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from application import Application

def exit(app : 'Application'):
    app.exited = True

def add_book(app : 'Application'):
    title = ask("Insira o título:")
    description =  ask("Insira a descrição:")
    author = ask("Insira o autor:")

    app.content.books.append(Book(title,description, author, random.randrange(1, 1E10)))
    print("Livro catalogado.")

def register(app : 'Application'):
    user_name = ask("What's your username?")
    password = ask("Insert your password.")
    app.get_content().users.append(User(user_name, password, USER_PRIORITY))

def login(app : 'Application'):
    user_name = ask("What's your username?")
    password = ask("Insert your password.")
    
    found = [x for x in app.get_content().users if x.name == user_name and x.password == password]
    if len(found) != 1:
        print("Password or user wrong. Try again.")
        return
    app.set_context(importlib.import_module("contexts").kownUserContext(found[0] ))
    print("Welcome")

def account(app : 'Application'):
    print("Name: " + app.get_contex().logged_user.name)
    print("Password: " + app.get_contex().logged_user.password)
    pass

def list_book(app : 'Application'):
    page = ask_int("Page number, enter to get first.")
    book_titles =  [ x.title for x in app.get_content().books ]
    for i in range(len(book_titles)):
        idx = page + i % len(book_titles)
        print(f'{idx + 1} - {book_titles[idx]}')
    

def search_books(app : 'Application'):
    filter_by = ask_dict({
        "title:": "title",
        "author:": "author",
        "description:": "description"
    })
    query = ask("Insira sua busca: ")
    results = filter_dict_list_by_value([x.__dict__ for x in app.get_content().books],query,lambda dict: dict[filter_by])
    say_listed([x["title"] for x in results])