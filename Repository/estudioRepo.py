import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Model.Estudio

class EstudioRepo():
    def getEstudios(self) -> list[Model.Estudio.Estudio]:
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM ESTUDIO")
        estudiosBD = cursor.fetchall()
        estudios = []

        for estudioBD in estudiosBD:
            estudio = Model.Estudio.Estudio(estudioBD[0], estudioBD[1], estudioBD[2], estudioBD[3])
            estudios.append(estudio)

        return estudios