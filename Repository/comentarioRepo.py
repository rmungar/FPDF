import json
import sqlite3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class ComentarioRepo():

    from Model.Comentario import Comentario
    from Model.Usuario import Usuario

    def getComentarios(self) -> list[Comentario]:

        from Model.Comentario import Comentario

        db_path = os.path.abspath("default.db")  # Asegura que accedemos a la base de datos correcta
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM COMENTARIO")
        comentariosBD = cursor.fetchall()  # Recuperar todos los resultados

        comentarios = []
        for comentarioBD in comentariosBD:
            comentario = Comentario(comentarioBD[0], comentarioBD[1], comentarioBD[2], comentarioBD[3])
            comentarios.append(comentario)

        conn.close()
        return comentarios
    

    def getComentariosByUser(self, usuario: Usuario) -> list[Comentario]:

        from Model.Comentario import Comentario

        db_path = os.path.abspath("default.db")  # Asegura que accedemos a la base de datos correcta
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM COMENTARIO WHERE USUARIO = ?",(usuario.email,))
        comentariosBD = cursor.fetchall()  # Recuperar todos los resultados

        comentarios = []
        for comentarioBD in comentariosBD:
            comentario = Comentario(comentarioBD[0], comentarioBD[1], comentarioBD[2], comentarioBD[3])
            comentarios.append(comentario)

        conn.close()
        return comentarios


    def addComentarioToAnime(self, comentario: Comentario):
        db_path = os.path.abspath("default.db")  # Asegura que usamos la base de datos correcta
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Insertar en la tabla COMENTARIO
        cursor.execute(
            "INSERT OR REPLACE INTO COMENTARIO VALUES (?, ?, ?, ?)", 
            (comentario._id, comentario.usuario, comentario.texto, comentario.fecha)
        )

        # Obtener los comentarios actuales del anime
        cursor.execute("SELECT comentarios FROM ANIME WHERE _id = ?", (comentario._id,))
        row = cursor.fetchone()

        if row:
            comentarios_actuales = json.loads(row[0]) if row[0] else []
        else:
            comentarios_actuales = []

        # Agregar el nuevo comentario
        nuevo_comentario = {
            "usuario": comentario.usuario,
            "comentario": comentario.texto,
            "fecha": comentario.fecha
        }
        comentarios_actuales.append(nuevo_comentario)

        # Guardar de nuevo el JSON en la base de datos
        cursor.execute(
            "UPDATE ANIME SET comentarios = ? WHERE _id = ?",
            (json.dumps(comentarios_actuales), comentario._id)
        )

        conn.commit()  # Asegura que se guardan los cambios
        conn.close()

def main():
    print(ComentarioRepo.getComentarios())


if __name__ == '__main__':
    main()