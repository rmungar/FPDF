# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userUi.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(903, 821)
        MainWindow.setMinimumSize(QSize(903, 821))
        MainWindow.setMaximumSize(QSize(903, 821))
        MainWindow.setStyleSheet(u"background-color: rgb(21, 32, 60);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.estudioButton = QPushButton(self.centralwidget)
        self.estudioButton.setObjectName(u"estudioButton")
        self.estudioButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.estudioButton, 7, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(227, 227, 227);")
        self.formLayoutWidget = QWidget(self.widget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(290, 190, 291, 98))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.nombreLabel = QLabel(self.formLayoutWidget)
        self.nombreLabel.setObjectName(u"nombreLabel")
        self.nombreLabel.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"Segoe UI\";")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nombreLabel)

        self.emailLabel = QLabel(self.formLayoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"Segoe UI\";")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.emailLabel)

        self.email = QLabel(self.formLayoutWidget)
        self.email.setObjectName(u"email")
        self.email.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"Segoe UI\";")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.email)

        self.nombre = QLabel(self.formLayoutWidget)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"Segoe UI\";")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nombre)

        self.favoritosLabel = QLabel(self.formLayoutWidget)
        self.favoritosLabel.setObjectName(u"favoritosLabel")
        self.favoritosLabel.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"Segoe UI\";")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.favoritosLabel)

        self.favoritos = QLabel(self.formLayoutWidget)
        self.favoritos.setObjectName(u"favoritos")
        self.favoritos.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"Segoe UI\";")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.favoritos)

        self.userImg = QLabel(self.widget)
        self.userImg.setObjectName(u"userImg")
        self.userImg.setGeometry(QRect(70, 60, 191, 191))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userImg.sizePolicy().hasHeightForWidth())
        self.userImg.setSizePolicy(sizePolicy)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 510, 131, 20))
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"Segoe UI\";")
        self.comentariosList = QListWidget(self.widget)
        self.comentariosList.setObjectName(u"comentariosList")
        self.comentariosList.setGeometry(QRect(30, 540, 701, 192))

        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 3, 2, 18, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 19, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 17, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 20, 1, 1, 1)

        self.mangaButton = QPushButton(self.centralwidget)
        self.mangaButton.setObjectName(u"mangaButton")
        self.mangaButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.mangaButton, 6, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 18, 1, 1, 1)

        self.homeButton = QPushButton(self.centralwidget)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setStyleSheet(u"QPushButton {\n"
"    background: transparent; \n"
"    border: none;\n"
"    color: white; \n"
"	font: 24pt \"Pinky Show\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent; \n"
"}")

        self.gridLayout.addWidget(self.homeButton, 0, 1, 2, 1)

        self.animeButton = QPushButton(self.centralwidget)
        self.animeButton.setObjectName(u"animeButton")
        self.animeButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.animeButton, 5, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 16, 1, 1, 1)

        self.mangakaButton = QPushButton(self.centralwidget)
        self.mangakaButton.setObjectName(u"mangakaButton")
        self.mangakaButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.mangakaButton, 8, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.estudioButton.setText(QCoreApplication.translate("MainWindow", u"Estudios", None))
        self.nombreLabel.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.email.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nombre.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.favoritosLabel.setText(QCoreApplication.translate("MainWindow", u"Favoritos:", None))
        self.favoritos.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.userImg.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Comentarios:", None))
        self.mangaButton.setText(QCoreApplication.translate("MainWindow", u"Mangas", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"ANIGIRI", None))
        self.animeButton.setText(QCoreApplication.translate("MainWindow", u"Animes", None))
        self.mangakaButton.setText(QCoreApplication.translate("MainWindow", u"Mangakas", None))
    # retranslateUi

