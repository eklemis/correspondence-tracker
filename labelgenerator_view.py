from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox


class LabelGeneratorView:
    def __init__(self, mainUI):
        self.ui = mainUI
        from label_generator import Labels
        self.labels = Labels()

        # connect generateLabelButton to display pageGenerateLabel page
        self.ui.generateLabelButton.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageGenerateLabel))

        # Setup table widget that displays all loaded and entered child ids in pageGenerateLabel page
        self.ui.allChildIds.setColumnWidth(0, 30)
        self.ui.allChildIds.setColumnWidth(1, 100)
        self.ui.allChildIds.setColumnWidth(2, 200)
        self.ui.allChildIds.setColumnWidth(3, 100)
        self.ui.allChildIds.setColumnWidth(4, 200)
        self.ui.allChildIds.setColumnWidth(5, 80)
        self.ui.allChildIds.setColumnWidth(6, 230)

        # open file dialog when button load click
        self.ui.loadExcelBtn.clicked.connect(self.openExcelChildIds)

        # generate label on A4 pdf page when printToPdfBtn clicked
        self.ui.printToPdfBtn.clicked.connect(self.generateLabelToAFourPage)
        print(type(self.ui))

    def openExcelChildIds(self):
        fileName = QFileDialog.getOpenFileName(self.ui, 'Open file',
                                               '/Users/ek_solution', "Excel file (*.xlsx *.xls)")
        fPath = Path(fileName[0])

        is_correct_file = self.labels.labelFromExcelFile(fPath)

        if not is_correct_file:
            message = "The file you selected contain no child id!"
            QMessageBox.about(self.ui, "Info", message)
        else:
            selectedSponsorships = self.labels.getFormattedData()

            self.displayLabelsInTable(selectedSponsorships)

    def displayLabelsInTable(self, vSelectedSponsorships):
        row = 0

        for sponsorship in vSelectedSponsorships:
            if sponsorship["includedThis"]:
                self.ui.allChildIds.setRowCount(row + 1)
                self.ui.allChildIds.setItem(row, 1, QtWidgets.QTableWidgetItem(sponsorship["childId"]))
                self.ui.allChildIds.setItem(row, 2, QtWidgets.QTableWidgetItem(sponsorship["childName"]))
                self.ui.allChildIds.setItem(row, 3, QtWidgets.QTableWidgetItem(sponsorship["donorId"]))
                self.ui.allChildIds.setItem(row, 4, QtWidgets.QTableWidgetItem(sponsorship["donorName"]))
                self.ui.allChildIds.setItem(row, 5, QtWidgets.QTableWidgetItem(sponsorship["donorCountry"]))
                self.ui.allChildIds.setItem(row, 6, QtWidgets.QTableWidgetItem(sponsorship["childStatus"]))
                checkBoxItem = QtWidgets.QTableWidgetItem("Item")
                checkBoxItem.setCheckState(Qt.Unchecked)

                self.ui.allChildIds.setItem(row, 0, checkBoxItem)
                row += 1

    def generateLabelToAFourPage(self):
        self.labels.produceAFourLandscapePage()
