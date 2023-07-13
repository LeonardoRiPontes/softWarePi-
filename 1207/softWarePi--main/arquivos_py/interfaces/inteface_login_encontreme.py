# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inteface_login_encontreme.ui'
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

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(528, 518)
        Login.setMinimumSize(QSize(528, 518))
        Login.setMaximumSize(QSize(528, 518))
        Login.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.198864, x2:1, y2:0, stop:0 rgba(153, 153, 153, 255), stop:1 rgba(210, 210, 210, 255));")
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(528, 518))
        self.centralwidget.setMaximumSize(QSize(528, 518))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 170, 401, 301))
        self.frame.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_email_login = QLabel(self.frame)
        self.label_email_login.setObjectName(u"label_email_login")
        self.label_email_login.setGeometry(QRect(50, 20, 31, 21))
        font = QFont()
        font.setFamilies([u"Franklin Gothic Demi Cond"])
        font.setPointSize(10)
        self.label_email_login.setFont(font)
        self.label_email_login.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_email_login = QLineEdit(self.frame)
        self.line_email_login.setObjectName(u"line_email_login")
        self.line_email_login.setGeometry(QRect(40, 50, 321, 31))
        self.line_email_login.setStyleSheet(u"background-color: rgb(203, 203, 203);\n"
"border-radius:2px;\n"
"input:password;")
        self.btn_logar = QPushButton(self.frame)
        self.btn_logar.setObjectName(u"btn_logar")
        self.btn_logar.setGeometry(QRect(90, 220, 221, 41))
        font1 = QFont()
        font1.setFamilies([u"Franklin Gothic Demi Cond"])
        font1.setPointSize(12)
        self.btn_logar.setFont(font1)
        self.btn_logar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logar.setStyleSheet(u"QPushButton{background-color: rgb(255, 204, 74);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.188, x2:1, y2:0, stop:0 rgba(255, 141, 102, 255), stop:0.670455 rgba(235, 194, 61, 255), stop:1 rgba(255, 192, 43, 255));\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 204, 74);\n"
"}\n"
"\n"
"")
        self.line_senha_login = QLineEdit(self.frame)
        self.line_senha_login.setObjectName(u"line_senha_login")
        self.line_senha_login.setGeometry(QRect(40, 140, 321, 31))
        self.line_senha_login.setStyleSheet(u"background-color: rgb(203, 203, 203);\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-radius:2px;\n"
"border-color:black;")
        self.line_senha_login.setEchoMode(QLineEdit.Password)
        self.label_senha_login = QLabel(self.frame)
        self.label_senha_login.setObjectName(u"label_senha_login")
        self.label_senha_login.setGeometry(QRect(50, 110, 151, 21))
        self.label_senha_login.setFont(font)
        self.label_senha_login.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, -10, 531, 141))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_nome = QLabel(self.frame_2)
        self.label_nome.setObjectName(u"label_nome")
        self.label_nome.setGeometry(QRect(-30, 0, 601, 151))
        font2 = QFont()
        font2.setFamilies([u"Niagara Solid"])
        font2.setPointSize(72)
        self.label_nome.setFont(font2)
        self.label_nome.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.818, y1:1, x2:1, y2:0, stop:0 rgba(255, 209, 113, 255), stop:1 rgba(255, 183, 0, 255));")
        self.label_nome.setAlignment(Qt.AlignCenter)
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.label_email_login.setText(QCoreApplication.translate("Login", u"USER", None))
        self.line_email_login.setPlaceholderText(QCoreApplication.translate("Login", u"Digite seu user", None))
        self.btn_logar.setText(QCoreApplication.translate("Login", u"Login", None))
        self.line_senha_login.setPlaceholderText(QCoreApplication.translate("Login", u"Digite sua senha", None))
        self.label_senha_login.setText(QCoreApplication.translate("Login", u"SENHA", None))
        self.label_nome.setText(QCoreApplication.translate("Login", u"ENCONTRE ME", None))

    def pegar_email(self):
        valor_usuario= self.line_email_login.text()
        return valor_usuario
    def pegar_senha(self):
        valor_senha= self.line_senha_login.text()
        return valor_senha

        
    retranslateUi

