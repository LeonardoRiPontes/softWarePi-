# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_CadastroUsuario(object):
    def setupUi(self, CadastroUsuario):
        if not CadastroUsuario.objectName():
            CadastroUsuario.setObjectName(u"CadastroUsuario")
        CadastroUsuario.resize(611, 600)
        self.centralwidget = QWidget(CadastroUsuario)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frameCadastro1 = QFrame(self.centralwidget)
        self.frameCadastro1.setObjectName(u"frameCadastro1")
        self.frameCadastro1.setGeometry(QRect(-10, -10, 631, 91))
        self.frameCadastro1.setStyleSheet(u"background-color: rgb(209, 209, 209);\n"
"")
        self.frameCadastro1.setFrameShape(QFrame.StyledPanel)
        self.frameCadastro1.setFrameShadow(QFrame.Raised)
        self.nome = QLabel(self.frameCadastro1)
        self.nome.setObjectName(u"nome")
        self.nome.setGeometry(QRect(70, 40, 151, 21))
        font = QFont()
        font.setFamilies([u"Franklin Gothic Demi Cond"])
        font.setPointSize(20)
        self.nome.setFont(font)
        self.frameCadastro2 = QFrame(self.centralwidget)
        self.frameCadastro2.setObjectName(u"frameCadastro2")
        self.frameCadastro2.setGeometry(QRect(59, 129, 491, 421))
        self.frameCadastro2.setStyleSheet(u"background-color: rgb(209, 209, 209);\n"
"")
        self.frameCadastro2.setFrameShape(QFrame.StyledPanel)
        self.frameCadastro2.setFrameShadow(QFrame.Raised)
        self.edit_user = QLineEdit(self.frameCadastro2)
        self.edit_user.setObjectName(u"edit_user")
        self.edit_user.setGeometry(QRect(170, 120, 251, 31))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(10)
        self.edit_user.setFont(font1)
        self.edit_user.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"font-color: rgb(255, 255, 255);")
        self.edit_user.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edit_senha = QLineEdit(self.frameCadastro2)
        self.edit_senha.setObjectName(u"edit_senha")
        self.edit_senha.setGeometry(QRect(170, 190, 251, 31))
        font2 = QFont()
        font2.setPointSize(10)
        self.edit_senha.setFont(font2)
        self.edit_senha.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:3px")
        self.edit_senha.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.novoCadastro = QLabel(self.frameCadastro2)
        self.novoCadastro.setObjectName(u"novoCadastro")
        self.novoCadastro.setGeometry(QRect(160, 30, 181, 31))
        self.novoCadastro.setFont(font)
        self.edit_confirmar = QLineEdit(self.frameCadastro2)
        self.edit_confirmar.setObjectName(u"edit_confirmar")
        self.edit_confirmar.setGeometry(QRect(170, 260, 251, 31))
        self.edit_confirmar.setFont(font1)
        self.edit_confirmar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:3px")
        self.edit_confirmar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.usuarioCadastro = QLabel(self.frameCadastro2)
        self.usuarioCadastro.setObjectName(u"usuarioCadastro")
        self.usuarioCadastro.setGeometry(QRect(30, 130, 121, 20))
        font3 = QFont()
        font3.setFamilies([u"Fixedsys"])
        font3.setPointSize(8)
        self.usuarioCadastro.setFont(font3)
        self.criarSenhaCadastro = QLabel(self.frameCadastro2)
        self.criarSenhaCadastro.setObjectName(u"criarSenhaCadastro")
        self.criarSenhaCadastro.setGeometry(QRect(30, 200, 111, 20))
        self.criarSenhaCadastro.setFont(font3)
        self.confirmarSenhaCadastro = QLabel(self.frameCadastro2)
        self.confirmarSenhaCadastro.setObjectName(u"confirmarSenhaCadastro")
        self.confirmarSenhaCadastro.setGeometry(QRect(30, 270, 131, 20))
        self.confirmarSenhaCadastro.setFont(font3)
        self.btn_cadastrar = QPushButton(self.frameCadastro2)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(140, 342, 211, 31))
        font4 = QFont()
        font4.setFamilies([u"Franklin Gothic Demi Cond"])
        font4.setPointSize(10)
        self.btn_cadastrar.setFont(font4)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{background-color: rgb(250, 250, 250);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 204, 74);\n"
"	transform: 5000ms;\n"
"}")
        CadastroUsuario.setCentralWidget(self.centralwidget)

        self.retranslateUi(CadastroUsuario)

        QMetaObject.connectSlotsByName(CadastroUsuario)
    # setupUi

    def retranslateUi(self, CadastroUsuario):
        CadastroUsuario.setWindowTitle(QCoreApplication.translate("CadastroUsuario", u"MainWindow", None))
        self.nome.setText(QCoreApplication.translate("CadastroUsuario", u"ENCONTRE ME", None))
        self.edit_user.setText("")
        self.edit_user.setPlaceholderText(QCoreApplication.translate("CadastroUsuario", u"Digite o User", None))
        self.edit_senha.setText("")
        self.edit_senha.setPlaceholderText(QCoreApplication.translate("CadastroUsuario", u"Digite a senha", None))
        self.novoCadastro.setText(QCoreApplication.translate("CadastroUsuario", u"NOVO CADASTRO", None))
        self.edit_confirmar.setText("")
        self.edit_confirmar.setPlaceholderText(QCoreApplication.translate("CadastroUsuario", u"Confirme a senha ", None))
        self.usuarioCadastro.setText(QCoreApplication.translate("CadastroUsuario", u"CRIAR USU\u00c1RIO:", None))
        self.criarSenhaCadastro.setText(QCoreApplication.translate("CadastroUsuario", u"CRIAR SENHA:", None))
        self.confirmarSenhaCadastro.setText(QCoreApplication.translate("CadastroUsuario", u"CONFIRMAR SENHA:", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("CadastroUsuario", u"CADASTRAR", None))
    # retranslateUi

