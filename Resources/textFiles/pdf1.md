# Estructura de la Base de Datos

A continuación se describe la estructura de la base de datos utilizada para la aplicación, con sus respectivas tablas y campos.

## Tabla: USUARIO

Esta tabla almacena la información de los usuarios registrados en la plataforma.

| Campo       | Tipo                  | Descripción                                          |
|-------------|-----------------------|------------------------------------------------------|
| nombre      | VARCHAR(255) NOT NULL | Nombre del usuario (clave primaria).                 |
| passwd      | VARCHAR(255) NOT NULL | Contraseña del usuario.                              |
| email       | VARCHAR(255) NOT NULL | Correo electrónico del usuario.                      |
| comentarios | JSON                  | Almacena los comentarios del usuario en formato JSON.|
| favoritos   | JSON                  | Almacena los favoritos del usuario en formato JSON.  |

### Campos:
- **nombre**: Nombre del usuario (clave primaria).
- **passwd**: Contraseña del usuario.
- **email**: Correo electrónico del usuario.
- **comentarios**: Almacena los comentarios en formato JSON.
- **favoritos**: Almacena los favoritos del usuario en formato JSON.
---

## Tabla: MANGA

Esta tabla contiene la información relacionada con los mangas disponibles en la plataforma.

| Campo      | Tipo                  | Descripción                                          |
|------------|-----------------------|------------------------------------------------------|
| _id        | VARCHAR(255) PRIMARY KEY | Identificador único del manga.                    |
| nombre     | VARCHAR(255) NOT NULL | Nombre del manga.                                    |
| sinopsis   | VARCHAR(255) NOT NULL | Sinopsis breve del manga.                            |
| genero     | VARCHAR(255) NOT NULL | Género del manga.                                    |
| autor      | VARCHAR(255) NOT NULL | Autor del manga.                                     |
| imagen     | VARCHAR(255) NOT NULL | URL de la imagen del manga.                          |
| tomos      | INTEGER NOT NULL      | Número de tomos del manga.                           |
| capitulos  | INTEGER NOT NULL      | Número de capítulos del manga.                       |
| comentarios| TEXT                  | Comentarios sobre el manga.                          |

### Campos:
- **_id**: Identificador único del manga.
- **nombre**: Nombre del manga.
- **sinopsis**: Sinopsis breve del manga.
- **genero**: Género del manga.
- **autor**: Autor del manga.
- **imagen**: URL de la imagen del manga.
- **tomos**: Número de tomos del manga.
- **capitulos**: Número de capítulos del manga.
- **comentarios**: Comentarios sobre el manga.
---

## Tabla: ANIME

Esta tabla contiene la información relacionada con los animes disponibles en la plataforma.

| Campo      | Tipo                     | Descripción                                      |
|------------|--------------------------|--------------------------------------------------|
| _id        | VARCHAR(255) PRIMARY KEY | Identificador único del anime.                   |
| nombre     | VARCHAR(255) NOT NULL    | Nombre del anime.                                |
| sinopsis   | TEXT NOT NULL            | Sinopsis detallada del anime.                    |
| genero     | VARCHAR(255) NOT NULL    | Género del anime.                                |
| estudio    | VARCHAR(255) NOT NULL    | Estudio de animación que produjo el anime.       |
| imagen     | VARCHAR(255) NOT NULL    | URL de la imagen del anime.                      |
| temporadas | INTEGER NOT NULL         | Número de temporadas del anime.                  |
| capitulos  | INTEGER NOT NULL         | Número de capítulos del anime.                   |
| comentarios| JSON                     | Comentarios sobre el anime en formato JSON.      |

### Campos:
- **_id**: Identificador único del anime.
- **nombre**: Nombre del anime.
- **sinopsis**: Sinopsis detallada del anime.
- **genero**: Género del anime.
- **estudio**: Estudio de animación que produjo el anime.
- **imagen**: URL de la imagen del anime.
- **temporadas**: Número de temporadas del anime.
- **capitulos**: Número de capítulos del anime.
- **comentarios**: Comentarios sobre el anime en formato JSON.
---

## Tabla: MANGAKA

Esta tabla contiene la información de los autores de manga.

| Campo      | Tipo                     | Descripción                                         |
|------------|--------------------------|-----------------------------------------------------|
| _id        | VARCHAR(255) PRIMARY KEY | Identificador único del mangaka.                    |
| nombre     | VARCHAR(255) NOT NULL    | Nombre del mangaka.                                 |
| nacimiento | DATE NOT NULL            | Fecha de nacimiento del mangaka.                    |
| nacionalidad | VARCHAR(255) NOT NULL  | Nacionalidad del mangaka.                           |
| imagen     | VARCHAR(255) NOT NULL    | URL de la imagen del mangaka.                       |
| obras      | JSON                     | Lista de obras del mangaka en formato JSON.         |

### Campos:
- **_id**: Identificador único del mangaka.
- **nombre**: Nombre del mangaka.
- **nacimiento**: Fecha de nacimiento del mangaka.
- **nacionalidad**: Nacionalidad del mangaka.
- **imagen**: URL de la imagen del mangaka.
- **obras**: Lista de obras del mangaka en formato JSON.
---

## Tabla: ESTUDIO

Esta tabla contiene la información de los estudios de animación.

| Campo      | Tipo                | Descripción                                           |
|------------|---------------------|-------------------------------------------------------|
| nombre     | VARCHAR(255) PRIMARY KEY | Nombre del estudio de animación.                   |
| pais       | VARCHAR(255) NOT NULL | País de origen del estudio.                          |
| imagen     | VARCHAR(255) NOT NULL | URL de la imagen del estudio.                        |
| animes     | JSON                 | Lista de animes producidos por el estudio en formato JSON. |

### Campos:
- **nombre**: Nombre del estudio de animación.
- **pais**: País de origen del estudio.
- **imagen**: URL de la imagen del estudio.
- **animes**: Lista de animes producidos por el estudio en formato JSON.
---

## Tabla: COMENTARIO

Esta tabla almacena los comentarios realizados por los usuarios sobre mangas, animes u otros contenidos.

| Campo      | Tipo                | Descripción                                           |
|------------|---------------------|-------------------------------------------------------|
| _id        | VARCHAR(255) PRIMARY KEY | Identificador único del comentario.                |
| usuario    | VARCHAR(255) NOT NULL | Nombre del usuario que realiza el comentario.         |
| texto      | TEXT NOT NULL        | El contenido del comentario.                          |
| fecha      | VARCHAR(255) NOT NULL | Fecha en que el comentario fue realizado.             |



### Campos:
- **_id**: Identificador único del comentario.
- **usuario**: Nombre del usuario que realiza el comentario.
- **texto**: El contenido del comentario.
- **fecha**: Fecha en que el comentario fue realizado.

---
