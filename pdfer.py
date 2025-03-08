import sys
import fpdf

from pdfs import PDF1, PDF2, PDF3, PDF4, PDF5
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import uic

class Pdfer(QMainWindow):
    '''Esta es la clase principal'''
    
    def __init__(self):
        #Inicializa la ventana
        super(Pdfer, self).__init__() # Reservamos un espacio en memoria para la clase
      
        uic.loadUi('C:/Users/larad/Documents/FPDF/Ui/informes.ui',self)

        self.informe1Button.clicked.connect(self.crearInforme1)
        self.informe2Button.clicked.connect(self.crearInforme2)
        self.informe3Button.clicked.connect(self.crearInforme3)
        self.informe4Button.clicked.connect(self.crearInforme4)
        self.informe5Button.clicked.connect(self.crearInforme5)

    def crearInforme1(self):
        body = "Resources\Pdfs\pdf1.md"
        pdf = PDF1()
        pdf.add_page()
        pdf.body(body)
        pdf.set_font('Times', '', 12)
        try:
            pdf.output('informe1.pdf', 'F')
            QMessageBox.information(self,'Información', '¡Informe 1 creado con éxito!') 
        except:
            QMessageBox.critical(self,'Error', '¡Error al crear el informe 1!')

    def crearInforme2(self):
        body = "Resources\Pdfs\pdf2.md"
        pdf = PDF2()
        pdf.add_page()
        pdf.body(body)
        pdf.set_font('Times', '', 12)
        try:
            pdf.output('informe2.pdf', 'F')
            QMessageBox.information(self,'Información', '¡Informe 2 creado con éxito!') 
        except:
            QMessageBox.critical(self,'Error', '¡Error al crear el informe 2!')

    def crearInforme3(self):
        body = "Resources\Pdfs\pdf3.md"
        pdf = PDF3()
        pdf.add_page()
        pdf.body(body)
        pdf.set_font('Times', '', 12)
        try:
            pdf.output('informe3.pdf', 'F')
            QMessageBox.information(self,'Información', '¡Informe 3 creado con éxito!') 
        except:
            QMessageBox.critical(self,'Error', '¡Error al crear el informe 3!')

    def crearInforme4(self):
        body = "Resources\Pdfs\pdf4.md"
        pdf = PDF4()
        pdf.add_page()
        pdf.body(body)
        pdf.set_font('Times', '', 12)
        try:
            pdf.output('informe3.pdf', 'F')
            QMessageBox.information(self,'Información', '¡Informe 4 creado con éxito!') 
        except:
            QMessageBox.critical(self,'Error', '¡Error al crear el informe 4!')

    def crearInforme5(self):
        body = "Resources\Pdfs\pdf5.md"
        pdf = PDF5()
        pdf.add_page()
        pdf.body(body)
        pdf.set_font('Times', '', 12)
        try:
            pdf.output('informe3.pdf', 'F')
            QMessageBox.information(self,'Información', '¡Informe 5 creado con éxito!') 
        except:
            QMessageBox.critical(self,'Error', '¡Error al crear el informe 5!')



def main():
    app = QApplication(sys.argv)
    window = Pdfer()
    window.show()
    app.exec() 

if __name__ == '__main__':
    main()   