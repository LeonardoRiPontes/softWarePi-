# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceAtualizar.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_Atualizar(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(577, 440)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(40, 110, 501, 311))
        self.frame_2.setStyleSheet(u"background-color: rgb(209, 209, 209);\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btn_cancelar = QPushButton(self.frame_2)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(190, 260, 131, 31))
        font = QFont()
        font.setFamilies([u"Franklin Gothic Demi Cond"])
        font.setPointSize(12)
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar.setStyleSheet(u"QPushButton{background-color: rgb(250, 250, 250);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 204, 74);\n"
"	transform: 5000ms;\n"
"}")
        self.btn_cadastrar = QPushButton(self.frame_2)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(20, 260, 131, 31))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{background-color: rgb(250, 250, 250);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 204, 74);\n"
"	transform: 5000ms;\n"
"}")

        font2 = QFont()
        font2.setFamilies([u"Fixedsys"])
        self.edit_sala = QLineEdit(self.frame_2)
        self.edit_sala.setObjectName(u"edit_sala")
        self.edit_sala.setGeometry(QRect(20, 120, 231, 31))
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dlg 2"])
        font3.setPointSize(10)
        self.edit_sala.setFont(font3)
        self.edit_sala.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"BORDER-RADIUS:3PX;")
        self.lbl_sala = QLabel(self.frame_2)
        self.lbl_sala.setObjectName(u"lbl_sala")
        self.lbl_sala.setGeometry(QRect(20, 100, 91, 16))
        self.lbl_sala.setFont(font2)
        self.edit_descricao = QLineEdit(self.frame_2)
        self.edit_descricao.setObjectName(u"edit_descricao")
        self.edit_descricao.setGeometry(QRect(20, 40, 461, 51))
        self.edit_descricao.setFont(font3)
        self.edit_descricao.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"BORDER-RADIUS:3PX;")
        self.edit_descricao.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lbl_descricao = QLabel(self.frame_2)
        self.lbl_descricao.setObjectName(u"lbl_descricao")
        self.lbl_descricao.setGeometry(QRect(20, 20, 91, 16))
        self.lbl_descricao.setFont(font2)
        font4 = QFont()
        font4.setFamilies([u"Fixedsys"])
        font4.setPointSize(8)
        self.btn_cancelar_2 = QPushButton(self.frame_2)
        self.btn_cancelar_2.setObjectName(u"btn_cancelar_2")
        self.btn_cancelar_2.setGeometry(QRect(350, 260, 131, 31))
        self.btn_cancelar_2.setFont(font)
        self.btn_cancelar_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar_2.setStyleSheet(u"QPushButton{background-color: rgb(250, 250, 250);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 204, 74);\n"
"	transform: 5000ms;\n"
"}")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 0, 591, 91))
        self.frame.setStyleSheet(u"background-color: rgb(209, 209, 209);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.nome = QLabel(self.frame)
        self.nome.setObjectName(u"nome")
        self.nome.setGeometry(QRect(210, 30, 191, 31))
        font5 = QFont()
        font5.setFamilies([u"Franklin Gothic Demi Cond"])
        font5.setPointSize(16)
        self.nome.setFont(font5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_cancelar.setText(QCoreApplication.translate("MainWindow", u"DELETAR", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"ATUALIZAR", None))
        self.edit_sala.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Em qual sala perdeu?", None))
        self.lbl_sala.setText(QCoreApplication.translate("MainWindow", u"SALA:", None))
        self.edit_descricao.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Descreva seu obejto Ex:cor,fromato,nome.", None))
        self.lbl_descricao.setText(QCoreApplication.translate("MainWindow", u"DESCRI\u00c7\u00c3O:", None))
        self.btn_cancelar_2.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.nome.setText(QCoreApplication.translate("MainWindow", u"ATUALIZAR REGISTROS", None))
    # retranslateUi



    def atualizar_descricao(self):
        descricao_atualizar = self.edit_descricao.text()
        return descricao_atualizar

    def atualizar_sala(self):
        sala_atualizar = self.edit_descricao.text()
        return sala_atualizar


