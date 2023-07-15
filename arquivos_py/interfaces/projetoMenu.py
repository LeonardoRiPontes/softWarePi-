# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projetoMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Menu(object):
    def setupUi(self, Menu):
        if not Menu.objectName():
                Menu.setObjectName(u"Menu")
        Menu.resize(999, 630)
        Menu.setMinimumSize(QSize(999, 630))
        Menu.setMaximumSize(QSize(999, 630))
        self.actionObjeto_perdido = QAction(Menu)
        self.actionObjeto_perdido.setObjectName(u"actionObjeto_perdido")
        self.actionE_mail = QAction(Menu)
        self.actionE_mail.setObjectName(u"actionE_mail")
        self.actionO_Autor = QAction(Menu)
        self.actionO_Autor.setObjectName(u"actionO_Autor")
        self.actionO_Software = QAction(Menu)
        self.actionO_Software.setObjectName(u"actionO_Software")
        self.actionObjeto = QAction(Menu)
        self.actionObjeto.setObjectName(u"actionObjeto")
        self.actionDevolvidos = QAction(Menu)
        self.actionDevolvidos.setObjectName(u"actionDevolvidos")
        self.actionPerdidos = QAction(Menu)
        self.actionPerdidos.setObjectName(u"actionPerdidos")
        self.actionDevolver_objeto_perdido = QAction(Menu)
        self.actionDevolver_objeto_perdido.setObjectName(u"actionDevolver_objeto_perdido")
        self.centralwidget = QWidget(Menu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, -10, 1051, 641))
        font = QFont()
        font.setFamilies([u"Franklin Gothic Demi Cond"])
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgb(250, 250, 250);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 10, 1051, 121))
        self.frame_2.setStyleSheet(u"background-color: rgb(209, 209, 209);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 20, 261, 81))
        font1 = QFont()
        font1.setFamilies([u"Franklin Gothic Demi Cond"])
        font1.setPointSize(30)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.gerar_relatorio = QPushButton(self.frame_2)
        self.gerar_relatorio.setObjectName(u"gerar_relatorio")
        self.gerar_relatorio.setGeometry(QRect(390, 40, 171, 41))
        font2 = QFont()
        font2.setFamilies([u"Franklin Gothic Demi Cond"])
        font2.setPointSize(12)
        self.gerar_relatorio.setFont(font2)
        self.gerar_relatorio.setStyleSheet(u"QPushButton{background-color: rgb(255,255,255);\n"
"border-radius: 15px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 204, 74);\n"
"	transform: 5000ms;\n"
"}")
        self.cadastrarUsuario = QPushButton(self.frame_2)
        self.cadastrarUsuario.setObjectName(u"cadastrarUsuario")
        self.cadastrarUsuario.setGeometry(QRect(590, 40, 171, 41))
        self.cadastrarUsuario.setFont(font2)
        self.cadastrarUsuario.setStyleSheet(u"QPushButton{background-color: rgb(255,255,255);\n"
"border-radius: 15px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 204, 74);\n"
"	transform: 5000ms;\n"
"}")
        self.atualizarRegistro = QPushButton(self.frame_2)
        self.atualizarRegistro.setObjectName(u"atualizarRegistro")
        self.atualizarRegistro.setGeometry(QRect(780, 40, 171, 41))
        self.atualizarRegistro.setFont(font2)
        self.atualizarRegistro.setStyleSheet(u"QPushButton{background-color: rgb(255,255,255);\n"
"border-radius: 15px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 204, 74);\n"
"	transform: 5000ms;\n"
"}")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(70, 170, 881, 411))
        self.frame_3.setStyleSheet(u"background-color: rgb(209, 209, 209);\n"
"border-radius:3px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.plainTextEdit = QPlainTextEdit(self.frame_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(160, 80, 571, 141))
        self.plainTextEdit.setFont(font2)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 30, 281, 31))
        font3 = QFont()
        font3.setFamilies([u"Franklin Gothic Demi Cond"])
        font3.setPointSize(20)
        self.label_2.setFont(font3)
        self.btn_cadastro = QPushButton(self.frame_3)
        self.btn_cadastro.setObjectName(u"btn_cadastro")
        self.btn_cadastro.setGeometry(QRect(140, 270, 211, 61))
        self.btn_cadastro.setFont(font2)
        self.btn_cadastro.setStyleSheet(u"QPushButton{background-color: rgb(255,255,255);\n"
"border-radius: 15px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 204, 74);\n"
"	transform: 5000ms;\n"
"}")
        self.btn_devolucao = QPushButton(self.frame_3)
        self.btn_devolucao.setObjectName(u"btn_devolucao")
        self.btn_devolucao.setGeometry(QRect(500, 270, 211, 61))
        self.btn_devolucao.setFont(font2)
        self.btn_devolucao.setStyleSheet(u"QPushButton{background-color: rgb(255,255,255);\n"
"border-radius: 15px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 204, 74);\n"
"	transform: 5000ms;\n"
"}")
        self.frame_3.raise_()
        self.frame_2.raise_()
        Menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(Menu)

        QMetaObject.connectSlotsByName(Menu)
    # setupUi

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QCoreApplication.translate("Menu", u"MainWindow", None))
        self.actionObjeto_perdido.setText(QCoreApplication.translate("Menu", u"Cadastrar objeto perdido", None))
        self.actionE_mail.setText(QCoreApplication.translate("Menu", u"E-mail", None))
        self.actionO_Autor.setText(QCoreApplication.translate("Menu", u"O Autor", None))
        self.actionO_Software.setText(QCoreApplication.translate("Menu", u"O Software", None))
        self.actionObjeto.setText(QCoreApplication.translate("Menu", u"Objeto", None))
        self.actionDevolvidos.setText(QCoreApplication.translate("Menu", u"Devolvidos", None))
        self.actionPerdidos.setText(QCoreApplication.translate("Menu", u"Perdidos", None))
        self.actionDevolver_objeto_perdido.setText(QCoreApplication.translate("Menu", u"Devolver objeto perdido", None))
        self.label.setText(QCoreApplication.translate("Menu", u"ENCONTRE ME", None))
        self.gerar_relatorio.setText(QCoreApplication.translate("Menu", u"GERAR RELAT\u00d3RIO", None))
        self.cadastrarUsuario.setText(QCoreApplication.translate("Menu", u"CADASTRAR USU\u00c1RIO", None))
        self.atualizarRegistro.setText(QCoreApplication.translate("Menu", u"ATUALIZAR REGISTRO", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Menu", u"- Esse \u00e9 nosso software de achados e perdidos, desenvovido para facilitar a informa\u00e7\u00e3o entre os alunos que perdem seus itens no ambiente do SENAC.\n"
"\n"
"\n"
"\n"
"Abaixo temos nossas intera\u00e7\u00f5es.", None))
        self.label_2.setText(QCoreApplication.translate("Menu", u"Bem vindo ao, Encontre Me", None))
        self.btn_cadastro.setText(QCoreApplication.translate("Menu", u"CADASTAR NOVO OBJETOS", None))
        self.btn_devolucao.setText(QCoreApplication.translate("Menu", u"DEVOLU\u00c7\u00c3O DE OBJETOS", None))
    # retranslateUi

