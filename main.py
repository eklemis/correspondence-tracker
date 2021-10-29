from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import Screen, ScreenManager

from notification_rl import NotificationRL
from barcode import Barcode

class WelcomeScreen(Screen):
    pass

class FirstScreen(Screen):
    pass

class ScreenManager(ScreenManager):
    pass

class BarcodeGeneratorForm(GridLayout):
    lastCode = StringProperty()
    _barcode = Barcode()
    lastCode = StringProperty(str(_barcode.getLastId()))

    def generateBarcode(self, num_of_barcode):
        if num_of_barcode == "":
            num_of_barcode = 5
        else:
            num_of_barcode = int(num_of_barcode)

        self._barcode.generateBarcode(num_of_barcode)
        self.lastCode = str(self._barcode.getLastId())

class BarcodesPage(GridLayout):
    pass

class MainFront(GridLayout):
    pass

class CorrManagerApp(App):
    title = 'Sponsorship Correspondence Manager'
    def build(self):
        self._barcode = Barcode()
        self.mainFront = MainFront()
        return self.mainFront

    def generateBarcode(self, num_of_barcode):
        if num_of_barcode == "":
            num_of_barcode = 5
        else:
            num_of_barcode = int(num_of_barcode)

        self._barcode.generateBarcode(num_of_barcode)
        self.mainFront.ids.last_code = str(self._barcode.getLastId())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    notifikasi = NotificationRL()
    notifikasi.show()

    CorrManagerApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
