import sqlite3
import sys
import fpdf

from Repository.comentarioRepo import ComentarioRepo
from Repository.usuarioRepo import UsuarioRepo
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
        self.informe2Button.clicked.connect(self.crearInforme2)
        ##self.informe3Button.clicked.connect(self.crearInforme3)
        self.informe4Button.clicked.connect(self.crearInforme4)
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

    def crearInforme2(self):

        email: str = "prueba@gmail.com"
        anime: str = "Dragon Ball Z"

        usuario_repo = UsuarioRepo()
        usuario = usuario_repo.getUsuario(email)
        comentario_repo = ComentarioRepo()
        comentarios = comentario_repo.getComentariosByUser(self, usuario)
 
        resultado =[]
        for comentario in comentarios:
            if comentario._id.__contains__(anime):
                resultado.append([comentario._id, comentario.usuario, comentario.texto, comentario.fecha])

        introduccion = (
            "En este documento se detallará la forma de realizar una consulta a la tabla COMENTARIO, "
            "con el objetivo de obtener la lista de comentarios realizados por un usuario en un anime específico. "
            "La consulta se centrará en la relación entre la tabla de usuarios y la tabla de comentarios, "
            "permitiendo así recuperar todos los comentarios realizados por un usuario sobre un anime determinado. "
        )

        detalle_consulta = (
            "Para hacer esta consulta, usamos el método `getComentariosByUser` del repositorio de comentarios, "
            "que nos da todos los comentarios hechos por un usuario en específico. Después, aplicamos un filtro "
            "para quedarnos solo con los comentarios que están relacionados con el anime que nos interesa. "
            "Los datos que usamos para la consulta fueron:\n\n"
            f"- **Email del usuario:** {email}\n"
            f"- **Nombre del anime:** {anime}\n\n"
            "**Cómo funciona:**\n"
            "El método `getComentariosByUser` busca, a través de esta consulta: SELECT * FROM COMENTARIO WHERE USUARIO = ?, todos los comentarios que ha hecho el usuario con el email que le pasamos. "
            "Luego, filtramos esos comentarios para quedarnos solo con los que tienen el nombre del anime en su identificador (`_id`). "
            "Esta forma de hacerlo es eficiente y nos permite encontrar rápidamente los comentarios de un usuario sobre un anime en particular."
        )

        conclusion = (
            "En resumen, este informe muestra cómo buscamos y filtramos los comentarios que el usuario '{email}' "
            f"ha hecho sobre el anime '{anime}'. Usamos el método `getComentariosByUser` para obtener todos sus comentarios "
            "y luego aplicamos un filtro para seleccionar solo los que están relacionados con este anime.\n\n"
            "Este método es práctico porque reutiliza la lógica del repositorio, lo que hace que el código sea más fácil de mantener "
            "y ampliar en el futuro. Los resultados que obtuvimos se presentan en este informe, lo que nos ayuda a entender mejor "
            "cómo interactúa el usuario con el contenido de la plataforma. Esta información es útil para tomar decisiones "
            "que mejoren la experiencia de los usuarios."
        )

        headers = ["Id", "Usuario", "Texto", "Fecha"]
        
        pdf = PDF2()
        pdf.add_page()
        pdf.add_title("Introducción")
        pdf.body(introduccion)
        
        pdf.add_title("Detalles consulta")
        pdf.body(detalle_consulta)

        pdf.add_title("Resultado de la consulta")
        pdf.add_results(headers, resultado)

        pdf.add_title("Conclusión")
        pdf.body(conclusion)
            
        try:
            pdf.output('informe2.pdf', 'F')
            QMessageBox.information(self,'Información', '¡Informe 2 creado con éxito!') 
        except:
            QMessageBox.critical(self,'Error', '¡Error al crear el informe 2!')

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

    def crearInforme4(self):
        # Conectar a la base de datos
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()

        # Consulta SQL para obtener los datos de la tabla ESTUDIO
        query = "SELECT nombre, pais, animes FROM ESTUDIO"
        cursor.execute(query)
        datos_estudios = cursor.fetchall()

        # Obtener estadísticas adicionales
        cursor.execute("SELECT COUNT(*) FROM ESTUDIO")
        total_estudios = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(DISTINCT pais) FROM ESTUDIO")
        total_paises = cursor.fetchone()[0]

        # Cerrar la conexión a la base de datos
        conn.close()

        # Crear el PDF
        pdf = PDF4()
        pdf.set_font('Times', '', 12)
        pdf.add_page()

        # Introducción
        introduccion = (
            "Este informe detalla la información sobre los estudios de animación registrados en la base de datos. "
            "Incluye la estructura de la tabla ESTUDIO y los datos de los estudios almacenados, mostrando su país de origen "
            "y las producciones más destacadas. A continuación, se presentan los datos recopilados junto con algunas estadísticas."
        )
        pdf.body_text(introduccion)

        # Estadísticas
        estadisticas = (
            f"Estadísticas:\n"
            f"- Número total de estudios: {total_estudios}\n"
            f"- Número total de países: {total_paises}\n"
        )
        pdf.body_text(estadisticas)

        # Datos de la tabla
        datos_convertidos = []
        for estudio in datos_estudios:
            nombre = estudio[0]
            pais = estudio[1]
            animes_raw = estudio[2]

            animes = animes_raw.replace("[", "").replace("]", "").replace('"', "").strip()

            datos_convertidos.append([nombre, pais, animes])

        pdf.body("Datos de los estudios:", ["Nombre", "País", "Animes"], datos_convertidos)

        # Conclusiones
        conclusiones = (
            "Conclusiones:\n"
            "Este informe muestra que la mayoría de los estudios de animación están ubicados en Japón, "
            "lo que refleja la importancia de este país en la industria de la animación. Además, se observa que "
            "cada estudio tiene una lista diversa de producciones destacadas."
        )
        pdf.body_text(conclusiones)

        try:
            pdf.output('informe4.pdf', 'F')
            QMessageBox.information(self, 'Información', '¡Informe 4 creado con éxito!')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'¡Error al crear el informe 4! Detalles: {str(e)}')

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