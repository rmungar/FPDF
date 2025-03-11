import sqlite3
import sys
import fpdf
from Repository.animeRepo import AnimeRepo
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
        self.setWindowTitle("Informes")

        self.informe1Button.clicked.connect(self.crearInforme1)
        self.informe2Button.clicked.connect(self.crearInforme2)
        self.informe3Button.clicked.connect(self.crearInforme3)
        self.informe4Button.clicked.connect(self.crearInforme4)
        self.informe5Button.clicked.connect(self.crearInforme5)

    def crearInforme1(self):
        
        pdf = PDF1()
        pdf.set_font('Times', '', 12)
        pdf.add_page()

        descripcion = (
        "Este informe presenta un análisis de los comentarios realizados sobre mangas y animes "
        "del género de Acción en la base de datos. Se incluyen detalles como el comentario realizado, "
        "la fecha en la que fue registrado, el título del contenido y su género.\n"
        "A continuación, se puede ver la consulta realizada:\n"
        "\n"
        """
        SELECT c.texto AS comentario, c.fecha AS fecha_comentario,
        COALESCE(m.nombre, a.nombre) AS titulo,
        COALESCE(m.genero, a.genero) AS genero
        FROM COMENTARIO c
        LEFT JOIN MANGA m ON m.comentarios LIKE '%' || c._id || '%' 
                          AND m.genero LIKE '%Acción%'  
        LEFT JOIN ANIME a ON a.comentarios LIKE '%' || c._id || '%' 
                          AND a.genero LIKE '%Acción%' 
        WHERE c.fecha = '2025-03-10'
        ORDER BY c.fecha DESC;\n
        """
        "\n"
        "Esta consulta va a acceder a los datos que necesitamos mediante el uso de LEFT JOIN y COALESCE.\n"
        "COALESCE -> Es una función de SQL que recorrerá todos los valores de una lista de columnas y retornará el primer valor no nulo de esta.\n"
        "LEFT JOIN -> Es una función de SQL que unirá dos tablas que devolverá todos los registros de la tabla izquiera y aquellos que coincidan de la derecha.\n"
        )



        pdf.body(descripcion)

        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()
        consulta = """
        SELECT c.texto AS comentario, c.fecha AS fecha_comentario,
        COALESCE(m.nombre, a.nombre) AS titulo,
        COALESCE(m.genero, a.genero) AS genero
        FROM COMENTARIO c
        LEFT JOIN MANGA m ON m.comentarios LIKE '%' || c._id || '%' 
                          AND m.genero LIKE '%Acción%'  
        LEFT JOIN ANIME a ON a.comentarios LIKE '%' || c._id || '%' 
                          AND a.genero LIKE '%Acción%' 
        WHERE c.fecha = '2025-03-10'
        ORDER BY c.fecha DESC;
        """
        cursor.execute(consulta)
        results = cursor.fetchall()
        headers = ["Comentario", "Fecha", "Título", "Género"]
        print(results)

        titulo = "Comentarios de Mangas y Animes con el género Acción"
        
        pdf.add_table(titulo, headers, results)
        
        
        try:
            pdf.output('informe1.pdf', 'F')
            QMessageBox.information(self,'Información', '¡Informe 1 creado con éxito!') 
        except:
            QMessageBox.critical(self,'Error', '¡Error al crear el informe 1!')

    def crearInforme2(self):

        email: str = "prueba@gmail.com"
        anime: str = "Naruto"

        """
        usuario_repo = UsuarioRepo()
        usuario = usuario_repo.getUsuario(email)
        comentario_repo = ComentarioRepo()
        comentarios = comentario_repo.getComentariosByUser(usuario)
 
        resultado =[]
        for comentario in comentarios:
            if comentario._id.__contains__(anime):
                resultado.append([comentario._id, comentario.usuario, comentario.texto, comentario.fecha])
        """
        

        
        conn = sqlite3.connect("default.db")
        cursor = conn.cursor()
#
        query = """
        SELECT c._id, c.usuario, c.texto, c.fecha 
        FROM COMENTARIO c
        JOIN USUARIO u ON c.usuario = u.email
        WHERE u.email = ? AND c._id LIKE ?
        """
#
        cursor.execute(query, (email, f"%-{anime}-%"))
        resultado  = cursor.fetchall()
        conn.close()

        print(resultado)

        introduccion = (
            "En este informe se explicará el proceso de consulta a la base de datos para obtener los comentarios "
            "realizados por un usuario específico sobre un anime determinado. La consulta que se describe a continuación "
            "permite obtener los comentarios de un usuario en función de un anime, utilizando la relación entre las tablas "
            "de usuarios y comentarios dentro de una base de datos SQL.\n\n"
        )

        detalle_consulta = (
            "La consulta SQL realizada está diseñada para filtrar los comentarios hechos por un usuario sobre un anime específico. "
        "En primer lugar, la consulta establece una relación entre las tablas COMENTARIO y USUARIO a través de un JOIN, "
        "basado en el campo 'usuario' de la tabla COMENTARIO, que coincide con el campo 'email' de la tabla USUARIO. "
        "A continuación, se aplica un filtro para asegurar que los comentarios sean aquellos realizados por el usuario "
        "con el email proporcionado y que el identificador del comentario (_id) contenga el nombre del anime, en este caso 'Naruto'.\n\n"
        "Los datos que se usan en esta consulta son los siguientes:\n"
        f"- Email del usuario: {email}\n"
        f"- Nombre del anime: {anime}\n"
        "\nConsulta SQL utilizada:\n"
            "```sql\n"
            "SELECT c._id, c.usuario, c.texto, c.fecha\n"
            "FROM COMENTARIO c\n"
            "JOIN USUARIO u ON c.usuario = u.email\n"
            "WHERE u.email = ? AND c._id LIKE ?\n"
        )

        resultado_detallado = (
            "El resultado de la consulta consiste en una lista de comentarios que cumplen con los criterios especificados. "
            "Cada registro incluye el identificador del comentario, el usuario que lo realizó, el texto del comentario y la fecha en "
            "que fue publicado. A continuación, se presentan los resultados obtenidos de la consulta:\n\n"
        )

        conclusion = (
            f"Este informe ha ilustrado el proceso de obtener los comentarios realizados por el usuario '{email}' sobre el anime '{anime}'. "
            "Mediante una consulta SQL bien estructurada, hemos logrado filtrar los registros de manera eficiente, asegurando que solo se "
            "recuperen los datos pertinentes. El uso del JOIN entre las tablas COMENTARIO y USUARIO y la condición LIKE en el campo _id "
            "permite realizar una búsqueda precisa, lo cual facilita el análisis de las interacciones del usuario con el contenido de anime.\n\n"
            "Es importante destacar que este enfoque puede adaptarse fácilmente a otros escenarios y tipos de consultas, "
            "siendo una solución versátil y escalable para la gestión y análisis de datos en bases de datos relacionales."
        )

        headers = ["Id", "Usuario", "Texto", "Fecha"]
        
        pdf = PDF2()
        pdf.add_page()
        pdf.add_title("Introducción")
        pdf.body(introduccion)
        
        pdf.add_title("Detalles consulta")
        pdf.body(detalle_consulta)

        pdf.add_title("Resultado de la Consulta")
        pdf.body(resultado_detallado)
        pdf.add_results(headers, resultado) 

        pdf.add_page
        pdf.add_title("Conclusión")
        pdf.body(conclusion)
            
        try:
            pdf.output('informe2.pdf', 'F')
            QMessageBox.information(self,'Información', '¡Informe 2 creado con éxito!') 
        except:
            QMessageBox.critical(self,'Error', '¡Error al crear el informe 2!')
#_______________________________________________________________________________________________________________________
    def crearInforme3(self):
        anime_name = "Attack on Titan"
        anime_repo = AnimeRepo()
        animes = anime_repo.getAnime()
        

        anime = next((anime for anime in animes if anime.getNombre() == anime_name), None)

        anime_icon = anime.imagen

        if not anime:
            QMessageBox.critical(self, 'Error', f'¡No se encontró el anime "{anime_name}" en la base de datos!')
            return

        introduccion = (
            f"En este informe se detallará la información concreta de un anime en específico, en este caso: {anime_name}. "
            "Para mostrar el cómo realizar la consulta que nos permita obtener los detalles de un anime en particular, "
            "para poder hacer uso de su información."
        )

        detalles_anime = [
            ["Nombre", anime.getNombre()],
            ["Sinopsis", anime.getSinopsis()],
            ["Género", anime.getGenero()],
            ["Estudio", anime.getEstudio()],
            ["Temporadas", str(anime.getTemporadas())],
            ["Capítulos", str(anime.getCapitulos())],
        ]

        instrucciones = (
            "Instrucciones para la extracción de datos:\n"
            "\n"
            "1. Seleccionar el anime en la base de datos.\n"
            "\n"
            "2. Obtener los detalles del anime, incluyendo su sinopsis, género, estudio de animación, temporadas y capítulos.\n"
            "\n"
            "3. Mostrar los resultados obtenidos en este informe para su análisis y uso posterior."
        )

        headers = ["Campo", "Valor"]

        pdf = PDF3()
        pdf.add_page()
        pdf.add_title("Introducción")
        pdf.body(introduccion)

        pdf.add_title("Detalles del Anime")
        pdf.ln(10) 
        pdf.add_table(headers, detalles_anime)

        pdf.add_page()
        pdf.add_title("Instrucciones")
        pdf.ln(10)
        pdf.body(instrucciones)

        try:
            pdf.output('informe3.pdf', 'F')
            QMessageBox.information(self, 'Información', '¡Informe 3 creado con éxito!')
        except:
            QMessageBox.critical(self, 'Error', '¡Error al crear el informe 3!')


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

    def crearInforme5(self):
        # Conectar a la base de datos
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()

        # Consulta SQL
        query = """
        SELECT generos.genero, 
            IFNULL(GROUP_CONCAT(DISTINCT a.nombre), 'N/A') AS animes, 
            IFNULL(GROUP_CONCAT(DISTINCT m.nombre), 'N/A') AS mangas
        FROM (
            SELECT TRIM(value) AS genero, nombre
            FROM ANIME
            CROSS JOIN json_each('["' || REPLACE(genero, ', ', '","') || '"]')
            UNION ALL
            SELECT TRIM(value) AS genero, nombre
            FROM MANGA
            CROSS JOIN json_each('["' || REPLACE(genero, ', ', '","') || '"]')
        ) AS generos
        LEFT JOIN ANIME a ON generos.nombre = a.nombre
        LEFT JOIN MANGA m ON generos.nombre = m.nombre
        GROUP BY generos.genero;
        """

        cursor.execute(query)
        datos_tabla = cursor.fetchall()

        conn.close()

        # Crear el PDF
        pdf = PDF5()
        pdf.add_page()

        # Introducción
        introduccion = (
            "Este informe detalla los géneros compartidos entre animes y mangas. "
            "Cada género listado contiene los animes y mangas que lo representan. "
            "El objetivo es proporcionar una visión general de cómo los géneros "
            "se distribuyen entre ambas categorías."
        )
        pdf.chapter_body(introduccion)
        pdf.ln(10)

        # Mostrar la consulta SQL
        pdf.set_font('Times', 'B', 12)
        pdf.cell(0, 10, 'Consulta SQL Utilizada:', 0, 1)
        pdf.set_font('Times', '', 10)
        pdf.multi_cell(0, 10, query)
        pdf.ln(10)

        # Explicación de la consulta
        explicacion = (
            "La consulta SQL divide los géneros de animes y mangas en filas separadas "
            "utilizando `json_each`. Luego, agrupa los resultados por género y concatena "
            "los nombres de los animes y mangas asociados a cada género. Si no hay animes "
            "o mangas para un género, se muestra 'N/A'."
        )
        pdf.chapter_body(explicacion)
        pdf.ln(10)

        # Tabla de géneros
        pdf.set_font('Times', 'B', 12)
        pdf.cell(0, 10, 'Tabla de Géneros:', 0, 1)
        pdf.create_table(
            ["Género", "Animes", "Mangas"],
            datos_tabla,
            [50, 70, 70]  # Ajustar el ancho de las columnas
        )
        pdf.ln(10)

        # Conclusión
        pdf.set_font('Times', 'B', 12)
        pdf.cell(0, 10, 'Conclusión:', 0, 1)
        conclusion = (
            "Este informe ha proporcionado un análisis detallado de los géneros "
            "compartidos entre animes y mangas. Se han identificado los géneros "
            "más comunes y se ha presentado un listado completo de animes y mangas "
            "por género. La consulta SQL utilizada permite obtener estos datos de "
            "manera eficiente y estructurada."
        )
        pdf.chapter_body(conclusion)

        # Guardar el PDF
        try:
            pdf.output('informe5.pdf', 'F')
            print("¡Informe 5 creado con éxito!")
        except Exception as e:
            print(f"Error al crear el informe 5: {str(e)}")



def main():
    app = QApplication(sys.argv)
    window = Pdfer()
    window.show()
    app.exec() 

if __name__ == '__main__':
    main()   