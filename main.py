from kivy.app import App
from kivy.uix.floatlayout import FloatLayout 
from kivy.lang import Builder
from screens.MainScreen import MainScreen
from screens.Favorites import Favorites
from screens.History import History
from AppManager import AppManager
from screens.Star import Star

Builder.load_file("screens/utils.kv") # Some stylized widgets for better looking UI
Builder.load_file("screens/mainscreen.kv") # Main Screen obvious, it's in charge of changing ideas
Builder.load_file("appmanager.kv") # It's function is to change screens
Builder.load_file("screens/favorites.kv")
Builder.load_file("screens/star.kv")
Builder.load_file("screens/history.kv")
class IdealChooserApp(App):
    def build(self):
        
        return MainScreen()

    

if __name__ == "__main__":
    IdealChooserApp().run()
     