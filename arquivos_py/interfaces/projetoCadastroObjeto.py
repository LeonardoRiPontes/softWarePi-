# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projetoCadastroObjeto.ui'
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

class Ui_CadastroObjeto(object):
    def setupUi(self, CadastroObjeto):
        if not CadastroObjeto.objectName():
            CadastroObjeto.setObjectName(u"CadastroObjeto")
        CadastroObjeto.resize(560, 431)
        CadastroObjeto.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(CadastroObjeto)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -10, 591, 91))
        self.frame.setStyleSheet(u"background-color: rgb(209, 209, 209);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.nome = QLabel(self.frame)
        self.nome.setObjectName(u"nome")
        self.nome.setGeometry(QRect(180, 30, 191, 31))
        font = QFont()
        font.setFamilies([u"Franklin Gothic Demi Cond"])
        font.setPointSize(16)
        self.nome.setFont(font)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 100, 501, 311))
        self.frame_2.setStyleSheet(u"background-color: rgb(209, 209, 209);\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btn_cancelar = QPushButton(self.frame_2)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(280, 260, 201, 31))
        font1 = QFont()
        font1.setFamilies([u"Franklin Gothic Demi Cond"])
        font1.setPointSize(12)
        self.btn_cancelar.setFont(font1)
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
        self.btn_cadastrar.setGeometry(QRect(20, 260, 201, 31))
        self.btn_cadastrar.setFont(font1)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{background-color: rgb(250, 250, 250);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 204, 74);\n"
"	transform: 5000ms;\n"
"}")
        self.dateEdit = QDateEdit(self.frame_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(20, 200, 191, 31))
        font2 = QFont()
        font2.setFamilies([u"Franklin Gothic Demi Cond"])
        self.dateEdit.setFont(font2)
        self.dateEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"BORDER-RADIUS:3PX;")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate(2015, 1, 22))
        self.lbl_data = QLabel(self.frame_2)
        self.lbl_data.setObjectName(u"lbl_data")
        self.lbl_data.setGeometry(QRect(20, 170, 131, 16))
        font3 = QFont()
        font3.setFamilies([u"Fixedsys"])
        self.lbl_data.setFont(font3)
        self.edit_sala = QLineEdit(self.frame_2)
        self.edit_sala.setObjectName(u"edit_sala")
        self.edit_sala.setGeometry(QRect(20, 120, 191, 31))
        font4 = QFont()
        font4.setFamilies([u"MS Shell Dlg 2"])
        font4.setPointSize(10)
        self.edit_sala.setFont(font4)
        self.edit_sala.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"BORDER-RADIUS:3PX;")
        self.lbl_sala = QLabel(self.frame_2)
        self.lbl_sala.setObjectName(u"lbl_sala")
        self.lbl_sala.setGeometry(QRect(20, 100, 91, 16))
        self.lbl_sala.setFont(font3)
        self.edit_descricao = QLineEdit(self.frame_2)
        self.edit_descricao.setObjectName(u"edit_descricao")
        self.edit_descricao.setGeometry(QRect(20, 40, 461, 51))
        self.edit_descricao.setFont(font4)
        self.edit_descricao.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"BORDER-RADIUS:3PX;")
        self.edit_descricao.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lbl_descricao = QLabel(self.frame_2)
        self.lbl_descricao.setObjectName(u"lbl_descricao")
        self.lbl_descricao.setGeometry(QRect(20, 20, 91, 16))
        self.lbl_descricao.setFont(font3)
        self.radio_not = QRadioButton(self.frame_2)
        self.radio_not.setObjectName(u"radio_not")
        self.radio_not.setGeometry(QRect(300, 210, 82, 17))
        font5 = QFont()
        font5.setFamilies([u"Fixedsys"])
        font5.setPointSize(8)
        self.radio_not.setFont(font5)
        self.radio_not.setCursor(QCursor(Qt.PointingHandCursor))
        self.radio_ves = QRadioButton(self.frame_2)
        self.radio_ves.setObjectName(u"radio_ves")
        self.radio_ves.setGeometry(QRect(300, 180, 101, 17))
        self.radio_ves.setFont(font5)
        self.radio_ves.setCursor(QCursor(Qt.PointingHandCursor))
        self.radio_mat = QRadioButton(self.frame_2)
        self.radio_mat.setObjectName(u"radio_mat")
        self.radio_mat.setGeometry(QRect(300, 150, 82, 17))
        self.radio_mat.setFont(font5)
        self.radio_mat.setCursor(QCursor(Qt.PointingHandCursor))
        self.lbl_periodo = QLabel(self.frame_2)
        self.lbl_periodo.setObjectName(u"lbl_periodo")
        self.lbl_periodo.setGeometry(QRect(300, 120, 91, 16))
        self.lbl_periodo.setFont(font3)
        CadastroObjeto.setCentralWidget(self.centralwidget)
        self.frame_2.raise_()
        self.frame.raise_()

        self.retranslateUi(CadastroObjeto)

        QMetaObject.connectSlotsByName(CadastroObjeto)
    # setupUi

    def retranslateUi(self, CadastroObjeto):
        CadastroObjeto.setWindowTitle(QCoreApplication.translate("CadastroObjeto", u"MainWindow", None))
        self.nome.setText(QCoreApplication.translate("CadastroObjeto", u"CADASTRO DE OBJETOS", None))
        self.btn_cancelar.setText(QCoreApplication.translate("CadastroObjeto", u"CANCELAR", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("CadastroObjeto", u"CADASTRAR", None))
        self.lbl_data.setText(QCoreApplication.translate("CadastroObjeto", u"DATA DO ACHADO:", None))
        self.edit_sala.setPlaceholderText(QCoreApplication.translate("CadastroObjeto", u"Em qual sala perdeu?", None))
        self.lbl_sala.setText(QCoreApplication.translate("CadastroObjeto", u"SALA:", None))
        self.edit_descricao.setPlaceholderText(QCoreApplication.translate("CadastroObjeto", u"Descreva seu obejto Ex:cor,fromato,nome.", None))
        self.lbl_descricao.setText(QCoreApplication.translate("CadastroObjeto", u"DESCRI\u00c7\u00c3O:", None))
        self.radio_not.setText(QCoreApplication.translate("CadastroObjeto", u"NOTURNO", None))
        self.radio_ves.setText(QCoreApplication.translate("CadastroObjeto", u"VESPERTINO", None))
        self.radio_mat.setText(QCoreApplication.translate("CadastroObjeto", u"MATUTINO", None))
        self.lbl_periodo.setText(QCoreApplication.translate("CadastroObjeto", u"PER\u00cdODO:", None))
    # retranslateUi

    def pegar_descrição(self):
        descricao= self.edit_descricao.text()
        return descricao
    def pegar_sala(self):
        sala= self.edit_sala.text()
        return sala
    def pegar_data(self):
        data= self.dateEdit.text()
        return data
    def verificar_radio(self):
        if self.radio_mat.isChecked():
            return "Matunino"
        elif self.radio_ves.isChecked():
            return "Vespertino"
        elif self.radio_not.isChecked():
            return "Noturno"
        else:
            print("Nenhum radio button foi marcado.")

        

        

