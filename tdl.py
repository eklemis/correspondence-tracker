from correspondence import Correspondence
from fpdf import FPDF
import os


class TDL(Correspondence):
    def generatePageAll(self):
        pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
        #Arrange field in pdf page
        start_top = 15
        space_vertical = 12
        start_left = 36
        space_horizontal = 75
        ##Create First Page
        pdf.add_page()
        pdf.add_font("NunitoSans400", "", r"Nunito_Sans\NunitoSans-Regular.ttf", uni=True)
        pdf.set_font("NunitoSans400","",14)
        pdf.text(start_left, start_top, f"{self.sponsorship.getChild().getFirstName()}")
        pdf.text(start_left+space_horizontal, start_top, self.sponsorship.getDonor().getTitleFirstName())
        pdf.text(start_left, start_top+space_vertical, self.sponsorship.getChild().getChildId())
        pdf.text(start_left+space_horizontal, start_top+space_vertical, self.sponsorship.getDonor().getId())
        ##Create Second Page
        pdf.add_page()
        pdf.text(start_left, start_top, f"{self.sponsorship.getChild().getFirstName()}")
        pdf.text(start_left, start_top+space_vertical, self.sponsorship.getChild().getChildId())
        #Save Created Page
        pdf.output(f'TDL_{self.getChildId()}.pdf', "F")

        #Open the created page
        _path = os.getcwd() + f"\\TDL_{self.getChildId()}.pdf"
        os.system(f'cmd /c {_path}')

    def generatePageFront(self):
        pass
    def generatePageBack(self):
        pass

