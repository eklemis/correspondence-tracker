from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
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
        self.ui.stackedWidget.setCurrentIndex(0)

        '''
        ### Below are all variabels and functions needed to make pageGenerateTDL page work!
        '''
        from label_generator import Labels
        self.labels = Labels()
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
        self.ui.allChildIds.setColumnWidth(5, 80)
        self.ui.allChildIds.setColumnWidth(6, 230)


        #open file dialog when button load click
        self.ui.loadExcelBtn.clicked.connect(self.openExcelChildIds)

        #generate label on A4 pdf page when printToPdfBtn clicked
        self.ui.printToPdfBtn.clicked.connect(self.generateLabelToAFourPage)

        '''
        ### End of all variabels and functions setup for pageGenerateTDL page!
        '''

        self.show()

    def openExcelChildIds(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '/Users/ek_solution', "Excel file (*.xlsx *.xls)")
        fPath = Path(fname[0])

        is_correct_file = self.labels.labelFromExcelFile(fPath)

        if not is_correct_file:
            message = "The file you selected contain no child id!"
            QMessageBox.about(self, "Info", message)
        else:
            selectedSponsorships = self.labels.getFormattedData()

            self.displayLabelsInTable(selectedSponsorships)


    def displayLabelsInTable(self, vSelectedSponsorships):
        row = 0

        for sponsorhip in vSelectedSponsorships:
            if sponsorhip["includedThis"]:
                self.ui.allChildIds.setRowCount(row + 1)
                self.ui.allChildIds.setItem(row, 1, QtWidgets.QTableWidgetItem(sponsorhip["childId"]))
                self.ui.allChildIds.setItem(row, 2, QtWidgets.QTableWidgetItem(sponsorhip["childName"]))
                self.ui.allChildIds.setItem(row, 3, QtWidgets.QTableWidgetItem(sponsorhip["donorId"]))
                self.ui.allChildIds.setItem(row, 4, QtWidgets.QTableWidgetItem(sponsorhip["donorName"]))
                self.ui.allChildIds.setItem(row, 5, QtWidgets.QTableWidgetItem(sponsorhip["donorCountry"]))
                self.ui.allChildIds.setItem(row, 6, QtWidgets.QTableWidgetItem(sponsorhip["childStatus"]))
                checkBoxItem = QtWidgets.QTableWidgetItem("Item")
                checkBoxItem.setCheckState(Qt.Unchecked)

                self.ui.allChildIds.setItem(row, 0, checkBoxItem)
                row += 1
    def generateLabelToAFourPage(self):
        self.labels.produceAFourLandscapePage()



app = QApplication(sys.argv)

window = UI()
app.exec_()