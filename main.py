from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import Screen, ScreenManager

from notification import Notification

class WelcomeScreen(Screen):
    pass

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ScreenManager(ScreenManager):
    pass

class BarcodeGeneratorForm(GridLayout):
    pass
class BarcodesPage(GridLayout):
    pass

class MainFront(GridLayout):
    pass

class CorrManagerApp(App):
    title = 'Sponsorship Correspondence Manager'
    def build(self):
        return MainFront()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    CorrManagerApp().run()
    #notifikasi = Notification("Hi,\nYou have 5 correspondence almost late (3 days left).\nPlease update their status!")
    #notifikasi.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
