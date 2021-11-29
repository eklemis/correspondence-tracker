from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.ui = uic.loadUi("main_app.ui", self)
        pixmap = QPixmap('ui_res/images/SC-Child-White.png')
        self.ui.Logo.setPixmap(pixmap)
        self.ui.Logo.repaint()

        #Connect filledTdlButton to display pageGenerateTDL page
        self.ui.filledTdlButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageGenerateTDL))

        #connect generateLabelButton to display pageGenerateLabel page
        self.ui.generateLabelButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageGenerateLabel))

        self.show()

app = QApplication(sys.argv)
window = UI()
app.exec_()