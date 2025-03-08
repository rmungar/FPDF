## cursor.execute(
##     """CREATE TABLE IF NOT EXISTS MANGAKA (
##     _id VARCHAR(255) PRIMARY KEY,
##     nombre VARCHAR(255) NOT NULL,
##     nacimiento DATE NOT NULL,
##     nacionalidad VARCHAR(255) NOT NULL,
##     obras JSON)"""
## )

class Mangaka():
    def __init__(self, _id, nombre, nacimiento, nacionalidad, imagen, obras):
        self._id = _id
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.nacionalidad = nacionalidad
        self.imagen = imagen
        self.obras = obras

    def getNacimiento(self):
        return self.nacimiento

    def getNacionalidad(self):
        return self.nacionalidad

    def getNombre(self):
        return self.nombre

    def getObras(self):
        return self.obras

    def get_id(self):
        return self._id

    def setNacimiento(self, nacimiento):
        self.nacimiento = nacimiento

    def setNacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setObras(self, obras):
        self.obras = obras

    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"