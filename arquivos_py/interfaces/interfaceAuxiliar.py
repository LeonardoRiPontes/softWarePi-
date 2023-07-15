# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceAuxiliar.ui'
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

class Ui_Auxiliar(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(383, 311)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-170, -10, 591, 91))
        self.frame.setStyleSheet(u"background-color: rgb(209, 209, 209);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.nome = QLabel(self.frame)
        self.nome.setObjectName(u"nome")
        self.nome.setGeometry(QRect(300, 30, 191, 31))
        font = QFont()
        font.setFamilies([u"Franklin Gothic Demi Cond"])
        font.setPointSize(16)
        self.nome.setFont(font)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 110, 321, 171))
        self.frame_2.setStyleSheet(u"background-color: rgb(209, 209, 209);\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btn_cadastrar = QPushButton(self.frame_2)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(20, 110, 131, 31))
        font1 = QFont()
        font1.setFamilies([u"Franklin Gothic Demi Cond"])
        font1.setPointSize(12)
        self.btn_cadastrar.setFont(font1)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{background-color: rgb(250, 250, 250);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 204, 74);\n"
"	transform: 5000ms;\n"
"}")
        self.edit_sala = QLineEdit(self.frame_2)
        self.edit_sala.setObjectName(u"edit_sala")
        self.edit_sala.setGeometry(QRect(20, 60, 281, 31))
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(10)
        self.edit_sala.setFont(font2)
        self.edit_sala.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"BORDER-RADIUS:3PX;")
        self.lbl_descricao = QLabel(self.frame_2)
        self.lbl_descricao.setObjectName(u"lbl_descricao")
        self.lbl_descricao.setGeometry(QRect(20, 20, 221, 16))
        font3 = QFont()
        font3.setFamilies([u"Fixedsys"])
        self.lbl_descricao.setFont(font3)
        self.btn_cancelar_2 = QPushButton(self.frame_2)
        self.btn_cancelar_2.setObjectName(u"btn_cancelar_2")
        self.btn_cancelar_2.setGeometry(QRect(170, 110, 131, 31))
        self.btn_cancelar_2.setFont(font1)
        self.btn_cancelar_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar_2.setStyleSheet(u"QPushButton{background-color: rgb(250, 250, 250);\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 204, 74);\n"
"	transform: 5000ms;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.nome.setText(QCoreApplication.translate("MainWindow", u"ENCONTRE ME", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"PROCURAR", None))
        self.edit_sala.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o código do objeto", None))
        self.lbl_descricao.setText(QCoreApplication.translate("MainWindow", u"DIGITE O C\u00d3DIGO DO OBEJTO:", None))
        self.btn_cancelar_2.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
    # retranslateUi

    def pegar_codigo(self):
        valor_codigo = self.edit_sala.text()
        return valor_codigo
        