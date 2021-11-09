import openpyxl
from fpdf import FPDF
import os

from correspondence import Correspondence

def __isdownstreamfile(path):
    workbook = openpyxl.load_workbook(path)

    sheet = workbook.active

    if sheet['A1'].value=='New Assignments:':
        return True
    return False

def __getChildIds(path):
    workbook = workbook = openpyxl.load_workbook(path)

    sheet = sheet = workbook.active

    row = 3
    col = "C"
    child_ids = []
    count = 1
    while (sheet[f'{col}{row}'].value != None):
        child_ids.append(sheet[f'{col}{row}'].value)
        row += 1
    #collect child ids from transfer donor children
    
    return child_ids

def generateFromExcel(path):
    if __isdownstreamfile(path):
        print("You select correct file!")
        print("Creating your TDLs ...")
        from tdl_page_setting import start_left, start_top, space_vertical, space_horizontal, font, font_source, font_size

        child_ids = __getChildIds(path)
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        for chil_id in child_ids:
            ##Create First Page
            pdf.add_page()
            pdf.add_font(font, "", font_source, uni=True)
            pdf.set_font(font, "", font_size)

            _corr = Correspondence(chil_id)

            pdf.text(start_left, start_top, f"{_corr.sponsorship.getChild().getFirstName()}")
            pdf.text(start_left + space_horizontal, start_top, _corr.sponsorship.getDonor().getTitleFirstName())
            pdf.text(start_left, start_top + space_vertical, _corr.sponsorship.getChild().getChildId())
            pdf.text(start_left + space_horizontal, start_top + space_vertical, _corr.sponsorship.getDonor().getId())
        # Save Created Page
        pdf.output(f'TDL_FROM_DOWNTSREAM.pdf', "F")

        # Open the created page
        _path = os.getcwd() + f"\\TDL_FROM_DOWNTSREAM.pdf"
        os.system(f'cmd /c {_path}')
        print(f"Finished create your TDLs on{_path}")


