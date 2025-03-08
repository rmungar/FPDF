# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1065, 583)
        MainWindow.setStyleSheet(u"background-color: rgb(21, 32, 60);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 4, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_9, 4, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_6, 6, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_8, 4, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_7, 3, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 5, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 4, 4, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 8, 2, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.email = QLabel(self.centralwidget)
        self.email.setObjectName(u"email")
        self.email.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.email, 1, 0, 1, 1)

        self.Pregunta = QLabel(self.centralwidget)
        self.Pregunta.setObjectName(u"Pregunta")
        self.Pregunta.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.Pregunta, 10, 1, 1, 1)

        self.VisiblePass = QCheckBox(self.centralwidget)
        self.VisiblePass.setObjectName(u"VisiblePass")
        self.VisiblePass.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.VisiblePass, 10, 0, 1, 1)

        self.passwordText = QTextEdit(self.centralwidget)
        self.passwordText.setObjectName(u"passwordText")
        self.passwordText.setMaximumSize(QSize(16777215, 36))
        self.passwordText.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.passwordText.setFrameShape(QFrame.Shape.StyledPanel)
        self.passwordText.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.passwordText.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.gridLayout.addWidget(self.passwordText, 9, 0, 1, 2)

        self.password_2 = QLabel(self.centralwidget)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.password_2, 7, 0, 1, 2)

        self.emailText = QTextEdit(self.centralwidget)
        self.emailText.setObjectName(u"emailText")
        self.emailText.setMaximumSize(QSize(16777215, 36))
        self.emailText.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.emailText.setAutoFillBackground(True)
        self.emailText.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 16pt;\n"
"color: rgb(0, 0, 0);")
        self.emailText.setFrameShape(QFrame.Shape.StyledPanel)
        self.emailText.setFrameShadow(QFrame.Shadow.Sunken)
        self.emailText.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.emailText.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.gridLayout.addWidget(self.emailText, 2, 0, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 6, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout, 4, 2, 1, 1)

        self.Title = QLabel(self.centralwidget)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setFamilies([u"Pinky Show"])
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.Title.setFont(font)
        self.Title.setStyleSheet(u"font: 24pt \"Pinky Show\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.Title, 2, 2, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_10, 0, 3, 1, 1)

        self.loginButton = QPushButton(self.centralwidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(200, 50))
        self.loginButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Segoe UI\";\n"
"color: rgb(36, 61, 95);")

        self.gridLayout_4.addWidget(self.loginButton, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)

        self.registerButton = QPushButton(self.centralwidget)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setMinimumSize(QSize(200, 50))
        self.registerButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Segoe UI\";\n"
"color: rgb(36, 61, 95);")

        self.gridLayout_4.addWidget(self.registerButton, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 1, 3, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 7, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.Pregunta.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">\u00bfA\u00fan no tienes cuenta? Reg\u00edstrate</p></body></html>", None))
        self.VisiblePass.setText(QCoreApplication.translate("MainWindow", u"Mostrar Contrase\u00f1a", None))
        self.passwordText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10.5pt;\"><br /></p></body></html>", None))
        self.password_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.emailText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10.5pt;\"><br /></p></body></html>", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Anigiri</p></body></html>", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
        self.registerButton.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
    # retranslateUi

