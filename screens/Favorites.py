from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from .Star import Star

favorite_ideas = ["Idea 1","Idea 2", "Idea 3","Idea 1","Idea 2", "Idea 3"]
class Favorites(Screen):
    def update(self, list_id):
        for idea in favorite_ideas:
            t = Label(text = idea, font_size = 20,size_hint_x= 0.8)
            s = Star(size_hint_x = 0.1)
            box = BoxLayout()
            box.add_widget(t)
            box.add_widget(s)
            list_id.add_widget(box)
        