import os
from fpdf import FPDF

pdf = FPDF()
pdf.set_auto_page_break(0)


imagelist = [i for i in os.listdir('Images') if i.endswith('jpg')]


for image in sorted(imagelist):

    pdf.add_page()
    pdf.image('Images/' + image, w=190, h=280)
    pdf.set_link("http://www.fpdf.org/", 10, 2)


pdf.output("wf.pdf", "F")











    































   






