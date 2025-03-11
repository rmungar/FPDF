from fpdf import FPDF


class PDF1(FPDF):
    def header(self):
        path_logo = "LogoAnigiri.jpeg"
        self.image(path_logo, 10, 8, 33)
        self.cell(0, 10, "Comentarios de Mangas y Animes de un género específico", ln=True, align="C")
        self.ln(25)

    def body(self, body: str):
        self.set_font('Times', '', 12)
        self.multi_cell(0, 5, body)
        self.ln(10)

    def add_table(self, title, headers, data):
        self.set_font("Times", style="B", size=12)
        self.cell(0, 10, title, ln=True, align="C")
        self.ln(2)

        col_widths = [40, 30, 30, 80]
        page_width = self.w  
        total_width = sum(col_widths)
        start_x = (page_width - total_width) / 2  

        self.set_x(start_x)
       

        self.set_font("Arial", size=10)
        self.set_fill_color(200, 200, 200)

        
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, border=1, align="C", fill=True)
        self.ln()

        
        for row in data:
            self.set_x(start_x)
            comentario, fecha, titulo, genero = row[0], row[1], row[2], row[3]
            x, y = self.get_x(), self.get_y()
            self.multi_cell(col_widths[0], 10, str(comentario), border=1, align="C")  # Comentario
            self.set_xy(x + col_widths[0], y)

            self.cell(col_widths[1], 10, str(fecha), border=1, align="C")  # Fecha
            self.cell(col_widths[2], 10, str(titulo), border=1, align="C")  # Título
            self.cell(col_widths[3], 10, str(genero), border=1, align="C")  # Género
            self.ln()

        self.ln(5)



class PDF2(FPDF):
    def header(self):
        path_logo = "LogoAnigiri.jpeg"
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
        path_logo = "LogoAnigiri.jpeg"
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
        self.image('LogoAnigiri.jpeg', x=10, y=10, w=30)  # Ajusta las coordenadas (x, y) y el tamaño (w) según sea necesario

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
        

        # Encabezado del PDF
        self.set_font('Times', 'B', 16)
        self.cell(0, 10, 'Informe de Géneros Compartidos', 0, 1, 'C')
        self.ln(20)

        self.image('LogoAnigiri.jpeg', x=10, y=10, w=30)
        self.ln(10)

    def footer(self):
        # Pie de página del PDF
        self.set_y(-15)
        self.set_font('Times', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def chapter_body(self, text):
        # Cuerpo de sección
        self.set_font('Times', '', 12)
        self.multi_cell(0, 10, text)
        self.ln()

    def create_table(self, headers, data, col_widths):
        # Crear una tabla con fuente más pequeña
        self.set_font('Times', 'B', 10)  # Fuente más pequeña para encabezados
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, 1, 0, 'C')
        self.ln()
        self.set_font('Times', '', 8)  # Fuente más pequeña para datos
        for row in data:
            for i, item in enumerate(row):
                self.cell(col_widths[i], 10, item, 1, 0, 'C')
            self.ln()