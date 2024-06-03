from contents import DEFAULT_CONTENT, Content
from contexts import Context, UnkownUserContext
import pickle


class Application:

    def __init__(self) -> None:
        self.context = UnkownUserContext()
        self.exited = False
        self.content = None

    def get_contex(self) -> Context:
        return self.context
    
    def set_context(self, ctx : Context):
        self.context = ctx

    def get_content(self) -> Content:
        if self.content != None:
            return self.content
        try:
            with open("./db.txt", "rb") as file:
                self.content = pickle.load(file)
        except Exception:
            self.content = DEFAULT_CONTENT
        return self.content
    
    def save_content(self):
        with open("./db.txt","wb") as file:
            pickle.dump(self.content, file)
