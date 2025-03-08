CREATE TABLE USUARIO (
    nombre VARCHAR(255) NOT NULL PRIMARY KEY,
    passwd VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    vistos JSON,
    empezados JSON,
    guardados JSON,
    comentarios JSON,
    favoritos JSON
);

CREATE TABLE ANIME (
    _id VARCHAR(255) PRIMARY KEY, -- Mezcla entre el estudio y el nombre (DBZ-TOEI)
    nombre VARCHAR(255) NOT NULL,
    sinopsis TEXT NOT NULL,
    genero VARCHAR(255) NOT NULL,
    estudio VARCHAR(255) NOT NULL, -- Referencia al nombre del estudio
    imagen VARCHAR(255) NOT NULL,
    temporadas INTEGER NOT NULL,
    capitulos INTEGER NOT NULL,
    comentarios JSON
);

CREATE TABLE MANGA (
    _id VARCHAR(255) PRIMARY KEY, -- Mezcla entre el nombre y el autor (ONE-ODA)
    nombre VARCHAR(255) NOT NULL,
    sinopsis VARCHAR(255) NOT NULL,
    genero VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,    -- Referencia al id del mangaka
    imagen VARCHAR(255) NOT NULL,
    tomos INTEGER NOT NULL,
    capitulos INTEGER NOT NULL,
    comentarios JSON
);

CREATE TABLE MANGAKA (
    _id VARCHAR(255) PRIMARY KEY, -- Nombre Completo
    nombre VARCHAR(255) NOT NULL,
    nacimiento DATE NOT NULL,
    nacionalidad VARCHAR(255) NOT NULL,
    obras JSON
);


CREATE TABLE ESTUDIO (
    nombre VARCHAR(255) PRIMARY KEY NOT NULL,
    pais VARCHAR(255) NOT NULL,
    animes JSON
);

CREATE TABLE COMENTARIO (
    _id VARCHAR(255) PRIMARY KEY, -- Mezcla entre el nombre del usuario y anime
    usuario VARCHAR(255) NOT NULL, -- Referencia al id del usuario
    anime VARCHAR(255), -- Referencia al id del anime (si tiene)
    manga VARCHAR(255), -- Referencia al id del manga (si tiene)
    texto TEXT NOT NULL,
    fecha DATE NOT NULL
);