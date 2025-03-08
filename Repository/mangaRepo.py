import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Model.Manga

class MangaRepo():
    def getMangas(self) -> list[Model.Manga.Manga]:
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM MANGA")
        mangasBD = cursor.fetchall()
        mangas = []

        for mangaBD in mangasBD:
            manga = Model.Manga.Manga(mangaBD[0], mangaBD[1], mangaBD[2], mangaBD[3], mangaBD[4], mangaBD[5], mangaBD[6], mangaBD[7], mangaBD[8])
            mangas.append(manga)

        return mangas