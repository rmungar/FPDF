## cursor.execute(
##     """CREATE TABLE IF NOT EXISTS MANGA (
##     _id VARCHAR(255) PRIMARY KEY,
##     nombre VARCHAR(255) NOT NULL,
##     sinopsis VARCHAR(255) NOT NULL,
##     genero VARCHAR(255) NOT NULL,
##     autor VARCHAR(255) NOT NULL,
##     imagen VARCHAR(255) NOT NULL,
##     tomos INTEGER NOT NULL,
##     capitulos INTEGER NOT NULL,
##     comentarios TEXT)"""
## )

from Model.Comentario import Comentario


class Manga():
    def __init__(self, _id, nombre, sinopsis, genero, autor, imagen, tomos, capitulos, comentarios):
        self._id = _id
        self.nombre = nombre
        self.sinopsis = sinopsis
        self.genero = genero
        self.autor = autor
        self.imagen = imagen
        self.tomos = tomos
        self.capitulos = capitulos
        self.comentarios = comentarios


    def addComentario(self, comentario):
        if comentario is Comentario:
            self.comentarios.append(comentario)

    def getComentarios(self):
        return self.comentarios

    def getAutor(self):
        return self.autor

    def getGenero(self):
        return self.genero

    def getImagen(self):
        return self.imagen

    def getNombre(self):
        return self.nombre

    def getSinopsis(self):
        return self.sinopsis

    def getTomos(self):
        return self.tomos

    def getCapitulos(self):
        return self.capitulos

    def get_id(self):
        return self._id

    def setAutor(self, autor):
        self.autor = autor

    def setGenero(self, genero):
        self.genero = genero

    def setImagen(self, imagen):
        self.imagen = imagen

    def setNombre(self, nombre):
        self.nombre = nombre

    def setSinopsis(self, sinopsis):
        self.sinopsis = sinopsis

    def setTomos(self, tomos):
        self.tomos = tomos

    def setCapitulos(self, capitulos):
        self.capitulos = capitulos

    def __str__(self):
        return f"{self.nombre} ({self.autor})"