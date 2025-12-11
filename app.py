from utils import clear_screen

class Screen:
    def __init__(self, app):
        self.app = app
   
    def show(self):
        print("Hello World")
    
    def go(self, screen):
        self.app.goto_screen(screen)
    
    def back(self):
        self.app.go_back()

class App:
    def __init__(self, initial_screen, context = {}):
        self.context = context
        self.__screen_history__ = [initial_screen]
        
    def run(self):
        while True:
            clear_screen()
            
            screen = self.__screen_history__[-1](self)
            
            screen.show()
    
    def go_back(self):
        if len(self.__screen_history__) == 1:
            return
        
        self.__screen_history__.pop()
    
    def goto_screen(self, screen):
        self.__screen_history__.append(screen)