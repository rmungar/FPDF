# -*- coding: utf-8 -*-

# prueba@gmail.com
# passwordPrueba


import sys
import os
import random
import pyrebase
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QErrorMessage, QLineEdit, QListWidget, QListWidgetItem, QDialogButtonBox, QVBoxLayout, QDialog, QLabel, QMessageBox
from PyQt6.QtCore import QSize, Qt
from PyQt6 import uic
from PyQt6.QtGui import QIcon, QPixmap, QFont, QBrush, QColor
from Model.Anime import Anime
from Model.Estudio import Estudio
from Model.Manga import Manga
from Model.Mangaka import Mangaka
from Model.Usuario import Usuario
from Model.Comentario import Comentario
from Repository.animeRepo import AnimeRepo
from Repository.estudioRepo import EstudioRepo
from Repository.mangaRepo import MangaRepo
from Repository.mangakaRepo import MangakaRepo
from Repository.usuarioRepo import UsuarioRepo
from Repository.comentarioRepo import ComentarioRepo
from datetime import date

basedir = os.path.dirname(__file__)

config = {
    "apiKey": "AIzaSyB7fn2d5cm8YtiBrelexmoxleAezCNiU9E",
    "authDomain": "anigiri-353a4.firebaseapp.com",
    "projectId": "anigiri-353a4",
    "storageBucket": "anigiri-353a4.firebasestorage.app",
    "databaseURL": "",
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
userLogged = auth.current_user
usuarioFound = False

def getUsuario(email: str, psswd: str) -> Usuario:
    usuarios = UsuarioRepo.getUsuarios()
    for usuario in usuarios:
        if usuario.email == email and usuario.passwd == psswd:
            currentUser = usuario
            usuarioFound = True
    if not usuarioFound:
        raise Exception
    else:
        return currentUser

class LoginScreen(QMainWindow):
    def __init__(self, stacked_widget):

        
        super(LoginScreen, self).__init__()
        uic.loadUi(os.path.join(basedir, 'Ui/login.ui'), self)
        self.setWindowTitle("Anigiri")
        font = QFont()
        font.setPointSize(16)
        self.emailText.setFont(font)
        self.stacked_widget = stacked_widget  # Referencia al `QStackedWidget
        self.loginButton.clicked.connect(self.login)
        self.registerButton.clicked.connect(self.register)


    def login(self):
        email = self.emailText.toPlainText()
        password = self.passwordText.toPlainText()

        try:
            auth.sign_in_with_email_and_password(email, password)  
            currentUser: Usuario = getUsuario(email, password)
            # Cambia a la pantalla de inicio
            homeScreen = HomeScreen(self.stacked_widget, currentUser)
            self.stacked_widget.addWidget(homeScreen)
            self.stacked_widget.setCurrentWidget(homeScreen)
        except:
            QErrorMessage(self).showMessage("Usuario o contraseña incorrectos")

    def register(self):
        email = self.emailText.toPlainText()
        password = self.passwordText.toPlainText()
        usuarioRepo = UsuarioRepo()
        try:
            auth.create_user_with_email_and_password(email, password)
            usuarioRepo.addUsuario(Usuario("",password, email, [], []))
        except:
            QErrorMessage(self).showMessage("Usuario ya registrado")

# Clases para las pantallas que muestran listados

class AllAnimeScreen(QMainWindow):
    def __init__(self, stacked_widget, currentUser: Usuario):
        super(AllAnimeScreen, self).__init__()
        self.currentUser = currentUser
        uic.loadUi(os.path.join(basedir, 'Ui/allTemplate.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget
        self.homeButton.clicked.connect(lambda: self.toHomeScreen())
        self.userButton.clicked.connect(lambda: self.toUserScreen())
        self.animeButton.clicked.connect(lambda: self.toAllAnimePage())
        self.mangaButton.clicked.connect(lambda: self.toAllMangaPage())
        self.mangakaButton.clicked.connect(lambda: self.toAllMangakaPage())
        self.estudioButton.clicked.connect(lambda: self.toAllEstudioPage())
        self.listWidget = self.findChild(QListWidget, "listWidget")  # Asegurar acceso
        

    
        
        animeRepo = AnimeRepo()
        self.animeList = animeRepo.getAnime()

        self.displayAnimeList()

    def displayAnimeList(self):
        """Muestra los animes en el QListWidget"""
        self.listWidget.clear()  # Limpia la lista antes de agregar nuevos elementos

        for anime in self.animeList:
        
            font = QFont()
            font.setPointSize(16)  # Cambia 16 por el tamaño que desees
            item = QListWidgetItem(anime.nombre)  # Asigna el icono y el nombre
            item.setData(1, anime)  # Guarda el objeto para referencia futura
            item.setFont(font)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item.setSizeHint(QSize(100, 100))
            
            self.listWidget.addItem(item)

        print("Número de elementos en listWidget:", self.listWidget.count())

        self.listWidget.update()
        self.listWidget.repaint()

        self.listWidget.itemClicked.connect(self.onAnimeClicked)

    def onAnimeClicked(self, item):
        anime = item.data(1)
        animeScreen = AnimeScreen(self.stacked_widget, anime, self.currentUser)
        self.stacked_widget.addWidget(animeScreen)
        self.stacked_widget.setCurrentWidget(animeScreen)

    def toAllAnimePage(self):
        allAnimePage = AllAnimeScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allAnimePage)
        stacked_widget.setCurrentWidget(allAnimePage) 

    def toAllMangaPage(self):
        allMangaPage = AllMangaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangaPage)
        stacked_widget.setCurrentWidget(allMangaPage)  

    def toAllEstudioPage(self):
        allEstudioPage = AllEstudioScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allEstudioPage)
        stacked_widget.setCurrentWidget(allEstudioPage)  

    def toAllMangakaPage(self):
        allMangakaPage = AllMangakaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangakaPage)
        stacked_widget.setCurrentWidget(allMangakaPage) 

    def toHomeScreen(self):
        stacked_widget.setCurrentIndex(1)

    def toUserScreen(self):
        userScreen = UserScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(userScreen)
        stacked_widget.setCurrentWidget(userScreen)
      
class AllMangaScreen(QMainWindow):
    def __init__(self, stacked_widget, currentUser: Usuario):
        super(AllMangaScreen, self).__init__()
        self.currentUser = currentUser
        uic.loadUi(os.path.join(basedir, 'Ui/allTemplate.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget
        self.homeButton.clicked.connect(lambda: self.toHomeScreen())
        self.userButton.clicked.connect(lambda: self.toUserScreen())
        self.animeButton.clicked.connect(lambda: self.toAllAnimePage())
        self.mangaButton.clicked.connect(lambda: self.toAllMangaPage())
        self.mangakaButton.clicked.connect(lambda: self.toAllMangakaPage())
        self.estudioButton.clicked.connect(lambda: self.toAllEstudioPage())
        self.listWidget = self.findChild(QListWidget, "listWidget")  # Asegurar acceso

        if self.listWidget is None:
            print("Error: listWidget no encontrado en la UI.")
            return  # Evita fallos si el widget no se encuentra
        
        mangaRepo = MangaRepo()
        self.mangaList = mangaRepo.getMangas()

        self.displayMangaList()

    def displayMangaList(self):
        """Muestra los animes en el QListWidget"""
        self.listWidget.clear()  # Limpia la lista antes de agregar nuevos elementos

        for manga in self.mangaList:
            font = QFont()
            font.setPointSize(16)  # Cambia 16 por el tamaño que desees
            item = QListWidgetItem(manga.nombre)  # Asigna el icono y el nombre
            item.setData(1, manga)  # Guarda el objeto para referencia futura
            item.setFont(font)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item.setSizeHint(QSize(100, 100))
            self.listWidget.addItem(item)

        print("Número de elementos en listWidget:", self.listWidget.count())

        self.listWidget.update()
        self.listWidget.repaint()

        self.listWidget.itemClicked.connect(self.onMangaClicked)

    def onMangaClicked(self, item):
        manga = item.data(1)
        mangaScreen = MangaScreen(self.stacked_widget, manga, self.currentUser)
        self.stacked_widget.addWidget(mangaScreen)
        self.stacked_widget.setCurrentWidget(mangaScreen)

    def toAllAnimePage(self):
        allAnimePage = AllAnimeScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allAnimePage)
        stacked_widget.setCurrentWidget(allAnimePage) 

    def toAllMangaPage(self):
        allMangaPage = AllMangaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangaPage)
        stacked_widget.setCurrentWidget(allMangaPage)  

    def toAllEstudioPage(self):
        allEstudioPage = AllEstudioScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allEstudioPage)
        stacked_widget.setCurrentWidget(allEstudioPage)  

    def toAllMangakaPage(self):
        allMangakaPage = AllMangakaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangakaPage)
        stacked_widget.setCurrentWidget(allMangakaPage) 

    def toHomeScreen(self):
        stacked_widget.setCurrentIndex(1)

    def toUserScreen(self):
        userScreen = UserScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(userScreen)
        stacked_widget.setCurrentWidget(userScreen)   

class AllMangakaScreen(QMainWindow):
    def __init__(self, stacked_widget, currentUser: Usuario):
        super(AllMangakaScreen, self).__init__()
        self.currentUser = currentUser
        uic.loadUi(os.path.join(basedir, 'Ui/allTemplate.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget
        self.homeButton.clicked.connect(lambda: self.toHomeScreen())
        self.userButton.clicked.connect(lambda: self.toUserScreen())
        self.animeButton.clicked.connect(lambda: self.toAllAnimePage())
        self.mangaButton.clicked.connect(lambda: self.toAllMangaPage())
        self.mangakaButton.clicked.connect(lambda: self.toAllMangakaPage())
        self.estudioButton.clicked.connect(lambda: self.toAllEstudioPage())
        self.listWidget = self.findChild(QListWidget, "listWidget")  # Asegurar acceso

        if self.listWidget is None:
            print("Error: listWidget no encontrado en la UI.")
            return  # Evita fallos si el widget no se encuentra
        
        mangakaRepo = MangakaRepo()
        self.mangakaList = mangakaRepo.getMangakas()

        self.displayMangakaList()

    def displayMangakaList(self):
        """Muestra los animes en el QListWidget"""
        self.listWidget.clear()  # Limpia la lista antes de agregar nuevos elementos

        for mangaka in self.mangakaList:
            font = QFont()
            font.setPointSize(16)  # Cambia 16 por el tamaño que desees
            item = QListWidgetItem(mangaka.nombre)  # Asigna el icono y el nombre
            item.setData(1, mangaka)  # Guarda el objeto para referencia futura
            item.setFont(font)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item.setSizeHint(QSize(100, 100))
            self.listWidget.addItem(item)

        print("Número de elementos en listWidget:", self.listWidget.count())

        self.listWidget.update()
        self.listWidget.repaint()

        self.listWidget.itemClicked.connect(self.onMangakaClicked)

    def onMangakaClicked(self, item):
        mangaka = item.data(1)
        mangakaScreen = MangakaScreen(self.stacked_widget, mangaka, self.currentUser)
        self.stacked_widget.addWidget(mangakaScreen)
        self.stacked_widget.setCurrentWidget(mangakaScreen)

    def toAllAnimePage(self):
        allAnimePage = AllAnimeScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allAnimePage)
        stacked_widget.setCurrentWidget(allAnimePage) 

    def toAllMangaPage(self):
        allMangaPage = AllMangaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangaPage)
        stacked_widget.setCurrentWidget(allMangaPage)  

    def toAllEstudioPage(self):
        allEstudioPage = AllEstudioScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allEstudioPage)
        stacked_widget.setCurrentWidget(allEstudioPage)  

    def toAllMangakaPage(self):
        allMangakaPage = AllMangakaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangakaPage)
        stacked_widget.setCurrentWidget(allMangakaPage) 

    def toHomeScreen(self):
        stacked_widget.setCurrentIndex(1)

    def toUserScreen(self):
        userScreen = UserScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(userScreen)
        stacked_widget.setCurrentWidget(userScreen)

class AllEstudioScreen(QMainWindow):
    def __init__(self, stacked_widget, currentUser: Usuario):
        super(AllEstudioScreen, self).__init__()
        self.currentUser = currentUser
        uic.loadUi(os.path.join(basedir, 'Ui/allTemplate.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget
        self.homeButton.clicked.connect(lambda: self.toHomeScreen())
        self.userButton.clicked.connect(lambda: self.toUserScreen())
        self.animeButton.clicked.connect(lambda: self.toAllAnimePage())
        self.mangaButton.clicked.connect(lambda: self.toAllMangaPage())
        self.mangakaButton.clicked.connect(lambda: self.toAllMangakaPage())
        self.estudioButton.clicked.connect(lambda: self.toAllEstudioPage())
        self.listWidget = self.findChild(QListWidget, "listWidget")  # Asegurar acceso

        if self.listWidget is None:
            print("Error: listWidget no encontrado en la UI.")
            return  # Evita fallos si el widget no se encuentra
        
        estudioRepo = EstudioRepo()
        self.estudioList = estudioRepo.getEstudios()

        self.displayEstudioList()

    def displayEstudioList(self):
        """Muestra los animes en el QListWidget"""
        self.listWidget.clear()  # Limpia la lista antes de agregar nuevos elementos

        for estudio in self.estudioList:
            font = QFont()
            font.setPointSize(16)  # Cambia 16 por el tamaño que desees
            item = QListWidgetItem(estudio.nombre)  # Asigna el icono y el nombre
            item.setData(1, estudio)  # Guarda el objeto para referencia futura
            item.setFont(font)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item.setSizeHint(QSize(100, 100))
            self.listWidget.addItem(item)

        print("Número de elementos en listWidget:", self.listWidget.count())

        self.listWidget.update()
        self.listWidget.repaint()

        self.listWidget.itemClicked.connect(self.onEstudioClicked)

    def onEstudioClicked(self, item):
        estudio = item.data(1)
        estudioScreen = EstudioScreen(self.stacked_widget, estudio, self.currentUser)
        self.stacked_widget.addWidget(estudioScreen)
        self.stacked_widget.setCurrentWidget(estudioScreen)
    def toAllAnimePage(self):
        allAnimePage = AllAnimeScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allAnimePage)
        stacked_widget.setCurrentWidget(allAnimePage) 

    def toAllMangaPage(self):
        allMangaPage = AllMangaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangaPage)
        stacked_widget.setCurrentWidget(allMangaPage)  

    def toAllEstudioPage(self):
        allEstudioPage = AllEstudioScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allEstudioPage)
        stacked_widget.setCurrentWidget(allEstudioPage)  

    def toAllMangakaPage(self):
        allMangakaPage = AllMangakaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangakaPage)
        stacked_widget.setCurrentWidget(allMangakaPage) 

    def toHomeScreen(self):
        home_Screen = HomeScreen(stacked_widget, self.currentUser)
        stacked_widget.addWidget(home_Screen)
        stacked_widget.setCurrentWidget(home_Screen)
        
    def toHomeScreen(self):
        home_Screen = HomeScreen(stacked_widget, self.currentUser)
        stacked_widget.addWidget(home_Screen)
        stacked_widget.setCurrentWidget(home_Screen)

    def toHomeScreen(self):
        self.stacked_widget.setCurrentIndex(1) 

    def toUserScreen(self):
        userScreen = UserScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(userScreen)
        stacked_widget.setCurrentWidget(userScreen)

class MangaScreen(QMainWindow):
    def __init__(self, stacked_widget, manga: Manga, currentUser: Usuario):
        super(MangaScreen, self).__init__()
        self.currentUser = currentUser
        uic.loadUi(os.path.join(basedir, 'Ui/contentPage.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget
        
        self.homeButton.clicked.connect(lambda: self.toHomeScreen())
        self.userButton.clicked.connect(lambda: self.toUserScreen())
        self.animeButton.clicked.connect(lambda: self.toAllAnimePage())
        self.mangaButton.clicked.connect(lambda: self.toAllMangaPage())
        self.mangakaButton.clicked.connect(lambda: self.toAllMangakaPage())
        self.estudioButton.clicked.connect(lambda: self.toAllEstudioPage())

        if manga is not None:  
            self.favoriteButton.clicked.connect(lambda: self.addFav(currentUser, manga)) 
            self.commentButton.clicked.connect(lambda: self.abrir_formulario(manga, currentUser))
            self.title.setText(manga.nombre)
            self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.synopsis.setText(manga.sinopsis)
            self.placeholderimage.setPixmap(
                QPixmap(os.path.join(basedir, manga.imagen)).scaled(242, 305, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)  # Ajusta el tamaño
            )
            self.homeButton.clicked.connect(lambda: self.toHomeScreen())
            self.rankingLabel.setText("RANKING DE MANGAS")
            self.rankingLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.updateRanking()
            self.descripcion.setText(f"· Géneros: {manga.genero}\n· Volúmenes: {manga.tomos}\n· Capítulos: {manga.capitulos}\n· Mangaka: {manga.autor}")            
            self.updateComentarios(manga)
            self.comments.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        else:
            self.title.setText("Sin información")
            self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.synopsis.setText("No se ha seleccionado un manga.")
            self.synopsis.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.placeholderimage.clear()  # Limpia la imagen
            self.descripcion.setText("Información no disponible.")
            self.descripcion.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.comments.setText("COMENTARIOS")
            self.comments.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.rankingLabel.setText("RANKING DE ANIMES")
            self.rankingLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)


    def addFav(self, usuario: Usuario, manga: Manga):
        usuario.updateFavoritos(manga)
        self.mostrar_notificacion("Favoritos actualizados")
        


    def updateRanking(self):
        cont = 1
        mangaRepo= MangaRepo()
        mangaList = mangaRepo.getMangas()
        for manga in mangaList:
            item = QListWidgetItem(f"{cont} - {manga.nombre}")
            font = QFont()  # Crear un objeto de tipo QFont
            font.setPointSize(12)  # Aumentar el tamaño de la fuente (ajusta el número según lo que necesites)
            item.setFont(font)
            item.setForeground(QBrush(QColor(0, 0, 0)))
            self.ranking.addItem(item)
            cont += 1

    def abrir_formulario(self, manga:Manga, usuario:Usuario):
        dialogo = FormularioEmergente()
        resultado = dialogo.exec()  # Ejecuta la ventana emergente

        if resultado == 1:
            datos = dialogo.obtener_datos()

            comentarioRepo = ComentarioRepo()
            comentarioRepo.addComentarioToAnime(
                Comentario(
                    f"M-{manga.nombre}-{usuario.nombre}",
                    usuario.email,
                    datos["Comentario"],
                    f"{date.today()}"
                )   
            )
            self.updateComentarios(manga)
            self.mostrar_notificacion("Comentario añadido")
    

    def mostrar_notificacion(self, mensaje):
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Notificación")
        msg.setText(mensaje)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()


    def updateComentarios(self, manga: Manga):
        text = "COMENTARIOS\n"
        comentarioRepo = ComentarioRepo()
        comments: list[Comentario] = comentarioRepo.getComentarios()
        for comentario in comments:
            if comentario._id.split("-")[0] == "M" and comentario._id.split("-")[1] == manga.nombre:
                text += "{}: {}\n".format(comentario.usuario.split("@")[0], comentario.texto)
        self.comments.setText(text)

    def toAllAnimePage(self):
        allAnimePage = AllAnimeScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allAnimePage)
        stacked_widget.setCurrentWidget(allAnimePage) 

    def toAllMangaPage(self):
        allMangaPage = AllMangaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangaPage)
        stacked_widget.setCurrentWidget(allMangaPage)  

    def toAllEstudioPage(self):
        allEstudioPage = AllEstudioScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allEstudioPage)
        stacked_widget.setCurrentWidget(allEstudioPage)  

    def toAllMangakaPage(self):
        allMangakaPage = AllMangakaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangakaPage)
        stacked_widget.setCurrentWidget(allMangakaPage) 

    def toHomeScreen(self):
        home_Screen = HomeScreen(stacked_widget, self.currentUser)
        stacked_widget.addWidget(home_Screen)
        stacked_widget.setCurrentWidget(home_Screen)

    def toHomeScreen(self):
        stacked_widget.setCurrentIndex(1)

    def toUserScreen(self):
        userScreen = UserScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(userScreen)
        stacked_widget.setCurrentWidget(userScreen)

class AnimeScreen(QMainWindow):
    def __init__(self, stacked_widget, anime: Anime, currentUser: Usuario):
        super(AnimeScreen, self).__init__()
        self.currentUser = currentUser
        uic.loadUi(os.path.join(basedir, 'Ui/contentPage.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget
        self.homeButton.clicked.connect(lambda: self.toHomeScreen())
        self.userButton.clicked.connect(lambda: self.toUserScreen())
        self.animeButton.clicked.connect(lambda: self.toAllAnimePage())
        self.mangaButton.clicked.connect(lambda: self.toAllMangaPage())
        self.mangakaButton.clicked.connect(lambda: self.toAllMangakaPage())
        self.estudioButton.clicked.connect(lambda: self.toAllEstudioPage())
        
        if anime is not None:
            self.favoriteButton.clicked.connect(lambda: self.addFav(currentUser, anime)) 
            self.commentButton.clicked.connect(lambda: self.abrir_formulario(anime, currentUser))
            self.title.setText(anime.nombre)
            self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.synopsis.setText(anime.sinopsis)
            self.placeholderimage.setPixmap(
                QPixmap(os.path.join(basedir, anime.imagen)).scaled(242, 305, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
            )
            self.descripcion.setText(f"· Géneros: {anime.genero}\n· Temporadas: {anime.temporadas}\n· Capítulos: {anime.capitulos}\n· Estudio: {anime.estudio}")
            self.updateComentarios(anime)
            self.comments.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.updateRanking()
            self.rankingLabel.setText("RANKING DE ANIMES")
            self.rankingLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        else:
            self.title.setText("Sin información")
            self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.synopsis.setText("No se ha seleccionado un manga.")
            self.descripcion.setText("Información no disponible.")
            self.placeholderimage.clear()
            self.information.setText("Información no disponible.")
            self.comments.setText("COMENTARIOS")
            self.comments.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.rankingLabel.setText("RANKING DE ANIMES")
            self.rankingLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)

    def addFav(self, usuario: Usuario, anime: Anime):
        usuario.updateFavoritos(anime)
        self.mostrar_notificacion("Favoritos Actualizados")

    def abrir_formulario(self, anime:Anime, usuario:Usuario):
        dialogo = FormularioEmergente()
        resultado = dialogo.exec()  # Ejecuta la ventana emergente

        if resultado == 1:
            datos = dialogo.obtener_datos()

            comentarioRepo = ComentarioRepo()
            comentarioRepo.addComentarioToAnime(
                Comentario(
                    f"A-{anime.nombre}-{usuario.nombre}",
                    usuario.email,
                    datos["Comentario"],
                    f"{date.today()}"
                )   
            )
            self.updateComentarios(anime)
            self.mostrar_notificacion("Comentario añadido")

    def updateComentarios(self, anime: Anime):
        text = "COMENTARIOS\n"
        comentarioRepo = ComentarioRepo()
        comments: list[Comentario] = comentarioRepo.getComentarios()
        for comentario in comments:
            if comentario._id.split("-")[0] == "A" and comentario._id.split("-")[1] == anime.nombre:
                text += "{}: {}\n".format(comentario.usuario.split("@")[0], comentario.texto)
        self.comments.setText(text)
            
    def mostrar_notificacion(self, mensaje):
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Notificación")
        msg.setText(mensaje)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def updateRanking(self):
        cont = 1
        animeRepo = MangaRepo()
        animeList = animeRepo.getMangas()
        for anime in animeList:
            item = QListWidgetItem(f"{cont} - {anime.nombre}")
            font = QFont()  # Crear un objeto de tipo QFont
            font.setPointSize(12)  # Aumentar el tamaño de la fuente (ajusta el número según lo que necesites)
            item.setFont(font)
            item.setForeground(QBrush(QColor(0, 0, 0)))
            self.ranking.addItem(item)
            cont += 1

    def toAllAnimePage(self):
        allAnimePage = AllAnimeScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allAnimePage)
        stacked_widget.setCurrentWidget(allAnimePage) 

    def toAllMangaPage(self):
        allMangaPage = AllMangaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangaPage)
        stacked_widget.setCurrentWidget(allMangaPage)  

    def toAllEstudioPage(self):
        allEstudioPage = AllEstudioScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allEstudioPage)
        stacked_widget.setCurrentWidget(allEstudioPage)  

    def toAllMangakaPage(self):
        allMangakaPage = AllMangakaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangakaPage)
        stacked_widget.setCurrentWidget(allMangakaPage) 

    def toHomeScreen(self):
        stacked_widget.setCurrentIndex(1)

    def toUserScreen(self):
        userScreen = UserScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(userScreen)
        stacked_widget.setCurrentWidget(userScreen)
    
class MangakaScreen(QMainWindow):
    def __init__(self, stacked_widget, mangaka: Mangaka, currentUser: Usuario):
        super(MangakaScreen, self).__init__()
        self.currentUser = currentUser
        uic.loadUi(os.path.join(basedir, 'Ui/creatorsPage.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget
        self.homeButton.clicked.connect(lambda: self.toHomeScreen())
        self.userButton.clicked.connect(lambda: self.toUserScreen())
        self.animeButton.clicked.connect(lambda: self.toAllAnimePage())
        self.mangaButton.clicked.connect(lambda: self.toAllMangaPage())
        self.mangakaButton.clicked.connect(lambda: self.toAllMangakaPage())
        self.estudioButton.clicked.connect(lambda: self.toAllEstudioPage())

        if mangaka is not None:
            self.title.setText(mangaka.nombre)
            self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.biographyvalue.setText(f"· Nacimiento: {mangaka.nacimiento}\n· Nacionalidad: {mangaka.nacionalidad}")
            self.placeholderimage.setPixmap(
                QPixmap(os.path.join(basedir, mangaka.imagen)).scaled(300, 400, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)  # Ajusta el tamaño
            )
            self.obras.setText(f"Obras: {mangaka.obras}")
        else:
            self.title.setText("Sin información")
            self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.biographyvalue.setText("No se ha seleccionado un mangaka.")
            self.biographyvalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.placeholderimage.clear()  # Limpia la imagen
            self.obras.setText("Información no disponible.")
            self.obras.setAlignment(Qt.AlignmentFlag.AlignCenter)


    def toAllAnimePage(self):
        allAnimePage = AllAnimeScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allAnimePage)
        stacked_widget.setCurrentWidget(allAnimePage) 

    def toAllMangaPage(self):
        allMangaPage = AllMangaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangaPage)
        stacked_widget.setCurrentWidget(allMangaPage)  

    def toAllEstudioPage(self):
        allEstudioPage = AllEstudioScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allEstudioPage)
        stacked_widget.setCurrentWidget(allEstudioPage)  

    def toAllMangakaPage(self):
        allMangakaPage = AllMangakaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangakaPage)
        stacked_widget.setCurrentWidget(allMangakaPage) 

    def toHomeScreen(self):
        stacked_widget.setCurrentIndex(1)

    def toUserScreen(self):
        userScreen = UserScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(userScreen)
        stacked_widget.setCurrentWidget(userScreen)

class EstudioScreen(QMainWindow):

    def __init__(self, stacked_widget, estudio: Estudio, currentUser: Usuario):
        super(EstudioScreen, self).__init__()
        self.currentUser = currentUser
        uic.loadUi(os.path.join(basedir, 'Ui/creatorsPage.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget
        self.homeButton.clicked.connect(lambda: self.toHomeScreen())
        self.userButton.clicked.connect(lambda: self.toUserScreen())
        self.animeButton.clicked.connect(lambda: self.toAllAnimePage())
        self.mangaButton.clicked.connect(lambda: self.toAllMangaPage())
        self.mangakaButton.clicked.connect(lambda: self.toAllMangakaPage())
        self.estudioButton.clicked.connect(lambda: self.toAllEstudioPage())

        if estudio is not None:
            self.title.setText(estudio.nombre)
            self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.biographyvalue.setText(f"· País: {estudio.pais}")
            self.placeholderimage.setPixmap(QPixmap(os.path.join(basedir, estudio.imagen)).scaled(300, 400, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))  # Ajusta el tamaño
            self.obras.setText(f"Animes: {estudio.animes}")
        else:
            self.title.setText("Sin información")
            self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.biographyvalue.setText("No se ha seleccionado un estudio.")
            self.biographyvalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.placeholderimage.clear()  # Limpia la imagen
            self.obras.setText("Información no disponible.")
            self.obras.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def toAllAnimePage(self):
        allAnimePage = AllAnimeScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allAnimePage)
        stacked_widget.setCurrentWidget(allAnimePage) 

    def toAllMangaPage(self):
        allMangaPage = AllMangaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangaPage)
        stacked_widget.setCurrentWidget(allMangaPage)  

    def toAllEstudioPage(self):
        allEstudioPage = AllEstudioScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allEstudioPage)
        stacked_widget.setCurrentWidget(allEstudioPage)  

    def toAllMangakaPage(self):
        allMangakaPage = AllMangakaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangakaPage)
        stacked_widget.setCurrentWidget(allMangakaPage) 

    def toHomeScreen(self):
        stacked_widget.setCurrentIndex(1)

    def toUserScreen(self):
        userScreen = UserScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(userScreen)
        stacked_widget.setCurrentWidget(userScreen)

class UserScreen(QMainWindow):

    def __init__(self, stacked_widget, usuario: Usuario):
        super(UserScreen, self).__init__()
        self.currentUser = usuario
        uic.loadUi(os.path.join(basedir, 'Ui/userUi.ui'), self)
        self.setWindowTitle("Anigiri")
        self.homeButton.clicked.connect(lambda: self.toHomeScreen())
        self.animeButton.clicked.connect(lambda: self.toAllAnimePage())
        self.mangaButton.clicked.connect(lambda: self.toAllMangaPage())
        self.mangakaButton.clicked.connect(lambda: self.toAllMangakaPage())
        self.estudioButton.clicked.connect(lambda: self.toAllEstudioPage())
        self.stacked_widget = stacked_widget

        if usuario is not None:
            self.setComentarios(usuario)
            self.nombre.setText(usuario.nombre)
            self.email.setText(usuario.email)
            self.favoritos.setText(f"{len(usuario.favoritos)}")
            ruta_imagen = os.path.join(basedir, "Resources/User/userImage.png")
            pixmap = QPixmap(ruta_imagen)
            self.userImg.setPixmap(QPixmap(pixmap).scaled(191,191, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation))
        else:
            self.nombre.setText("Sin información")
            self.email.setText("Sin información")


    def setComentarios(self, usuario: Usuario):
        comentarioRepo = ComentarioRepo()
        comments = comentarioRepo.getComentariosByUser(usuario)

        self.comentariosList.clear()  # Limpiar lista antes de agregar nuevos comentarios

        for comentario in comments:
            # Formatear el texto del comentario
            texto_comentario = f"{comentario.fecha} - {comentario._id.split('-')[1]}: {comentario.texto}"

            # Crear el item y añadirlo al QListWidget
            item = QListWidgetItem(texto_comentario)
            font = QFont()  # Crear un objeto de tipo QFont
            font.setPointSize(12)  # Aumentar el tamaño de la fuente (ajusta el número según lo que necesites)
            item.setFont(font)
            item.setForeground(QBrush(QColor(0, 0, 0)))
            self.comentariosList.addItem(item)


    def toAllAnimePage(self):
        allAnimePage = AllAnimeScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allAnimePage)
        stacked_widget.setCurrentWidget(allAnimePage) 

    def toAllMangaPage(self):
        allMangaPage = AllMangaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangaPage)
        stacked_widget.setCurrentWidget(allMangaPage)  

    def toAllEstudioPage(self):
        allEstudioPage = AllEstudioScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allEstudioPage)
        stacked_widget.setCurrentWidget(allEstudioPage)  

    def toAllMangakaPage(self):
        allMangakaPage = AllMangakaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangakaPage)
        stacked_widget.setCurrentWidget(allMangakaPage) 

    def toHomeScreen(self):
        stacked_widget.setCurrentIndex(1)

class HomeScreen(QMainWindow):
    def __init__(self, stacked_widget, currentUser: Usuario):
        super(HomeScreen, self).__init__()
        self.currentUser = currentUser
        self.login_screen = LoginScreen(stacked_widget)

        uic.loadUi(os.path.join(basedir, 'Ui/homePage.ui'), self)
        self.setWindowTitle("Anigiri")
        self.stacked_widget = stacked_widget
        self.userButton.clicked.connect(lambda: self.toUserScreen())
        self.animeButton.clicked.connect(lambda: self.toAllAnimePage())
        self.mangaButton.clicked.connect(lambda: self.toAllMangaPage())
        self.mangakaButton.clicked.connect(lambda: self.toAllMangakaPage())
        self.estudioButton.clicked.connect(lambda: self.toAllEstudioPage())

        usuarioRepo = UsuarioRepo()
        mangaRepo = MangaRepo()
        animeRepo = AnimeRepo()
        mangakaRepo = MangakaRepo()
        estudioRepo = EstudioRepo()

        # Obtener listas de datos
        self.animeList = animeRepo.getAnime()
        self.mangaList = mangaRepo.getMangas()
        self.mangakaList = mangakaRepo.getMangakas()
        self.estudioList = estudioRepo.getEstudios()

        # Índices para rastrear la posición de cada imagen
        self.anime_indices = [0, 1, 2]  # [izquierda (top2), centro (top1), derecha (top3)]
        self.manga_indices = [0, 1, 2]
        self.mangaka_indices = [0, 1, 2]
        self.estudio_indices = [0, 1, 2]

        # Configurar imágenes en UI
        self.setImagenes(self.animeTop1, self.animeTop2, self.animeTop3, 
                         self.anime_indices, self.animeList, self.toAnimePage)

        self.setImagenes(self.mangaTop1, self.mangaTop2, self.mangaTop3, 
                         self.manga_indices, self.mangaList, self.toMangaPage)

        self.setImagenes(self.mangakaTop1, self.mangakaTop2, self.mangakaTop3, 
                         self.mangaka_indices, self.mangakaList, self.toMangakaPage)

        self.setImagenes(self.estudiosTop1, self.estudiosTop2, self.estudiosTop3, 
                         self.estudio_indices, self.estudioList, self.toEstudioPage)

    def configurarBoton(self, boton, imagen):
        """Configura un botón con la imagen proporcionada"""
        boton.setText("")
        boton.setStyleSheet("background: transparent; border: none;")
        boton.setIcon(QIcon(imagen))
        boton.setIconSize(QSize(370, 400))

    def setImagenes(self, btn_centro, btn_izq, btn_der, indices, lista, funcion_navegar):
        """Configura los botones de imágenes con sus eventos de navegación y rotación"""
        self.configurarBoton(btn_centro, os.path.join(basedir, lista[indices[1]].imagen))  # Centro (top1)
        self.configurarBoton(btn_izq, os.path.join(basedir, lista[indices[0]].imagen))  # Izquierda (top2)
        self.configurarBoton(btn_der, os.path.join(basedir, lista[indices[2]].imagen))  # Derecha (top3)

        # Asignar navegación correcta al botón central
        
        btn_centro.clicked.connect(lambda: funcion_navegar(lista[indices[1]]))  # top1 lleva a la info correcta

        # Asignar eventos de rotación
        
        btn_izq.clicked.connect(lambda: self.moverImagen(indices, lista, btn_centro, btn_izq, btn_der, funcion_navegar, -1))

        
        btn_der.clicked.connect(lambda: self.moverImagen(indices, lista, btn_centro, btn_izq, btn_der, funcion_navegar, 1))

    def moverImagen(self, indices, lista, btn_centro, btn_izq, btn_der, funcion_navegar, direccion):
        """Rota las imágenes manteniendo la disposición correcta"""
        if direccion == 1:  # Si se presiona top3
            indices[:] = [indices[1], indices[2], indices[0]]  # top3 → top1, top2 → top3, top1 → top2
        elif direccion == -1:  # Si se presiona top2
            indices[:] = [indices[2], indices[0], indices[1]]  # top2 → top1, top1 → top3, top3 → top2

        # Actualizar imágenes en los botones
        self.configurarBoton(btn_centro, os.path.join(basedir, lista[indices[1]].imagen))  # Centro (top1)
        self.configurarBoton(btn_izq, os.path.join(basedir, lista[indices[0]].imagen))  # Izquierda (top2)
        self.configurarBoton(btn_der, os.path.join(basedir, lista[indices[2]].imagen))  # Derecha (top3)

        # Actualizar el evento del botón central para que lleve a la página correcta
        
        btn_centro.clicked.connect(lambda: funcion_navegar(lista[indices[1]]))  # Siempre top1 lleva a la página correcta

    def toMangaPage(self, manga: Manga):
        manga_screen = MangaScreen(stacked_widget, manga, self.currentUser)
        stacked_widget.addWidget(manga_screen)
        stacked_widget.setCurrentWidget(manga_screen)   

    def toAnimePage(self, anime: Anime):
        """Actualiza AnimeScreen y cambia de ventana"""
        animeScreen = AnimeScreen(self.stacked_widget, anime, self.currentUser)
        stacked_widget.addWidget(animeScreen)
        stacked_widget.setCurrentWidget(animeScreen)   
    
    def toMangakaPage(self, mangaka: Mangaka):  
        """Actualiza MangakaScreen y cambia de ventana"""
        mangakaScreen = MangakaScreen(self.stacked_widget, mangaka, self.currentUser)
        stacked_widget.addWidget(mangakaScreen)
        stacked_widget.setCurrentWidget(mangakaScreen)   

    def toEstudioPage(self, estudio: Estudio):
        """Actualiza EstudioScreen y cambia de ventana"""
        estudioScreen = EstudioScreen(self.stacked_widget, estudio, self.currentUser)
        stacked_widget.addWidget(estudioScreen)
        stacked_widget.setCurrentWidget(estudioScreen)   

    def toAllAnimePage(self):
        allAnimePage = AllAnimeScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allAnimePage)
        stacked_widget.setCurrentWidget(allAnimePage) 

    def toAllMangaPage(self):
        allMangaPage = AllMangaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangaPage)
        stacked_widget.setCurrentWidget(allMangaPage)  

    def toAllEstudioPage(self):
        allEstudioPage = AllEstudioScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allEstudioPage)
        stacked_widget.setCurrentWidget(allEstudioPage)  

    def toAllMangakaPage(self):
        allMangakaPage = AllMangakaScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(allMangakaPage)
        stacked_widget.setCurrentWidget(allMangakaPage)  

    def toUserScreen(self):
        userScreen = UserScreen(self.stacked_widget, self.currentUser)
        stacked_widget.addWidget(userScreen)
        stacked_widget.setCurrentWidget(userScreen)    

class FormularioEmergente(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Añadir un comentario")
        self.setGeometry(100, 100, 300, 200)

        # Layout principal
        layout = QVBoxLayout()
        self.comentario_input = QLineEdit(self)
        self.comentario_input.setPlaceholderText("Comentario")
        layout.addWidget(QLabel("Comentar"))
        layout.addWidget(self.comentario_input)

        # Botones de Aceptar y Cancelar
        botones = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, 
            self
        )
        botones.accepted.connect(self.accept)  # Cierra el diálogo y retorna `QDialog.Accepted`
        botones.rejected.connect(self.reject)  # Cierra el diálogo y retorna `QDialog.Rejected`
        layout.addWidget(botones)

        self.setLayout(layout)

    def obtener_datos(self):
        return {
            "Comentario": self.comentario_input.text(),
        }

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Crear el QStackedWidget
    stacked_widget = QStackedWidget()
    loginScreen = LoginScreen(stacked_widget)
    # Iniciar en la pantalla de Login
    stacked_widget.addWidget(loginScreen)
    stacked_widget.setCurrentIndex(0)
    stacked_widget.show()

    app.exec()
