from actions import list_book, register, login, account, search_books, exit, add_book
from typing import TYPE_CHECKING, Callable

from utils import ADMIN_PRIORITY


if TYPE_CHECKING:
    from contents import User

class Context:
    def getArgs(self) -> dict[str, (Callable)]:
        raise NotImplemented()
    
class UnkownUserContext(Context):
    def getArgs(self):
        return {"Cadastar-se": register, "Entrar": login, "Sair": exit}
    
class kownUserContext(Context):
    def __init__(self, logged_user : 'User') -> None:
        super().__init__()
        self.logged_user = logged_user

    def getArgs(self):
        result =  {"Sair": exit, "Conta": account, "Livros": list_book, "Pesquisar": search_books}

        if self.logged_user.priority == ADMIN_PRIORITY:
            result["Adcionar Livro"] = add_book

        return result