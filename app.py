from utils import clear_screen
import textwrap

class Screen:
    def __init__(self, app):
        self.app = app
   
    def show(self):
        pass
    
    def go(self, screen):
        self.app.goto_screen(screen)
    
    def back(self):
        self.app.go_back()

class App:
    def __init__(self, initial_screen, context = {}):
        self.context = context
        self.__initial_screen = initial_screen
        self.__screen_history__ = [initial_screen]
        
    def run(self):
        while True:
            try:
                clear_screen()
                
                screen = self.__screen_history__[-1](self)
                
                screen.show()
            except KeyboardInterrupt:
                exit()
            except Exception as e:
                clear_screen()

                print(textwrap.dedent(f"""
                ### An Error Occured ###

                {e}
                """))

                input("press any key to continue....")

                self.__screen_history__.insert(0, self.__initial_screen)
                self.__screen_history__ = self.__screen_history__[:1]
    
    def go_back(self):
        if len(self.__screen_history__) == 1:
            return
        
        self.__screen_history__.pop()
    
    def goto_screen(self, screen):
        self.__screen_history__.append(screen)
