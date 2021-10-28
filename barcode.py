from fpdf import FPDF
from pdf417 import encode, render_image
import os

class Barcode:
    def __init__(self):
        self.last_id = self.getLastId()

    def getLastId(self):
        source = open("check_file.txt", "rb")
        data = source.read()
        last_id = 0
        if data != b'':
            last_id = int(data)
        print(last_id)
        source.close()
        return last_id

    def setLastId(self, newlastid):
        dest = open("check_file.txt", "w")
        dest.write(str(newlastid))
        dest.close()

    def generateBarcode(self, number_of_barcode=1):
        #First we generate codes that will made barcode
        start_code = self.last_id+1
        barcodes = [code for code in range(start_code, start_code+number_of_barcode)]
        last_code = barcodes[-1]

        print(barcodes)

        barcodeImages = []
        for code in barcodes:
            codes = encode(str(code), columns=3, security_level=2)
            image = render_image(codes, scale=3, ratio=2, padding=5, fg_color="Black",
                                 bg_color="#ddd")  # Pillow Image object
            image.save('barcodes\\barcode{0}.jpg'.format(code))
            barcodeImages.append('barcodes\\barcode{0}.jpg'.format(code))

        #Set barcode image positions on pdf page
        x = 0
        y = 0
        w = 30
        h = 15
        margin_top = 15
        margin_left = 5
        per_row = 5
        per_col = 11
        count_barcode = self.last_id
        pdf = FPDF()
        pdf.add_page()

        for image_path in barcodeImages:
            count_barcode += 1
            pdf.image(image_path, x + margin_left, y + margin_top, w, h)
            x += w + 10
            if count_barcode % per_row == 0:
                y += h + 10
                x = 0
            if count_barcode % (per_row * per_col) == 0:
                pdf.add_page()
                x = 0
                y = 0

        pdf.output('barcodes.pdf', "F")
        _path = os.getcwd()+"\\barcodes.pdf"
        os.system(f'cmd /c {_path}')
        self.setLastId(last_code)


