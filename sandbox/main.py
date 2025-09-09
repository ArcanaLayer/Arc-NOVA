#nova main.py

from kivy.app import app
from kivy.uix.label import Label

class Nova(app):
    def build(self):
        return Label(text = "Welcome Everyone", font_size = '26dp')
    

if __name__ == "__main__":
    Nova().run()
