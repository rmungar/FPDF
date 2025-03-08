import sqlite3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Model.Usuario import Usuario 




class UsuarioRepo():

    def getUsuarios() -> list[Usuario]:
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM USUARIO")
        usuariosDB = cursor.fetchall()
        usuarios = []

        for usuarioDB in usuariosDB:
            usuario = Usuario(usuarioDB[0],usuarioDB[1],usuarioDB[2],usuarioDB[3],usuarioDB[4])
            usuarios.append(usuario)

        return usuarios
    
    def addUsuario(usuario):
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO USUARIO VALUES (?, ?, ?)", (usuario.nombre, usuario.email, usuario.password))
        conn.commit()

    def getUsuario(email) -> Usuario:
        conn = sqlite3.connect('default.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM USUARIO WHERE email = ?", (email,))
        usuarioBD = cursor.fetchone()

        return Usuario(usuarioBD[0], usuarioBD[1], usuarioBD[2], usuarioBD[3], usuarioBD[4], usuarioBD[5], usuarioBD[6], usuarioBD[7])
