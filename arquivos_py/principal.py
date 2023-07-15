import sys
from PySide6.QtWidgets import QMainWindow,QApplication

from interfaces.cadastroPi import *
from interfaces.inteface_login_encontreme import *
from interfaces.projetoDevolucaoObjeto import *
from interfaces.projetoCadastroObjeto import *
from interfaces.projetoMenu import *
# from Administrador import * 
from interfaces.interfaceAtualizar import *
from interfaces.interfaceAuxiliar import *
# from arquivos_py.Objeto import *


class Logar(QMainWindow,Ui_Login):
    def __init__(self) -> None:
        super(Logar,self).__init__()
        self.setupUi(self)

        self.btn_logar.clicked.connect(self.logar)
    
    def logar(self):
        # senha=self.pegar_senha()
        # user=self.pegar_email()
        # validacao = Administrador(None,user,senha)

        if 1==1:
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
        self.cadastrarUsuario.clicked.connect(self.cadastroUsuario)
        self.atualizarRegistro.clicked.connect(self.updateRegistro)

    def cadastrarObjeto(self):
            self.o=CadastrarObejto()
            self.o.show()

    def devolucao(self):
            self.o=Devolucao()
            self.o.show()

    def cadastroUsuario(self):
            self.o=CadastroUsuario()
            self.o.show()

    def updateRegistro(self):
            self.o=Auxiliar()
            self.o.show()

class CadastrarObejto(QMainWindow,Ui_CadastroObjeto):
    def __init__(self) -> None:
        super(CadastrarObejto,self).__init__()
        self.setupUi(self)
        
        self.btn_cadastrar.clicked.connect(self.cadastar_objeto)
        self.btn_cancelar.clicked.connect(self.close)

    def cadastar_objeto(self):
        descricao=self.pegar_descrição()
        sala=self.pegar_sala()
        data=self.pegar_data()
        periodo=self.verificar_radio()
        print(periodo)
        print(data)
        print(descricao)
        print(sala)
        return periodo,data,descricao
         

class CadastroUsuario(QMainWindow,Ui_CadastroUsuario):
    def __init__(self) -> None:
        super(CadastroUsuario,self).__init__()
        self.setupUi(self)

        

class Devolucao(QMainWindow,Ui_DevolucaoObjeto):
    def __init__(self) -> None:
        super(Devolucao,self).__init__()
        self.setupUi(self)
        self.btn_devolver.clicked.connect(self.devolver_objeto)
        self.btn_cancelar.clicked.connect(self.close)

    def devolver_objeto(self):
        id=self.pegar_id()
        matricula=self.pegar_matricula()
        data_devolucao=self.pegar_data_devolucao()
        print(id)
        print(matricula)
        print(data_devolucao)

class Atualizar(QMainWindow,Ui_Atualizar):
    def __init__(self) -> None:
        super(Atualizar,self).__init__()
        self.setupUi(self)

        self.btn_cancelar_2.clicked.connect(self.close)

    def atualizar_cadastro(self):
        nova_descricao = self.atualizar_descricao()
        nova_sala= self.atualizar_sala()

        

        return nova_descricao,nova_sala
        

class Auxiliar(QMainWindow,Ui_Auxiliar,Ui_Atualizar):
    def __init__(self) -> None:
        super(Auxiliar,self).__init__()
        self.setupUi(self)
        self.btn_cadastrar.clicked.connect(self.procurar)

    def procurar(self):

        codigo= self.pegar_codigo()

        if codigo=="1":#mudar esse valor para procurar o código no banco"
            self.w=Atualizar()
            self.w.edit_descricao.setText()#trocar pelo selct do banco
            self.w.edit_sala.setText()#trocar pelo selct do banco
            self.w.show()
            self.close()
        else:
            print(codigo)

        if codigo=="2":#mudar esse valor para procurar o código no banco
            self.w=Atualizar()
            self.w.edit_descricao.setText()#trocar pelo selct do banco
            self.w.edit_sala.setText()#trocar pelo selct do banco
            self.w.show()
            self.close()
        else:
            print(codigo)
              

if __name__ == "__main__":
    app = QApplication(sys.argv)
    logar = Logar()
    logar.show()
    sys.exit(app.exec())




