import openpyxl
from fpdf import FPDF
import os
from sponsorship import Sponsorship

class Labels():
    def __init__(self):
        self.__all_labels = []
    def addLabel(self, of_child_id):
        self.__all_labels.append(Sponsorship(of_child_id))

    def removeLabel(self, of_chil_id):
        pass

    '''
    Below are all function needed to load child id(s) from excel file
    '''
    def __getChilIdColRowPosition(self, sheet):
        found_row = None
        found_col = None
        col_start = 'A'
        col_limit = 'Q'
        row_start = 1
        row_limit = 20
        found = False
        curr_row = row_start
        while not found and curr_row<=row_limit:
            #go trough rows
            curr_col = col_start
            while not found and curr_col<col_limit:
                value_to_check = sheet[f'{curr_col}{curr_row}'].value
                found = str(value_to_check).startswith("113")

                if found:
                    found_col = curr_col
                    found_row = curr_row
                    break
                #go trough column
                curr_col = chr(ord(curr_col)+1)

            curr_row += 1
        return found_col, found_row
    def __pullIdFromsheet(self, sheet, start_row, selected_col):
        curr_row = start_row
        col = selected_col

        while str(sheet[f'{col}{curr_row}'].value) != '' and str(sheet[f'{col}{curr_row}'].value).startswith("113"):
            value = str(sheet[f'{col}{curr_row}'].value)
            if value.startswith("113"):
                self.addLabel(value)
            curr_row += 1
        print("Pull ids from excel done!");

    def labelFromExcelFile(self, path):
        workbook = openpyxl.load_workbook(path)

        sheet = workbook.active

        start_col, start_row = self.__getChilIdColRowPosition(sheet)

        is_contain_id = start_col != None and start_row != None

        if is_contain_id:
            self.__pullIdFromsheet(sheet, start_row, start_col)
            return True
        else:
            return False

    def getFormattedData(self):
        selectedSponsorships = []
        for row in self.__all_labels:
            formatedRow = {
                "childId": row.getChild().getChildId(),
                "childName": row.getChild().getFullName(),
                "donorId": row.getDonor().getId(),
                "donorName": row.getDonor().getTitleFirstName(),
                "childStatus": row.getChild().getStatus()
            }
            selectedSponsorships.append(formatedRow)

        return selectedSponsorships
