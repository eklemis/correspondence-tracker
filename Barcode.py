import sys

from fpdf import FPDF
from pdf417 import encode, render_image
from PIL import Image

# collect & check user input
fo = open("check_file.txt", "rb")
check = fo.read()

last_id = check
last_id = int(check)

barcode_id = int(input("How many barcode do you need : "))
new_id  = last_id+barcode_id

results = [item for item in range(last_id, new_id)]
fo.close()


#save data to txt
def saveTxt(last_id, new_id) :
    textfile = open("check_file.txt", "w")
    last_id = str(new_id)
    textfile.write(last_id)

saveTxt(last_id, new_id)






# print barcode to jpg
imglist = []
for item in results:
    codes = encode(str(item), columns=3, security_level=2)
    image = render_image(codes, scale=3, ratio=2, padding=5, fg_color="Black", bg_color="#ddd")  # Pillow Image object
    image.save('barcode{0}.jpg'.format(item))
    '''print(type(image))'''
    imglist.append('barcode{0}.jpg'.format(item))






# convert barcode image to pdf
def print_barcode(start_id, total_id):
    x = 0
    y = 0
    w = 30
    h = 15
    margin_top = 15
    margin_left = 5
    per_row = 5
    per_col = 11
    count_barcode = start_id
    pdf = FPDF()
    pdf.add_page()

    for id in range(start_id, total_id):
        count_barcode += 1
        '''print(f"x={x + margin_left}, y={y + margin_top}")'''
        pdf.image(f"barcode{count_barcode - 1}.jpg", x + margin_left, y + margin_top, w, h)
        x += w + 10
        if count_barcode % per_row == 0:
            y += h + 10
            x = 0
        if count_barcode % (per_row * per_col) == 0:
            pdf.add_page()
            x = 0
            y = 0

    pdf.output('convert.pdf', "F")
    print("Adding all your barcodes into a pdf file")

print_barcode(last_id, new_id)











