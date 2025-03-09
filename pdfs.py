from fpdf import FPDF


class PDF1(FPDF):
    def header(self):
        self.cell(0, 10, "Estructura de la Base de Datos", ln=True, align="C")
        self.ln(5)

    def body(self, body: str):
        self.set_font('Times', '', 12)
        self.multi_cell(0, 5, body)
        self.ln(5)
    def add_table(self, title, headers, data):
        self.set_font('Times', '', 12)
        self.cell(0, 10, title, ln=True, align="L")
        self.ln()
        
        col_widths = [50, 50, 90]
        self.set_font("Arial", size=10)
        self.set_fill_color(200, 200, 200)
        
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, border=1, align="C", fill=True)
        self.ln()
        
        for row in data:
            for i, item in enumerate(row):
                self.cell(col_widths[i], 10, str(item), border=1, align="C")
            self.ln()
        
        self.ln(5)


    def footer(self):
        self.set_font('Times', '', 12)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


class PDF2(FPDF):
    def header(self):
        path_logo = "logo.png"
        self.image(path_logo, 10, 8, 33)
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(30, 10, 'Informe de consulta a la tabla Comentario',ln=True, align="C")
        self.ln(20)

    def add_title(self, title):
        self.set_font('Times', 'B', 14)
        self.cell(0, 10, title, ln=True, align="C")
        self.ln(5)

    def body(self, text):
        self.set_font('Times', '', 12)
        self.multi_cell(0, 5, text)
        self.ln(10)

    def add_results(self, headers, resultados):        
        col_widths = [50, 40, 60, 40]
        self.set_font("Arial",'' , 10)
        self.set_fill_color(200, 200, 200)
        
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, border=1, align="C", fill=True)
        self.ln()
        
        for row in resultados:
            for i, item in enumerate(row):
                self.cell(col_widths[i], 10, str(item), border=1, align="C")
            self.ln()
        self.ln(5)

    def footer(self):
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'R')

class PDF3(FPDF):
    def header(self):
        self.set_font('Times', '', 12)

    def body(self, body):
        with open(body, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        self.set_font('Times', '', 12)
        self.multi_cell(0, 5, txt)

    def footer(self):
        self.set_font('Times', '', 12)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

class PDF4(FPDF):
    def header(self):
        self.set_font('Times', '', 12)

    def body(self, body):
        with open(body, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        self.set_font('Times', '', 12)
        self.multi_cell(0, 5, txt)

    def footer(self):
        self.set_font('Times', '', 12)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

class PDF5(FPDF):
    def header(self):
        self.set_font('Times', '', 12)

    def body(self, body):
        with open(body, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        self.set_font('Times', '', 12)
        self.multi_cell(0, 5, txt)

    def footer(self):
        self.set_font('Times', '', 12)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')