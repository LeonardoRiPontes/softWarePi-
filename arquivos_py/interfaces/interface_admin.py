# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_admin.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1156, 738)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1161, 111))
        self.frame.setStyleSheet(u"background-color: rgb(209, 209, 209);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 30, 131, 41))
        font = QFont()
        font.setFamilies([u"Franklin Gothic Demi Cond"])
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton{background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 204, 74);\n"
"	transform: 5000ms;\n"
"}")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(940, 30, 171, 41))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton{background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 204, 74);\n"
"	transform: 5000ms;\n"
"}")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(760, 30, 171, 41))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"QPushButton{background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 204, 74);\n"
"	transform: 5000ms;\n"
"}")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 161, 61))
        font1 = QFont()
        font1.setFamilies([u"Franklin Gothic Demi Cond"])
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(580, 30, 171, 41))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton{background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 204, 74);\n"
"	transform: 5000ms;\n"
"}")
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(380, 30, 131, 41))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(u"QPushButton{background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 204, 74);\n"
"	transform: 5000ms;\n"
"}")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 110, 1161, 631))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.tabelas = QTabWidget(self.frame_2)
        self.tabelas.setObjectName(u"tabelas")
        self.tabelas.setGeometry(QRect(66, 50, 1021, 521))
        self.tabela_usuarios = QWidget()
        self.tabela_usuarios.setObjectName(u"tabela_usuarios")
        self.tabelas.addTab(self.tabela_usuarios, "")
        self.tabela_objetos = QWidget()
        self.tabela_objetos.setObjectName(u"tabela_objetos")
        self.tabelas.addTab(self.tabela_objetos, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabelas.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Gerar Relat\u00f3rio", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Deletar", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ENCONTRE ME", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.tabelas.setTabText(self.tabelas.indexOf(self.tabela_usuarios), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabelas.setTabText(self.tabelas.indexOf(self.tabela_objetos), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

