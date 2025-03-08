## cursor.execute(
##     """CREATE TABLE IF NOT EXISTS COMENTARIO (
##     _id VARCHAR(255) PRIMARY KEY, 
##     usuario VARCHAR(255) NOT NULL,
##     texto TEXT NOT NULL,
##     fecha DATE NOT NULL)"""
## )

from Model.Usuario import Usuario

class Comentario():
    def __init__(self, _id: str, usuario: Usuario, texto: str, fecha: str):
        self._id = _id
        self.usuario = usuario
        self.texto = texto
        self.fecha = fecha



    def getFecha(self):
        return self.fecha


    def getTexto(self):
        return self.texto

    def getUsuario(self):
        return self.usuario

    def get_id(self):
        return self._id

    def setFecha(self, fecha):
        self.fecha = fecha

    def setTexto(self, texto):
        self.texto = texto

    def setUsuario(self, usuario):
        self.usuario = usuario