## cursor.execute(
##     """CREATE TABLE IF NOT EXISTS ESTUDIO (
##     nombre VARCHAR(255) PRIMARY KEY NOT NULL,
##     pais VARCHAR(255) NOT NULL,
##     animes JSON)"""
## )

class Estudio():
    def __init__(self, nombre, pais, imagen, animes):
        self.nombre = nombre
        self.pais = pais
        self.imagen = imagen
        self.animes = animes

    def getAnimes(self):
        return self.animes

    def getNombre(self):
        return self.nombre

    def getPais(self):
        return self.pais

    def setAnimes(self, animes):
        self.animes = animes

    def setNombre(self, nombre):
        self.nombre = nombre

    def setPais(self, pais):
        self.pais = pais    

    def __str__(self):
        return f"{self.nombre} ({self.pais})"