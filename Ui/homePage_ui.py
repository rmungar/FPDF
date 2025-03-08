# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homePage.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1031, 750)
        MainWindow.setMinimumSize(QSize(1031, 750))
        MainWindow.setMaximumSize(QSize(1031, 750))
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
        self.widget.setStyleSheet(u"background-color: rgb(34, 65, 139)")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 854, 2224))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.label_5, 10, 0, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.label_4, 7, 0, 1, 1)

        self.topMangas = QWidget(self.scrollAreaWidgetContents_2)
        self.topMangas.setObjectName(u"topMangas")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topMangas.sizePolicy().hasHeightForWidth())
        self.topMangas.setSizePolicy(sizePolicy)
        self.topMangas.setMinimumSize(QSize(0, 500))
        self.topMangas.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(self.topMangas)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_8, 2, 2, 1, 1)

        self.mangaTop3 = QPushButton(self.topMangas)
        self.mangaTop3.setObjectName(u"mangaTop3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mangaTop3.sizePolicy().hasHeightForWidth())
        self.mangaTop3.setSizePolicy(sizePolicy1)
        self.mangaTop3.setMinimumSize(QSize(200, 200))
        self.mangaTop3.setMaximumSize(QSize(200, 200))
        self.mangaTop3.setStyleSheet(u"background-color: rgb(108, 199, 255);")

        self.gridLayout_5.addWidget(self.mangaTop3, 2, 7, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 2, 8, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.mangaTop2 = QPushButton(self.topMangas)
        self.mangaTop2.setObjectName(u"mangaTop2")
        sizePolicy1.setHeightForWidth(self.mangaTop2.sizePolicy().hasHeightForWidth())
        self.mangaTop2.setSizePolicy(sizePolicy1)
        self.mangaTop2.setMinimumSize(QSize(200, 200))
        self.mangaTop2.setMaximumSize(QSize(200, 200))
        self.mangaTop2.setStyleSheet(u"background-color: rgb(108, 199, 255);")

        self.gridLayout_5.addWidget(self.mangaTop2, 1, 1, 3, 1)

        self.mangaTop1 = QPushButton(self.topMangas)
        self.mangaTop1.setObjectName(u"mangaTop1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(30)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mangaTop1.sizePolicy().hasHeightForWidth())
        self.mangaTop1.setSizePolicy(sizePolicy2)
        self.mangaTop1.setMinimumSize(QSize(300, 400))
        self.mangaTop1.setMaximumSize(QSize(300, 400))
        self.mangaTop1.setStyleSheet(u"background-color: rgb(108, 199, 255);")

        self.gridLayout_5.addWidget(self.mangaTop1, 2, 3, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_14, 0, 1, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_15, 4, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_9, 2, 5, 1, 1)


        self.gridLayout_6.addWidget(self.topMangas, 6, 0, 1, 1)

        self.line_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 0))
        self.line_3.setStyleSheet(u"color: rgb(59, 59, 59);")
        self.line_3.setFrameShadow(QFrame.Shadow.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_6.addWidget(self.line_3, 5, 0, 1, 1)

        self.topMangakas = QWidget(self.scrollAreaWidgetContents_2)
        self.topMangakas.setObjectName(u"topMangakas")
        self.topMangakas.setMinimumSize(QSize(0, 500))
        self.topMangakas.setStyleSheet(u"")
        self.gridLayout_8 = QGridLayout(self.topMangakas)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_26, 1, 6, 1, 1)

        self.mangakaTop3 = QPushButton(self.topMangakas)
        self.mangakaTop3.setObjectName(u"mangakaTop3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mangakaTop3.sizePolicy().hasHeightForWidth())
        self.mangakaTop3.setSizePolicy(sizePolicy3)
        self.mangakaTop3.setMinimumSize(QSize(200, 200))
        self.mangakaTop3.setMaximumSize(QSize(200, 200))
        self.mangakaTop3.setStyleSheet(u"background-color: rgb(108, 199, 255);")

        self.gridLayout_8.addWidget(self.mangakaTop3, 1, 5, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_28, 0, 1, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_24, 1, 0, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_27, 1, 4, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_25, 1, 2, 1, 1)

        self.mangakaTop2 = QPushButton(self.topMangakas)
        self.mangakaTop2.setObjectName(u"mangakaTop2")
        sizePolicy1.setHeightForWidth(self.mangakaTop2.sizePolicy().hasHeightForWidth())
        self.mangakaTop2.setSizePolicy(sizePolicy1)
        self.mangakaTop2.setMinimumSize(QSize(200, 200))
        self.mangakaTop2.setMaximumSize(QSize(200, 200))
        self.mangakaTop2.setStyleSheet(u"background-color: rgb(108, 199, 255);")

        self.gridLayout_8.addWidget(self.mangakaTop2, 1, 1, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_29, 0, 5, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_30, 2, 5, 1, 1)

        self.mangakaTop1 = QPushButton(self.topMangakas)
        self.mangakaTop1.setObjectName(u"mangakaTop1")
        sizePolicy3.setHeightForWidth(self.mangakaTop1.sizePolicy().hasHeightForWidth())
        self.mangakaTop1.setSizePolicy(sizePolicy3)
        self.mangakaTop1.setMinimumSize(QSize(300, 400))
        self.mangakaTop1.setMaximumSize(QSize(300, 400))
        self.mangakaTop1.setStyleSheet(u"background-color: rgb(108, 199, 255);")

        self.gridLayout_8.addWidget(self.mangakaTop1, 0, 3, 3, 1)


        self.gridLayout_6.addWidget(self.topMangakas, 12, 0, 1, 1)

        self.line_4 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(0, 0))
        self.line_4.setStyleSheet(u"color: rgb(59, 59, 59);")
        self.line_4.setFrameShadow(QFrame.Shadow.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_6.addWidget(self.line_4, 1, 0, 1, 1)

        self.line_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 0))
        self.line_2.setStyleSheet(u"color: rgb(59, 59, 59);")
        self.line_2.setFrameShadow(QFrame.Shadow.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_6.addWidget(self.line_2, 11, 0, 1, 1)

        self.topEstudios = QWidget(self.scrollAreaWidgetContents_2)
        self.topEstudios.setObjectName(u"topEstudios")
        self.topEstudios.setMinimumSize(QSize(0, 500))
        self.topEstudios.setStyleSheet(u"")
        self.gridLayout_7 = QGridLayout(self.topEstudios)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_16, 1, 0, 1, 1)

        self.estudiosTop3 = QPushButton(self.topEstudios)
        self.estudiosTop3.setObjectName(u"estudiosTop3")
        sizePolicy1.setHeightForWidth(self.estudiosTop3.sizePolicy().hasHeightForWidth())
        self.estudiosTop3.setSizePolicy(sizePolicy1)
        self.estudiosTop3.setMinimumSize(QSize(200, 200))
        self.estudiosTop3.setMaximumSize(QSize(200, 200))
        self.estudiosTop3.setStyleSheet(u"background-color: rgb(108, 199, 255);")

        self.gridLayout_7.addWidget(self.estudiosTop3, 1, 5, 1, 1)

        self.estudiosTop2 = QPushButton(self.topEstudios)
        self.estudiosTop2.setObjectName(u"estudiosTop2")
        sizePolicy1.setHeightForWidth(self.estudiosTop2.sizePolicy().hasHeightForWidth())
        self.estudiosTop2.setSizePolicy(sizePolicy1)
        self.estudiosTop2.setMinimumSize(QSize(200, 200))
        self.estudiosTop2.setMaximumSize(QSize(200, 200))
        self.estudiosTop2.setStyleSheet(u"background-color: rgb(108, 199, 255);")

        self.gridLayout_7.addWidget(self.estudiosTop2, 1, 1, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_19, 1, 6, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_17, 1, 2, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_20, 1, 4, 1, 1)

        self.estudiosTop1 = QPushButton(self.topEstudios)
        self.estudiosTop1.setObjectName(u"estudiosTop1")
        sizePolicy3.setHeightForWidth(self.estudiosTop1.sizePolicy().hasHeightForWidth())
        self.estudiosTop1.setSizePolicy(sizePolicy3)
        self.estudiosTop1.setMinimumSize(QSize(300, 400))
        self.estudiosTop1.setMaximumSize(QSize(300, 400))
        self.estudiosTop1.setStyleSheet(u"background-color: rgb(108, 199, 255);")

        self.gridLayout_7.addWidget(self.estudiosTop1, 0, 3, 3, 1)


        self.gridLayout_6.addWidget(self.topEstudios, 9, 0, 1, 1)

        self.line = QFrame(self.scrollAreaWidgetContents_2)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 0))
        self.line.setStyleSheet(u"color: rgb(59, 59, 59);")
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_6.addWidget(self.line, 8, 0, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.label_3, 4, 0, 1, 1)

        self.topAnimes = QWidget(self.scrollAreaWidgetContents_2)
        self.topAnimes.setObjectName(u"topAnimes")
        self.topAnimes.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.topAnimes.sizePolicy().hasHeightForWidth())
        self.topAnimes.setSizePolicy(sizePolicy4)
        self.topAnimes.setMinimumSize(QSize(0, 500))
        self.topAnimes.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.topAnimes)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_13, 2, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_9, 0, 1, 1, 1)

        self.animeTop3 = QPushButton(self.topAnimes)
        self.animeTop3.setObjectName(u"animeTop3")
        sizePolicy1.setHeightForWidth(self.animeTop3.sizePolicy().hasHeightForWidth())
        self.animeTop3.setSizePolicy(sizePolicy1)
        self.animeTop3.setMinimumSize(QSize(200, 200))
        self.animeTop3.setMaximumSize(QSize(200, 200))
        self.animeTop3.setStyleSheet(u"background-color: rgb(108, 199, 255);")

        self.gridLayout_4.addWidget(self.animeTop3, 2, 7, 3, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_14, 3, 6, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_11, 3, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_13, 3, 2, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_11, 6, 1, 1, 1)

        self.animeTop1 = QPushButton(self.topAnimes)
        self.animeTop1.setObjectName(u"animeTop1")
        sizePolicy3.setHeightForWidth(self.animeTop1.sizePolicy().hasHeightForWidth())
        self.animeTop1.setSizePolicy(sizePolicy3)
        self.animeTop1.setMinimumSize(QSize(300, 400))
        self.animeTop1.setMaximumSize(QSize(300, 400))
        self.animeTop1.setStyleSheet(u"background-color: rgb(108, 199, 255);")

        self.gridLayout_4.addWidget(self.animeTop1, 1, 3, 5, 3)

        self.animeTop2 = QPushButton(self.topAnimes)
        self.animeTop2.setObjectName(u"animeTop2")
        sizePolicy1.setHeightForWidth(self.animeTop2.sizePolicy().hasHeightForWidth())
        self.animeTop2.setSizePolicy(sizePolicy1)
        self.animeTop2.setMinimumSize(QSize(200, 200))
        self.animeTop2.setMaximumSize(QSize(200, 200))
        self.animeTop2.setStyleSheet(u"background-color: rgb(108, 199, 255);")

        self.gridLayout_4.addWidget(self.animeTop2, 2, 1, 3, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 1, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_10, 5, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_12, 3, 8, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 6, 7, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_12, 4, 0, 1, 1)


        self.gridLayout_6.addWidget(self.topAnimes, 2, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_2.addWidget(self.scrollArea, 5, 2, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 3, 2, 18, 3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 24pt \"Pinky Show\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label, 0, 1, 2, 1)

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
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.UserAvailable))
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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.mangaButton.setText(QCoreApplication.translate("MainWindow", u"Mangas", None))
        self.animeButton.setText(QCoreApplication.translate("MainWindow", u"Animes", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Mangakas</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Estudios</span></p></body></html>", None))
        self.mangaTop3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.mangaTop2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.mangaTop1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.mangakaTop3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.mangakaTop2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.mangakaTop1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.estudiosTop3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.estudiosTop2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.estudiosTop1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Animes</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Mangas</span></p></body></html>", None))
        self.animeTop3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.animeTop1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.animeTop2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Anigiri</p></body></html>", None))
        self.userButton.setText("")
        self.mangakaButton.setText(QCoreApplication.translate("MainWindow", u"Mangakas", None))
        self.estudioButton.setText(QCoreApplication.translate("MainWindow", u"Estudios", None))
    # retranslateUi

