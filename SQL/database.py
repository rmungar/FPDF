import sqlite3
import json

conn = sqlite3.connect('default.db')
cursor = conn.cursor()

# Crear tablas
cursor.execute(
    """CREATE TABLE IF NOT EXISTS USUARIO (
    nombre VARCHAR(255) NOT NULL PRIMARY KEY,
    passwd VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    comentarios JSON,
    favoritos JSON)"""
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS MANGA (
    _id VARCHAR(255) PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    sinopsis VARCHAR(255) NOT NULL,
    genero VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    imagen VARCHAR(255) NOT NULL,
    tomos INTEGER NOT NULL,
    capitulos INTEGER NOT NULL,
    comentarios TEXT)"""
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS ANIME (
    _id VARCHAR(255) PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    sinopsis TEXT NOT NULL,
    genero VARCHAR(255) NOT NULL,
    estudio VARCHAR(255) NOT NULL,
    imagen VARCHAR(255) NOT NULL,
    temporadas INTEGER NOT NULL,
    capitulos INTEGER NOT NULL,
    comentarios JSON)"""
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS MANGAKA (
    _id VARCHAR(255) PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    nacimiento DATE NOT NULL,
    nacionalidad VARCHAR(255) NOT NULL,
    imagen VARCHAR(255) NOT NULL,
    obras JSON)"""
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS ESTUDIO (
    nombre VARCHAR(255) PRIMARY KEY NOT NULL,
    pais VARCHAR(255) NOT NULL,
    imagen VARCHAR(255) NOT NULL,
    animes JSON)"""
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS COMENTARIO (
    _id VARCHAR(255) PRIMARY KEY, 
    usuario VARCHAR(255) NOT NULL,
    texto TEXT NOT NULL,
    fecha VARCHAR(255) NOT NULL)"""
)

# Forma de insertar datos
datosUsuarios = [
    ('prueba', 'passwordPrueba', 'prueba@gmail.com', json.dumps([]), json.dumps([])),
    
]
datosMangas = [
    ('ONE-ODA', 'One Piece', 'One Piece es un manga japonés escrito e ilustrado por Eiichirō Oda. Comenzó a publicarse en la revista Weekly Shōnen Jump el 22 de julio de 1997.', 'Aventura, Acción, Comedia, Drama, Fantasía', 'Eiichirō Oda', 'Resources/Manga/OP.jpg', 98, 1000, json.dumps([])),
    ('NAR-KIS', 'Naruto', 'Naruto es un manga japonés escrito e ilustrado por Masashi Kishimoto. Comenzó a publicarse en la revista Weekly Shōnen Jump el 21 de septiembre de 1999.', 'Aventura, Acción, Comedia, Drama, Fantasía', 'Masashi Kishimoto', 'Resources/Manga/NARUTO.jpg', 72, 700, json.dumps([])),
    ('DRA-AKI', 'Dragon Ball', 'Dragon Ball es un manga japonés escrito e ilustrado por Akira Toriyama. Comenzó a publicarse en la revista Weekly Shōnen Jump el 3 de diciembre de 1984.', 'Aventura, Acción, Comedia, Drama, Fantasía', 'Akira Toriyama', 'Resources/Manga/DBZ.jpg', 42, 520, json.dumps([])),
    ('BLE-TIT', 'Bleach', 'Bleach es un manga japonés escrito e ilustrado por Tite Kubo. Comenzó a publicarse en la revista Weekly Shōnen Jump el 7 de agosto de 2001.', 'Aventura, Acción, Comedia, Drama, Fantasía', 'Tite Kubo', 'Resources/Manga/BLEACH.jpg', 74, 686, json.dumps([]))
]
datosAnimes = [
    ('DBZ-TOEI', 'Dragon Ball Z', 'Goku y sus amigos protegen la Tierra de amenazas cósmicas.', 'Acción, Aventura, Fantasía', 'Toei Animation', 'Resources/Anime/DBZ.jpg', 9, 291, json.dumps([])),
    ('NARUTO-PIERROT', 'Naruto', 'Un joven ninja busca el reconocimiento y sueña con ser Hokage.', 'Acción, Aventura', 'Studio Pierrot', 'Resources/Anime/NARUTO.jpg', 9, 220, json.dumps([])),
    ('AOT-WIT', 'Attack on Titan', 'La humanidad lucha contra titanes devoradores de hombres.', 'Acción, Drama', 'Wit Studio', 'Resources/Anime/AOT.jpg', 4, 87, json.dumps([])),
    ('DEATHNOTE-MADHOUSE', 'Death Note', 'Un estudiante encuentra un cuaderno con poderes mortales.', 'Suspense, Misterio', 'Madhouse', 'Resources/Anime/DEATHNOTE.jpg', 1, 37, json.dumps([]))
]
datosMangakas = [
    ('Eiichiro Oda', 'Eiichiro Oda', '1975-01-01', 'Japonesa', 'Resources/Mangaka/ODA.jpg', '["One Piece"]'),
    ('Masashi Kishimoto', 'Masashi Kishimoto', '1974-11-08', 'Japonesa', 'Resources/Mangaka/KISHIMOTO.jpg', '["Naruto", "Boruto"]'),
    ('Hajime Isayama', 'Hajime Isayama', '1986-08-29', 'Japonesa', 'Resources/Mangaka/ISAYAMA.jpg', '["Attack on Titan"]'),
    ('Tite Kubo', 'Tite Kubo', '1977-06-26', 'Japonesa', 'Resources/Mangaka/KUBO.jpg', '["Bleach"]')
]
datosEstudios = [
    ('Toei Animation', 'Japón', 'Resources/Estudios/TOEI.png', '["Dragon Ball Z", "One Piece"]'),
    ('Studio Pierrot', 'Japón', 'Resources/Estudios/PIERROT.jpg', '["Naruto", "Bleach"]'),
    ('Wit Studio', 'Japón', 'Resources/Estudios/WIT.jpg', '["Attack on Titan", "Vinland Saga"]'),
    ('Madhouse', 'Japón', 'Resources/Estudios/MADHOUSE.png', '["Death Note", "One Punch Man"]')
]


cursor.executemany("INSERT INTO USUARIO (nombre, passwd, email, comentarios, favoritos) VALUES (?, ?, ?, ?, ?)", datosUsuarios)
cursor.executemany("INSERT INTO MANGA (_id, nombre, sinopsis, genero, autor, imagen, tomos, capitulos, comentarios) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", datosMangas)
cursor.executemany("INSERT INTO ANIME (_id, nombre, sinopsis, genero, estudio, imagen, temporadas, capitulos, comentarios) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", datosAnimes)
cursor.executemany("INSERT INTO MANGAKA (_id, nombre, nacimiento, nacionalidad, imagen, obras) VALUES (?, ?, ?, ?, ?, ?)", datosMangakas)
cursor.executemany("INSERT INTO ESTUDIO (nombre, pais, imagen, animes) VALUES (?, ?, ?, ?)", datosEstudios)


cursor.execute("SELECT * FROM MANGA")
mangas = cursor.fetchall()

cursor.execute("SELECT * FROM ANIME")
animes = cursor.fetchall()

cursor.execute("SELECT * FROM USUARIO")
usuarios = cursor.fetchall()

cursor.execute("SELECT * FROM MANGAKA")
mangakas = cursor.fetchall()

cursor.execute("SELECT * FROM ESTUDIO")
estudios = cursor.fetchall()

cursor.execute("SELECT * FROM COMENTARIO")
copmentarios = cursor.fetchall()

print("Mangas/n")
for manga in mangas:
    print(f"{manga}\n")

print("Animes/n")
for anime in animes:
    print(f"{anime}\n")

print("Usuarios/n")
for usuario in usuarios:
    print(f"{usuario}\n")

print("Mangakas\n")
for mangaka in mangakas:
    print(f"{mangaka}\n")

print("Estudios\n")
for estudio in estudios:
    print(f"{estudio}\n")

print("Comentarios\n")
for comentario in copmentarios:
    print(f"{comentario}\n")


# Guardar cambios
conn.commit()
conn.close()