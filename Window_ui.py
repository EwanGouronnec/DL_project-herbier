# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SearchWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_SearchEngine(object):
    def setupUi(self, SearchEngine):
        if not SearchEngine.objectName():
            SearchEngine.setObjectName(u"SearchEngine")
        SearchEngine.resize(632, 377)
        self.gridLayout = QGridLayout(SearchEngine)
        self.gridLayout.setObjectName(u"gridLayout")
        self.SearchEdit = QLineEdit(SearchEngine)
        self.SearchEdit.setObjectName(u"SearchEdit")

        self.gridLayout.addWidget(self.SearchEdit, 0, 0, 1, 2)

        self.SearchButton = QPushButton(SearchEngine)
        self.SearchButton.setObjectName(u"SearchButton")

        self.gridLayout.addWidget(self.SearchButton, 0, 2, 1, 1)

        self.Information = QLineEdit(SearchEngine)
        self.Information.setObjectName(u"Information")
        self.Information.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.Information, 2, 0, 1, 1)

        self.ZoomIn = QPushButton(SearchEngine)
        self.ZoomIn.setObjectName(u"ZoomIn")
        self.ZoomIn.setMinimumSize(QSize(75, 0))
        icon = QIcon()
        icon.addFile(u"zoom+.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ZoomIn.setIcon(icon)

        self.gridLayout.addWidget(self.ZoomIn, 2, 1, 1, 1)

        self.ZoomOut = QPushButton(SearchEngine)
        self.ZoomOut.setObjectName(u"ZoomOut")
        self.ZoomOut.setEnabled(True)
        icon1 = QIcon()
        icon1.addFile(u"zoom-.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ZoomOut.setIcon(icon1)

        self.gridLayout.addWidget(self.ZoomOut, 2, 2, 1, 1)

        self.Image = QLabel(SearchEngine)
        self.Image.setObjectName(u"Image")
        self.Image.setMinimumSize(QSize(200, 0))
        self.Image.setStyleSheet(u"border: 2px solid black;  /* Cr\u00e9e une bordure noire de 2px autour de l'image */\n"
"border-radius: 10px;      /* Arrondir les coins du cadre */")

        self.gridLayout.addWidget(self.Image, 1, 0, 1, 1)

        self.label = QLabel(SearchEngine)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(250, 300))
        self.label.setStyleSheet(u"border: 2px solid black;  /* Cr\u00e9e une bordure noire de 2px autour de l'image */\n"
"border-radius: 10px;      /* Arrondir les coins du cadre */")

        self.gridLayout.addWidget(self.label, 1, 1, 1, 2)


        self.retranslateUi(SearchEngine)

        QMetaObject.connectSlotsByName(SearchEngine)
    # setupUi

    def retranslateUi(self, SearchEngine):
        SearchEngine.setWindowTitle(QCoreApplication.translate("SearchEngine", u"Dialog", None))
        self.SearchEdit.setText(QCoreApplication.translate("SearchEngine", u"Enter your query here", None))
        self.SearchButton.setText(QCoreApplication.translate("SearchEngine", u"Search", None))
        self.Information.setText(QCoreApplication.translate("SearchEngine", u"Search information", None))
        self.ZoomIn.setText("")
        self.ZoomOut.setText("")
        self.Image.setText("")
        self.label.setText("")
    # retranslateUi

