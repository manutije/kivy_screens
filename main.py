from logging import root
from re import A, S
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty
import databse


class Screen_three(Screen):
    namer= StringProperty("Hi Stranger")
    def update(self,name):
        self.namer = ("Welcome: "+name)



class Screen_four(Screen):
    validation = False
    username_l = StringProperty("Hello")
    def login_user(self, name, password):
        validation = databse.login_usr(name.text, password.text)
        self.username_l = name.text
        name.text = ""
        password.text =""
        self.parent.ids.three.update(self.username_l)
        if validation:
            self.parent.current = "three"
            self.parent.transition.direction = 'down'
            
        else:
            self.parent.current = "one"
            self.parent.transition.direction = 'up'
    

    

class Screen_two(Screen):

    def register_user(self,name,password,mail):
        databse.create_usr(name.text,password.text,mail.text)
        print("Uploaded to the database")

class Sm(ScreenManager):
    pass

class ScreensApp(App):
    pass

ScreensApp().run()