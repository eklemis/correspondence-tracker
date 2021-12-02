import pathlib

import openpyxl
from fpdf import FPDF
import os

from sponsorship import Sponsorship

class Labels():
    def __init__(self):
        self.formatedSponsorships = []
    def addLabel(self, of_child_id):
        row = Sponsorship(of_child_id)
        if row.getDonor().getCountry() == "USA":
            formatedRow = {
                "childId": row.getChild().getChildId(),
                "childName": row.getChild().getFullName(),
                "donorId": row.getDonor().getId(),
                "donorName": row.getDonor().getTitleFirstName(),
                "childStatus": row.getChild().getStatus(),
                "donorDCE": row.getDonor().getDCE(),
                "donorEnvLineOne": row.getDonor().getEnvLineOne(),
                "donorAddress": row.getDonor().getAddressLineOne(),
                "donorCityStateProv": row.getDonor().getCity() + " " + row.getDonor().getStateProv(),
                "donorPostalCode": row.getDonor().getPostalCode(),
                "donorCountry": row.getDonor().getCountry(),
                "includedThis": True
            }
            self.formatedSponsorships.append(formatedRow)

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
        return self.formatedSponsorships

    def produceAFourLandscapePage(self):
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        count = 1
        from label_page_setting import font_source, font, font_size, aFourPage

        x = aFourPage["xStart"]
        y = aFourPage["yStart"]
        w = aFourPage["labelWidth"]
        h = aFourPage["labelHeight"]
        boxSpace = aFourPage["boxSpace"]
        labelPerRow = aFourPage["labelPerRow"]

        col_counter = 0
        for row in self.formatedSponsorships:
            col_counter += 1
            if (count == 1) or (count % 17 == 0):
                #reinitialize x, y, col_counter
                x = aFourPage["xStart"]
                y = aFourPage["yStart"]

                #Page setup
                pdf.add_page()
                #set font based on platform
                import platform
                if platform.system() == "Darwin":
                    pdf.set_font("Helvetica", "B", font_size)
                elif platform.system() == "Windows":
                    pdf.add_font(font, "", font_source, uni=True)
                    pdf.set_font(font, "", font_size)

            #Orginizing items on created page
            #Draw box
            pdf.rect(x, y, w, h)

            #Displaying Items in label box
            strX = x + aFourPage["boxPadding"]

            strY = y + aFourPage["boxPadding"] + aFourPage["lineHeight"]
            pdf.text(strX, strY, str(row["donorDCE"]))

            strY += aFourPage["lineHeight"] + aFourPage["boxPadding"]
            pdf.text(strX, strY, str(row["donorEnvLineOne"]))

            strY += aFourPage["lineHeight"] + aFourPage["boxPadding"]
            pdf.text(strX, strY, str(row["donorAddress"]))
            if str(row["donorCityStateProv"]).strip() != "":
                strY += aFourPage["lineHeight"] + aFourPage["boxPadding"]
                pdf.text(strX, strY, str(row["donorCityStateProv"]))
            if str(row["donorPostalCode"]).strip() != "":
                strY += aFourPage["lineHeight"] + aFourPage["boxPadding"]
                pdf.text(strX, strY, str(row["donorPostalCode"]))

            strY += aFourPage["lineHeight"] + aFourPage["boxPadding"]
            pdf.text(strX, strY, str(row["donorCountry"]))

            x += w + boxSpace
            # move to new row when current column reach labelPerRow limit
            if col_counter == labelPerRow:
                x = aFourPage["xStart"]
                y += h + boxSpace
                col_counter = 0
            count += 1
        pdf.output(f'Labels_from_file.pdf', "F")
        _path = os.path.join(os.getcwd(),"Labels_from_file.pdf")
        print(f"File created: {_path}")
        import webbrowser
        import threading
        t = threading.Thread(target=webbrowser.open, args=(r'file:///'+_path, ))
        t.start()

    def produceOtherSizePage(self):
        pass