import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Model.Anime



class AnimeRepo():
    
    def getAnime(self) -> list[Model.Anime.Anime]:
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM ANIME")
        animesBD = cursor.fetchall()
        animes = []

        for animeBD in animesBD:
            anime = Model.Anime.Anime(animeBD[0], animeBD[1], animeBD[2], animeBD[3], animeBD[4], animeBD[5], animeBD[6], animeBD[7], animeBD[8])
            animes.append(anime)

        return animes
    
    

