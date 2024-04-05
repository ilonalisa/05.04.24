from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.image import Image
from kivy.properties import NumericProperty

class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

class GameScreen(Screen):
      points = NumericProperty(0)
      
      def __init__(self, **kw):
        super().__init__(**kw)

class Planet(Image):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print("touch")
        return super().on_touch_down(touch)
    

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget (MenuScreen(name='menu'))
        sm.add_widget (GameScreen(name='game'))
        return sm
    
    
    if platform != 'android':
        Window.size = (500, 800)
        Window.left = 750
        Window.top = 100
MainApp().run()                          
