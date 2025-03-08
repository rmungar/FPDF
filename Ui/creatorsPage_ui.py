# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'creatorsPage.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

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
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 17, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 18, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 19, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 16, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.mangaButton = QPushButton(self.centralwidget)
        self.mangaButton.setObjectName(u"mangaButton")
        self.mangaButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.mangaButton, 6, 1, 1, 1)

        self.animeButton = QPushButton(self.centralwidget)
        self.animeButton.setObjectName(u"animeButton")
        self.animeButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.animeButton, 5, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.title = QLabel(self.widget)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 100))
        self.title.setMaximumSize(QSize(16777215, 100))
        self.title.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"font: 700 26pt \"Trebuchet MS\";")

        self.gridLayout_2.addWidget(self.title, 1, 3, 1, 2)

        self.biographyvalue = QLabel(self.widget)
        self.biographyvalue.setObjectName(u"biographyvalue")
        self.biographyvalue.setStyleSheet(u"background-color:rgb(227, 227, 227);\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"Segoe UI Symbol\";")
        self.biographyvalue.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_2.addWidget(self.biographyvalue, 2, 3, 1, 1)

        self.obras = QLabel(self.widget)
        self.obras.setObjectName(u"obras")
        self.obras.setStyleSheet(u"background-color:rgb(227, 227, 227);\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"Segoe UI Symbol\";")
        self.obras.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_2.addWidget(self.obras, 3, 3, 1, 1)

        self.placeholderimage = QLabel(self.widget)
        self.placeholderimage.setObjectName(u"placeholderimage")
        self.placeholderimage.setStyleSheet(u"background-color:rgb(227, 227, 227);\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"Segoe UI Symbol\";")

        self.gridLayout_2.addWidget(self.placeholderimage, 2, 4, 2, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 3, 2, 18, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 20, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.userButton = QPushButton(self.centralwidget)
        self.userButton.setObjectName(u"userButton")
        self.userButton.setMinimumSize(QSize(55, 55))
        self.userButton.setStyleSheet(u"QPushButton {\n"
"    border-radius: 25px; \n"
"    background-color: rgb(20, 90, 182); \n"
"    color: white; \n"
"    border: none; \n"
"    font-size: 14px;\n"
"}")
        icon = QIcon(QIcon.fromTheme(u"user-available"))
        self.userButton.setIcon(icon)
        self.userButton.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.userButton, 0, 4, 2, 1)

        self.mangakaButton = QPushButton(self.centralwidget)
        self.mangakaButton.setObjectName(u"mangakaButton")
        self.mangakaButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.mangakaButton, 8, 1, 1, 1)

        self.estudioButton = QPushButton(self.centralwidget)
        self.estudioButton.setObjectName(u"estudioButton")
        self.estudioButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.estudioButton, 7, 1, 1, 1)

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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.mangaButton.setText(QCoreApplication.translate("MainWindow", u"Mangas", None))
        self.animeButton.setText(QCoreApplication.translate("MainWindow", u"Animes", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.biographyvalue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
        self.obras.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
        self.placeholderimage.setText("")
        self.userButton.setText("")
        self.mangakaButton.setText(QCoreApplication.translate("MainWindow", u"Mangakas", None))
        self.estudioButton.setText(QCoreApplication.translate("MainWindow", u"Estudios", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"ANIGIRI", None))
    # retranslateUi

