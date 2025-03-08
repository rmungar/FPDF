from fpdf import FPDF


class PDF1(FPDF):
    def header(self):
        self.set_font('Times', '', 12)
    def footer(self):
        self.set_font('Times', '', 12)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

class PDF2(FPDF):
    def header(self):
        self.set_font('Times', '', 12)
    def footer(self):
        self.set_font('Times', '', 12)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

class PDF3(FPDF):
    def header(self):
        self.set_font('Times', '', 12)
    def footer(self):
        self.set_font('Times', '', 12)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

class PDF4(FPDF):
    def header(self):
        self.set_font('Times', '', 12)
    def footer(self):
        self.set_font('Times', '', 12)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

class PDF5(FPDF):
    def header(self):
        self.set_font('Times', '', 12)
    def footer(self):
        self.set_font('Times', '', 12)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')