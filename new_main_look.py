from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic, QtWidgets
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.ui = uic.loadUi("main_app.ui", self)
        pixmap = QPixmap('ui_res/images/SC-Child-White.png')

        self.ui.Logo.setPixmap(pixmap)
        self.ui.Logo.repaint()
        #set default page
        self.ui.stackedWidget.setCurrentIndex(0);

        #Connect filledTdlButton to display pageGenerateTDL page
        self.ui.filledTdlButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageGenerateTDL))

        #connect generateLabelButton to display pageGenerateLabel page
        self.ui.generateLabelButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageGenerateLabel))

        #Setup table widget that displays all loaded and entered child ids in pageGenerateLabel page
        self.ui.allChildIds.setColumnWidth(0, 30)
        self.ui.allChildIds.setColumnWidth(1, 100)
        self.ui.allChildIds.setColumnWidth(2, 200)
        self.ui.allChildIds.setColumnWidth(3, 100)
        self.ui.allChildIds.setColumnWidth(4, 200)
        self.ui.allChildIds.setColumnWidth(5, 273)

        #open file dialog when button load click
        self.ui.loadExcelBtn.clicked.connect(self.openExcelChildIds)
        self.loadDataForLabels()
        self.show()

    def openExcelChildIds(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '', "Excel file (*.xlsx)")
    def loadDataForLabels(self):
        sponsorships = [
            {"childId":"11301345","childName":"Sample Child Name","donorId":"654545456", "donorName":"Hyu Jeen", "childStatus":"Ineligible - Not Participating"},
            {"childId": "11301346", "childName": "Sample Child Name", "donorId": "654545456", "donorName": "Hyu Jeen",
             "childStatus": "Eligible"},
            {"childId": "11301347", "childName": "Sample Child Name", "donorId": "654545456", "donorName": "Hyu Jeen",
             "childStatus": "Eligible"},
            {"childId": "11301348", "childName": "Sample Child Name", "donorId": "654545456", "donorName": "Hyu Jeen",
             "childStatus": "Ineligible - Not Participating"}
        ]
        row = 0

        for sponsorhip in sponsorships:
            self.ui.allChildIds.setRowCount(row + 1)
            self.ui.allChildIds.setItem(row, 1, QtWidgets.QTableWidgetItem(sponsorhip["childId"]))
            self.ui.allChildIds.setItem(row, 2, QtWidgets.QTableWidgetItem(sponsorhip["childName"]))
            self.ui.allChildIds.setItem(row, 3, QtWidgets.QTableWidgetItem(sponsorhip["donorId"]))
            self.ui.allChildIds.setItem(row, 4, QtWidgets.QTableWidgetItem(sponsorhip["donorName"]))
            self.ui.allChildIds.setItem(row, 5, QtWidgets.QTableWidgetItem(sponsorhip["childStatus"]))
            checkBoxItem = QtWidgets.QTableWidgetItem("Item")
            if row % 2 == 0:
                checkBoxItem.setCheckState(Qt.Checked)
            else:
                checkBoxItem.setCheckState(Qt.Unchecked)
            self.ui.allChildIds.setItem(row, 0, checkBoxItem)
            row+=1

'''f = QApplication.font('Gill Sans Infant Std');
f.setStyleStrategy(QFont.PreferAntialias);
QApplication.setFont(f);'''
app = QApplication(sys.argv)

window = UI()
app.exec_()