## cursor.execute(
##     """CREATE TABLE IF NOT EXISTS USUARIO (
##     nombre VARCHAR(255) NOT NULL PRIMARY KEY,
##     passwd VARCHAR(255) NOT NULL,
##     email VARCHAR(255) NOT NULL,
##     comentarios JSON,
##     favoritos JSON)"""
## )




import json
import sqlite3


class Usuario():
    
    def __init__(self, nombre: str, passwd: str, email: str, comentarios: list, favoritos: list):
        self.nombre = email.split("@")[0]
        self.passwd = passwd
        self.email = email
        self.comentarios = comentarios
        self.favoritos = favoritos
        self.load_favoritos()

    def load_favoritos(self):
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()
        query = "SELECT favoritos FROM USUARIO WHERE nombre = ?"
        cursor.execute(query, (self.nombre,))
        result = cursor.fetchone()
        
        if result and result[0]:  # Si hay datos
            try:
                self.favoritos = json.loads(result[0])  # Convertir el JSON a lista
            except json.JSONDecodeError:
                self.favoritos = []  # Si hay error en JSON, usar lista vacía
        else:
            self.favoritos = []


    def updateComentarios(self, comentario):
        from Model.Comentario import Comentario
        if comentario is Comentario:
            self.comentarios.append(comentario)


    def updateFavoritos(self, favorito):
        from Model.Manga import Manga
        from Model.Anime import Anime
        removed = False
        if isinstance(favorito, Manga) or isinstance(favorito, Anime):
            for fav in self.favoritos:  
                if favorito._id == fav["_id"] if isinstance(fav, dict) else fav._id:
                    self.favoritos.remove(fav)
                    removed = True
            if not removed:    
                self.favoritos.append(favorito)
            self.save_favoritos()

    def save_favoritos(self):
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()
        # Convertir la lista de favoritos a JSON
        favoritos_json = json.dumps([fav if isinstance(fav, dict) else fav.__dict__ for fav in self.favoritos])  # Suponiendo que Manga y Anime tienen atributos
        query = "UPDATE USUARIO SET favoritos = ? WHERE nombre = ?"
        cursor.execute(query, (favoritos_json, self.nombre))
        conn.commit()
    

    def __str__(self):
        return f"Usuario: {self.nombre}, {self.email}"