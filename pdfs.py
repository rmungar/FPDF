from fpdf import FPDF


class PDF1(FPDF):
    def header(self):
        path_logo = "logo.png"
        self.image(path_logo, 10, 8, 33)
        self.cell(0, 10, "Estructura de la Base de Datos", ln=True, align="C")
        self.ln(20)

    def body(self, body: str):
        self.set_font('Times', '', 12)
        self.multi_cell(0, 5, body)
        self.ln(5)
    def add_table(self, title, headers, data):
        self.set_font('Times', '', 10)
        self.cell(0, 10, title, ln=True, align="L")
        self.ln()
        
        col_widths = [50, 50, 90]
        self.set_font('Times', '', 10)
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
        path_logo = "logo.png"
        self.image(path_logo, 10, 8, 33)
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(30, 10, 'Informe de Anime', ln=True, align="C")
        self.ln(20)
        self.alias_nb_pages()

    def add_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, ln=True, align="C")
        self.ln(5)

    def body(self, text):
        self.set_font('Times', '', 12)
        self.multi_cell(0, 5, text, align="L")
        self.ln(10)

    def add_table(self, headers, data):
        self.set_font('Arial', 'B', 10)
        self.set_fill_color(200, 200, 200)

        col_widths = [40, 150]  
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, border=1, align="C", fill=True)
        self.ln()

        self.set_font("Arial", '', 10)
        for row in data:
            for i, item in enumerate(row):
                self.cell(col_widths[i], 10, str(item), border=1, align="C")
            self.ln()
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Times', '', 12)
        self.cell(0, 10, 'Página ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

class PDF4(FPDF):
    def header(self):
        # Añadir el logo en la parte superior izquierda
        self.image('logo.png', x=10, y=10, w=30)  # Ajusta las coordenadas (x, y) y el tamaño (w) según sea necesario

        # Título del informe
        self.set_font('Times', 'B', 14)
        self.cell(0, 10, "Informe de Estudios de Animación", ln=True, align="C")
        self.ln(20)  # Ajusta el espacio después del título

    def body_text(self, text):
        self.set_font('Times', '', 12)
        self.multi_cell(0, 10, text)
        self.ln(5)

    def body_table(self, headers, data):
        self.set_font('Times', 'B', 12)
        col_widths = [60, 50, 80]

        # Encabezados
        self.set_fill_color(200, 200, 200)
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, border=1, align="C", fill=True)
        self.ln()

        # Filas de datos
        self.set_font('Times', '', 10)
        for row in data:
            self.cell(col_widths[0], 10, row[0], border=1, align="C")  # Nombre
            self.cell(col_widths[1], 10, row[1], border=1, align="C")  # País
            self.multi_cell(col_widths[2], 10, row[2], border=1, align="C")  # Animes

        self.ln(5)

    def body(self, text, headers, data):
        self.body_text(text)
        self.body_table(headers, data)

    def footer(self):
        self.set_y(-15)
        self.set_font('Times', '', 12)
        self.cell(0, 10, 'Página ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

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