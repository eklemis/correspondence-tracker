from docutils.nodes import Root
from kivy.app import App
from kivy.factory import Factory
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
import os

from notification_rl import NotificationRL

from barcode import Barcode
from tdl import TDL


class WelcomeScreen(Screen):
    pass


class FirstScreen(Screen):
    pass


class ScreenManager(ScreenManager):
    pass


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class TDLIdentifierScreen(Screen):
    child_id = StringProperty()
    _tdl = None

    def generateFilledTdl(self):
        self.child_id = self.ids.child_id.text
        loadfile = ObjectProperty(None)
        savefile = ObjectProperty(None)
        text_input = ObjectProperty(None)

        if self.child_id != "":
            print(self.child_id)
            self._tdl = TDL(self.child_id)
            self.ids.child_name.text = self._tdl.sponsorship.getChild().getFirstName()
            self.ids.donor_id.text = self._tdl.sponsorship.getDonor().getId()
            self.ids.donor_name.text = self._tdl.sponsorship.getDonor().getTitleFirstName()
        else:
            print("Empty Id")
    def displayPDF(self):
        if self._tdl:
            self._tdl.generatePageAll()
    def getSelectedFile(self, *args):
        selectedFile = args[1][0]
        print(selectedFile)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()

    def _fbrowser_canceled(self, instance):
        print ('cancelled, Close self.')

    def _fbrowser_success(self, instance):
        print (instance.selection)

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

Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #notifikasi = NotificationRL()
    #notifikasi.show()

    CorrManagerApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
