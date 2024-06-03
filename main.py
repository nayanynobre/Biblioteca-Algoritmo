from application import Application
from utils import  ask_dict


    
if __name__ == "__main__":
    app = Application()

    print("Digite o número referente à funcionalidade desejada ou a própria funcionalidade que deseja.")

    while(not app.exited):
        print()
        ask_dict(app.get_contex().getArgs())(app)

    app.save_content()

        
