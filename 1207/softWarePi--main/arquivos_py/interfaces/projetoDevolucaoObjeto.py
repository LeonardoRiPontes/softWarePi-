# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projetoDevolucaoObjeto.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_DevolucaoObjeto(object):
    def setupUi(self, DevolucaoObjeto):
        if not DevolucaoObjeto.objectName():
            DevolucaoObjeto.setObjectName(u"DevolucaoObjeto")
        DevolucaoObjeto.resize(568, 447)
        DevolucaoObjeto.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(DevolucaoObjeto)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_devolver = QPushButton(self.centralwidget)
        self.btn_devolver.setObjectName(u"btn_devolver")
        self.btn_devolver.setGeometry(QRect(60, 330, 201, 31))
        font = QFont()
        font.setFamilies([u"Franklin Gothic Demi Cond"])
        font.setPointSize(12)
        self.btn_devolver.setFont(font)
        self.btn_devolver.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_devolver.setStyleSheet(u"QPushButton{background-color: rgb(250, 250, 250);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 204, 74);\n"
"	transform: 5000ms;\n"
"}")
        self.btn_cancelar = QPushButton(self.centralwidget)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(310, 330, 201, 31))
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar.setStyleSheet(u"QPushButton{background-color: rgb(250, 250, 250);\n"
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
        self.nome_2 = QLabel(self.frame)
        self.nome_2.setObjectName(u"nome_2")
        self.nome_2.setGeometry(QRect(180, 30, 191, 31))
        font1 = QFont()
        font1.setFamilies([u"Franklin Gothic Demi Cond"])
        font1.setPointSize(16)
        self.nome_2.setFont(font1)
        self.edit_matricula = QLineEdit(self.centralwidget)
        self.edit_matricula.setObjectName(u"edit_matricula")
        self.edit_matricula.setGeometry(QRect(60, 170, 451, 31))
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(10)
        self.edit_matricula.setFont(font2)
        self.edit_matricula.setStyleSheet(u"border:none;\n"
"border-radius: 3px;")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 130, 521, 271))
        self.frame_2.setStyleSheet(u"background-color: rgb(209, 209, 209);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lbl_descricao = QLabel(self.frame_2)
        self.lbl_descricao.setObjectName(u"lbl_descricao")
        self.lbl_descricao.setGeometry(QRect(280, 100, 141, 16))
        font3 = QFont()
        font3.setFamilies([u"Fixedsys"])
        self.lbl_descricao.setFont(font3)
        self.dateEdit = QDateEdit(self.frame_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(30, 130, 191, 31))
        font4 = QFont()
        font4.setFamilies([u"Franklin Gothic Demi Cond"])
        self.dateEdit.setFont(font4)
        self.dateEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate(2015, 1, 22))
        self.edit_id = QLineEdit(self.frame_2)
        self.edit_id.setObjectName(u"edit_id")
        self.edit_id.setGeometry(QRect(280, 130, 201, 31))
        self.edit_id.setFont(font2)
        self.edit_id.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;")
        self.edit_id.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl_data = QLabel(self.frame_2)
        self.lbl_data.setObjectName(u"lbl_data")
        self.lbl_data.setGeometry(QRect(30, 100, 171, 16))
        self.lbl_data.setFont(font3)
        self.lbl_sala = QLabel(self.frame_2)
        self.lbl_sala.setObjectName(u"lbl_sala")
        self.lbl_sala.setGeometry(QRect(30, 20, 221, 16))
        self.lbl_sala.setFont(font3)
        DevolucaoObjeto.setCentralWidget(self.centralwidget)
        self.frame_2.raise_()
        self.btn_devolver.raise_()
        self.btn_cancelar.raise_()
        self.frame.raise_()
        self.edit_matricula.raise_()

        self.retranslateUi(DevolucaoObjeto)

        QMetaObject.connectSlotsByName(DevolucaoObjeto)
    # setupUi

    def retranslateUi(self, DevolucaoObjeto):
        DevolucaoObjeto.setWindowTitle(QCoreApplication.translate("DevolucaoObjeto", u"MainWindow", None))
        self.btn_devolver.setText(QCoreApplication.translate("DevolucaoObjeto", u"DEVOLVER", None))
        self.btn_cancelar.setText(QCoreApplication.translate("DevolucaoObjeto", u"CANCELAR", None))
        self.nome_2.setText(QCoreApplication.translate("DevolucaoObjeto", u"DEVOLU\u00c7\u00c3O DE OBJETOS", None))
        self.edit_matricula.setPlaceholderText(QCoreApplication.translate("DevolucaoObjeto", u"Em qual sala perdeu?", None))
        self.lbl_descricao.setText(QCoreApplication.translate("DevolucaoObjeto", u"C\u00d3DIGO DO OBJETO:", None))
        self.edit_id.setPlaceholderText(QCoreApplication.translate("DevolucaoObjeto", u"Digite Aqui", None))
        self.lbl_data.setText(QCoreApplication.translate("DevolucaoObjeto", u"DATA DA DEVOLU\u00c7\u00c3O:", None))
        self.lbl_sala.setText(QCoreApplication.translate("DevolucaoObjeto", u"MATR\u00cdCULA DO SOLICITANTE:", None))
    # retranslateUi

