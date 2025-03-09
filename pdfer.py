import sys
import fpdf

from pdfs import PDF1, PDF2, PDF3, PDF4, PDF5
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import uic
import os
basedir = os.getcwd()

class Pdfer(QMainWindow):
    '''Esta es la clase principal'''
    
    def __init__(self):
        #Inicializa la ventana
        super(Pdfer, self).__init__() # Reservamos un espacio en memoria para la clase
        print(basedir)
        uic.loadUi(f'{basedir}/Ui/informes.ui',self)

        self.informe1Button.clicked.connect(self.crearInforme1)
        ##self.informe2Button.clicked.connect(self.crearInforme2)
        ##self.informe3Button.clicked.connect(self.crearInforme3)
        ##self.informe4Button.clicked.connect(self.crearInforme4)
        ##self.informe5Button.clicked.connect(self.crearInforme5)

    def crearInforme1(self):
        
        pdf = PDF1()
        pdf.set_font('Times', '', 12)
        pdf.add_page()
        
        estructuras = [
            ("Tabla: USUARIO", ["Campo", "Tipo", "Descripción"], [
                ["nombre", "VARCHAR(255) NOT NULL", "Nombre del usuario (clave primaria)."],
                ["passwd", "VARCHAR(255) NOT NULL", "Contraseña del usuario."],
                ["email", "VARCHAR(255) NOT NULL", "Correo electrónico del usuario."],
                ["comentarios", "JSON", "Almacena los comentarios en formato JSON."],
                ["favoritos", "JSON", "Almacena los favoritos en formato JSON."],
            ]),
            ("Tabla: MANGA", ["Campo", "Tipo", "Descripción"], [
                ["_id", "VARCHAR(255) PRIMARY KEY", "Identificador único del manga."],
                ["nombre", "VARCHAR(255) NOT NULL", "Nombre del manga."],
                ["sinopsis", "VARCHAR(255) NOT NULL", "Sinopsis breve del manga."],
                ["genero", "VARCHAR(255) NOT NULL", "Género del manga."],
                ["autor", "VARCHAR(255) NOT NULL", "Autor del manga."],
                ["imagen", "VARCHAR(255) NOT NULL", "URL de la imagen del manga."],
                ["tomos", "INTEGER NOT NULL", "Número de tomos del manga."],
                ["capitulos", "INTEGER NOT NULL", "Número de capítulos del manga."],
                ["comentarios", "TEXT", "Comentarios sobre el manga."],
            ]),
            ("Tabla: ANIME", ["Campo", "Tipo", "Descripción"], [
                ["_id", "VARCHAR(255) PRIMARY KEY", "Identificador único del anime."],
                ["nombre", "VARCHAR(255) NOT NULL", "Nombre del anime."],
                ["sinopsis", "TEXT NOT NULL", "Sinopsis detallada del anime."],
                ["genero", "VARCHAR(255) NOT NULL", "Género del anime."],
                ["estudio", "VARCHAR(255) NOT NULL", "Estudio de animación."],
                ["imagen", "VARCHAR(255) NOT NULL", "URL de la imagen del anime."],
                ["temporadas", "INTEGER NOT NULL", "Número de temporadas."],
                ["capitulos", "INTEGER NOT NULL", "Número de capítulos."],
                ["comentarios", "JSON", "Comentarios en formato JSON."],
            ]),
            ("Tabla: MANGAKA", ["Campo", "Tipo", "Descripción"], [
                ["_id", "VARCHAR(255) PRIMARY KEY", "Identificador único del mangaka."],
                ["nombre", "VARCHAR(255) NOT NULL", "Nombre del mangaka."],
                ["nacimiento", "DATE NOT NULL", "Fecha de nacimiento del mangaka."],
                ["nacionalidad", "VARCHAR(255) NOT NULL", "Nacionalidad del mangaka."],
                ["imagen", "VARCHAR(255) NOT NULL", "URL de la imagen del mangaka."],
                ["obras", "JSON", "Lista de obras en formato JSON."],
            ]),
            ("Tabla: ESTUDIO", ["Campo", "Tipo", "Descripción"], [
                ["nombre", "VARCHAR(255) PRIMARY KEY", "Nombre del estudio de animación."],
                ["pais", "VARCHAR(255) NOT NULL", "País de origen."],
                ["imagen", "VARCHAR(255) NOT NULL", "URL de la imagen del estudio."],
                ["animes", "JSON", "Lista de animes producidos en formato JSON."],
            ]),
            ("Tabla: COMENTARIO", ["Campo", "Tipo", "Descripción"], [
                ["_id", "VARCHAR(255) PRIMARY KEY", "Identificador único del comentario."],
                ["usuario", "VARCHAR(255) NOT NULL", "Usuario que realiza el comentario."],
                ["texto", "TEXT NOT NULL", "Contenido del comentario."],
                ["fecha", "VARCHAR(255) NOT NULL", "Fecha del comentario."],
            ]),
        ]
        body = (
            "Este documento contiene información relacionada con la estructura de la base de datos utilizada en la aplicación. "
            "A continuación, se detallan los elementos de la base de datos, sus relaciones y cómo se gestionan los datos "
            "en la aplicación. Este informe proporciona una visión general de cómo los datos se almacenan y organizan "
            "para su manipulación eficiente."
        )
        pdf.body(body)

        for title, headers, data in estructuras:
            pdf.add_table(title, headers, data)

        
        try:
            pdf.output('informe1.pdf', 'F')
            QMessageBox.information(self,'Información', '¡Informe 1 creado con éxito!') 
        except:
            QMessageBox.critical(self,'Error', '¡Error al crear el informe 1!')

    ## def crearInforme2(self):
    ##     body = "Resources\Pdfs\pdf2.md"
    ##     pdf = PDF2()
    ##     pdf.add_page()
    ##     pdf.body(body)
    ##     pdf.set_font('Times', '', 12)
    ##     try:
    ##         pdf.output('informe2.pdf', 'F')
    ##         QMessageBox.information(self,'Información', '¡Informe 2 creado con éxito!') 
    ##     except:
    ##         QMessageBox.critical(self,'Error', '¡Error al crear el informe 2!')

    ## def crearInforme3(self):
    ##     body = "Resources\Pdfs\pdf3.md"
    ##     pdf = PDF3()
    ##     pdf.add_page()
    ##     pdf.body(body)
    ##     pdf.set_font('Times', '', 12)
    ##     try:
    ##         pdf.output('informe3.pdf', 'F')
    ##         QMessageBox.information(self,'Información', '¡Informe 3 creado con éxito!') 
    ##     except:
    ##         QMessageBox.critical(self,'Error', '¡Error al crear el informe 3!')

    ## def crearInforme4(self):
    ##     body = "Resources\Pdfs\pdf4.md"
    ##     pdf = PDF4()
    ##     pdf.add_page()
    ##     pdf.body(body)
    ##     pdf.set_font('Times', '', 12)
    ##     try:
    ##         pdf.output('informe3.pdf', 'F')
    ##         QMessageBox.information(self,'Información', '¡Informe 4 creado con éxito!') 
    ##     except:
    ##         QMessageBox.critical(self,'Error', '¡Error al crear el informe 4!')

    ## def crearInforme5(self):
    ##     body = "Resources\Pdfs\pdf5.md"
    ##     pdf = PDF5()
    ##     pdf.add_page()
    ##     pdf.body(body)
    ##     pdf.set_font('Times', '', 12)
    ##     try:
    ##         pdf.output('informe3.pdf', 'F')
    ##         QMessageBox.information(self,'Información', '¡Informe 5 creado con éxito!') 
    ##     except:
    ##         QMessageBox.critical(self,'Error', '¡Error al crear el informe 5!')



def main():
    app = QApplication(sys.argv)
    window = Pdfer()
    window.show()
    app.exec() 

if __name__ == '__main__':
    main()   