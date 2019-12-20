from random import choice
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
ideas = []
try:
    idea_list = open('ideas.txt','r')
    for idea in idea_list.readlines():
        ideas.append(idea)
    idea_list.close()


except():
    print("My Bad, it didnt work ;-;")


class MainScreen(Screen):
    def change_text(self,label, favorite):
        idea = choice(ideas)
        if True:
            label.text = idea
            favorite.state = 'down'
    
    
