# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'informes.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.informe1Button = QPushButton(self.centralwidget)
        self.informe1Button.setObjectName(u"informe1Button")
        self.informe1Button.setGeometry(QRect(210, 150, 161, 71))
        self.informe1Button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(64, 150, 255);")
        self.informe5Button = QPushButton(self.centralwidget)
        self.informe5Button.setObjectName(u"informe5Button")
        self.informe5Button.setGeometry(QRect(450, 260, 161, 71))
        self.informe5Button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(64, 150, 255);")
        self.informe4Button = QPushButton(self.centralwidget)
        self.informe4Button.setObjectName(u"informe4Button")
        self.informe4Button.setGeometry(QRect(450, 150, 161, 71))
        self.informe4Button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(64, 150, 255);")
        self.informe2Button = QPushButton(self.centralwidget)
        self.informe2Button.setObjectName(u"informe2Button")
        self.informe2Button.setGeometry(QRect(210, 260, 161, 71))
        self.informe2Button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(64, 150, 255);")
        self.informe3Button = QPushButton(self.centralwidget)
        self.informe3Button.setObjectName(u"informe3Button")
        self.informe3Button.setGeometry(QRect(210, 360, 161, 71))
        self.informe3Button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(64, 150, 255);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.informe1Button.setText(QCoreApplication.translate("MainWindow", u"Informe 1", None))
        self.informe5Button.setText(QCoreApplication.translate("MainWindow", u"Informe 5", None))
        self.informe4Button.setText(QCoreApplication.translate("MainWindow", u"Informe 4", None))
        self.informe2Button.setText(QCoreApplication.translate("MainWindow", u"Informe 2", None))
        self.informe3Button.setText(QCoreApplication.translate("MainWindow", u"Informe 3", None))
    # retranslateUi

