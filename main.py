from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import Screen, ScreenManager

from notification_rl import NotificationRL
from barcode import Barcode
from tdl import TDL


class WelcomeScreen(Screen):
    pass


class FirstScreen(Screen):
    pass


class ScreenManager(ScreenManager):
    pass


class TDLIdentifierScreen(Screen):
    child_id = StringProperty()
    _tdl = None

    def generateFilledTdl(self):
        self.child_id = self.ids.child_id.text
        if self.child_id != "":
            print(self.child_id)
            self._tdl = TDL(self.child_id)
            self.ids.child_name.text = self._tdl.sponsorship.getChild().getFirstName()
            self.ids.donor_id.text = self._tdl.sponsorship.getDonor().getId()
            self.ids.donor_name.text = self._tdl.sponsorship.getDonor().getFirstName()
        else:
            print("Empty Id")
    def displayPDF(self):
        if self._tdl:
            self._tdl.generatePageAll()


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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    notifikasi = NotificationRL()
    notifikasi.show()

    CorrManagerApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
