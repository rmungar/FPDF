import fpdf

from pdfs import PDF1, PDF2, PDF3, PDF4, PDF5

class Pdfer():


    def crearInforme1(self):
        pdf = PDF1()
        pdf.add_page()
        pdf.set_title()
        pdf.set_font('Times', '', 12)

    def crearInforme2(self):
        pdf = PDF2()
        pdf.add_page()
        pdf.set_title()
        pdf.set_font('Times', '', 12)

    def crearInforme3(self):
        pdf = PDF3()
        pdf.add_page()
        pdf.set_title()
        pdf.set_font('Times', '', 12)

    def crearInforme4(self):
        pdf = PDF4()
        pdf.add_page()
        pdf.set_title()
        pdf.set_font('Times', '', 12)

    def crearInforme5(self):
        pdf = PDF5()
        pdf.add_page()
        pdf.set_title()
        pdf.set_font('Times', '', 12)