
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.ui = uic.loadUi("main_app.ui", self)

        '''
        ### General Application Setups
        '''
        pixmap = QPixmap('ui_res/images/SC-Child-White.png')
        avatarPix = QPixmap('ui_res/images/woman.png')
        self.ui.avatar.setPixmap(avatarPix)
        self.ui.setWindowIcon(QIcon('ui_res/images/icon.ico'))

        self.ui.Logo.setPixmap(pixmap)
        self.ui.Logo.repaint()
        # set default page
        self.ui.stackedWidget.setCurrentIndex(0)
        '''
        ### End General Application Setups
        '''

        '''
        ### Below are all variables and functions needed to make pageGenerateTDL page work!
        '''
        # Connect filledTdlButton to display pageGenerateTDL page
        self.ui.filledTdlButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageGenerateTDL))
        '''
        ### End of all variables and functions setup for pageGenerateTDL page!
        '''

        '''
        ### Below are all variables and functions needed to make pageGenerateLabel page work!
        '''
        from labelgenerator_view import LabelGeneratorView
        labelGeneratorView = LabelGeneratorView(self.ui)
        '''
        ### End of all variables and functions setup for pageGenerateLabel page!
        '''

        '''
        ### Below are all variables and functions needed to make pageGenerateRL page work!
        '''
        from rlgenerator_view import RlGeneratorView
        rlGeneratorView = RlGeneratorView(self.ui)
        '''
        ### End of all variables and functions setup for pageGenerateRL page!
        '''

        self.show()


app = QApplication(sys.argv)

window = UI()
app.exec_()
