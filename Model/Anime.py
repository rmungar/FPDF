## cursor.execute(
##     """CREATE TABLE IF NOT EXISTS ANIME (
##     _id VARCHAR(255) PRIMARY KEY,
##     nombre VARCHAR(255) NOT NULL,
##     sinopsis TEXT NOT NULL,
##     genero VARCHAR(255) NOT NULL,
##     estudio VARCHAR(255) NOT NULL,
##     imagen VARCHAR(255) NOT NULL,
##     temporadas INTEGER NOT NULL,
##     capitulos INTEGER NOT NULL,
##     comentarios JSON)"""
## )

from Model.Comentario import Comentario


class Anime():
    def __init__(self, _id, nombre, sinopsis, genero, estudio, imagen, temporadas, capitulos, comentarios):
        self._id = _id
        self.nombre = nombre
        self.sinopsis = sinopsis
        self.genero = genero
        self.estudio = estudio
        self.imagen = imagen
        self.temporadas = temporadas
        self.capitulos = capitulos
        self.comentarios = comentarios


    def getComentarios(self):
        return self.comentarios

    def getEstudio(self):
        return self.estudio

    def getGenero(self):
        return self.genero

    def getImagen(self):
        return self.imagen

    def getNombre(self):
        return self.nombre

    def getSinopsis(self):
        return self.sinopsis

    def getTemporadas(self):
        return self.temporadas

    def getCapitulos(self):
        return self.capitulos

    def get_id(self):
        return self._id

    def setEstudio(self, estudio):
        self.estudio = estudio

    def __str__(self):
        return f"Anime: {self.nombre} - {self.sinopsis} - {self.genero} - {self.estudio} - {self.imagen} - {self.temporadas} - {self.capitulos} - {self.comentarios}"

