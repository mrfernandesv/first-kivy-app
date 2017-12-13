import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class FormLayout(StackLayout):
    def print_nome(self,v):
        self.add_widget(Label(text = "Olá " + v, size_hint = (1, .2), font_size = 25))     

class TelaLayout(FloatLayout):
    pass

class OlaApp(App):
    pass

window = OlaApp()
window.run()