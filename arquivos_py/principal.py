import sys
from PySide6.QtWidgets import QMainWindow,QApplication

from interfaces.cadastroPi import *
from interfaces.inteface_login_encontreme import *
from interfaces.projetoDevolucaoObjeto import *
from interfaces.projetoCadastroObjeto import *
from interfaces.projetoMenu import *
from Administrador import * 


class Logar(QMainWindow,Ui_Login):
    def __init__(self) -> None:
        super(Logar,self).__init__()
        self.setupUi(self)

        self.btn_logar.clicked.connect(self.logar)
    
    def logar(self):
        senha=self.pegar_senha()
        user=self.pegar_email()
        validacao = Administrador(user,senha)
        validacao.validar()

        if validacao == True:
            self.w=Menu()
            self.w.show()
            self.close()
        else:
            print("senha ou usuario invalio")

class Menu(QMainWindow,Ui_Menu):
    def __init__(self) -> None:
        super(Menu,self).__init__()
        self.setupUi(self)
        self.btn_cadastro.clicked.connect(self.cadastrarObjeto)
        self.btn_devolucao.clicked.connect(self.devolucao)

    def cadastrarObjeto(self):
            self.o=CadastrarObejto()
            self.o.show()

    def devolucao(self):
            self.o=Devolucao()
            self.o.show()

class CadastrarObejto(QMainWindow,Ui_CadastroObjeto):
    def __init__(self) -> None:
        super(CadastrarObejto,self).__init__()
        self.setupUi(self)

class CadastroUsuario(QMainWindow,Ui_CadastroUsuario):
    def __init__(self) -> None:
        super(CadastroUsuario,self).__init__()
        self.setupUi(self)

class Devolucao(QMainWindow,Ui_DevolucaoObjeto):
    def __init__(self) -> None:
        super(Devolucao,self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    logar = Logar()
    logar.show()
    sys.exit(app.exec())




