import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Model.Mangaka

class MangakaRepo():
    def getMangakas(self) -> list[Model.Mangaka.Mangaka]:
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM MANGAKA")
        mangakasBD = cursor.fetchall()
        mangakas = []
        for mangakaBD in mangakasBD:
            mangaka = Model.Mangaka.Mangaka(mangakaBD[0], mangakaBD[1], mangakaBD[2], mangakaBD[3], mangakaBD[4], mangakaBD[5])
            mangakas.append(mangaka)

        return mangakas