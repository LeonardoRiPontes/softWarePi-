from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String , Integer , ForeignKey,Date
from sqlalchemy import create_engine ,func
from sqlalchemy.ext.declarative import declarative_base

import aspose.pdf as ap 

#inicializada doc obj
document = ap.Document()

#adiciona a pagina
page = document.pages.add


engine = create_engine('mysql+pymysql://root:Gloria28@localhost:3306/projeto_integrador')#Alterar url conforme seu servidor
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Objeto(Base):
   __tablename__="objeto"

   id_objeto = Column(Integer, primary_key=True,autoincrement=True)
   descricao = Column(String)
   num_sala =  Column(Integer)
   periodo = Column(String)
   data_encontrado = Column(Date)
   status_objeto = Column(String)
   data_devolvido = Column(Date)#
   id_usuario_devolvido = Column(Integer, ForeignKey("usuario.id_usuario")) 
   
   
   def __init__(self, id_objeto, descricao, num_sala, periodo, data_encontrado, status_objeto, data_devolvido, id_usuario_devolvido):
        self.id_objeto = id_objeto
        self.descricao = descricao
        self.num_sala = num_sala
        self.periodo = periodo
        self.data_encontrado = data_encontrado
        self.status_objeto = status_objeto
        self.data_devolvido = data_devolvido
        self.id_usuario_devolvido = id_usuario_devolvido

   def __repr__(self):#Serve para definir uma forma especifica para representar o objeto em string
      return f"{self.id_objeto}  {self.descricao}  {self.num_sala}  {self.periodo}  {self.data_encontrado} {self.status_objeto}  {self.data_devolvido}  {self.id_usuario_devolvido}\n"

   def select(self):
             data = db.session.query(Objeto).all()
             return data
   def adicionar(self):
            session.add(self)
            session.commit()   
   def delete(self):
            session.query(Objeto).filter(Objeto.id_objeto == self.id_objeto).delete
            session.commit()  
   def update(self):
         session.query(Objeto).filter(Objeto.id_objeto == id_objeto).update({"id_objeto":self.id_objeto, "descricao":self.descricao, "num_sala":self.num_sala, "periodo":self.periodo, "data_encontrado":self.data_encontrado, "status_objeto":self.status_objeto, "data_devolvido":self.data_devolvido, "id_usuario_devolvido":self.id_usuario_devolvido})
         session.commit()  
   def devolvidosUsuarios(self):  
         for o, u in session.query(Objeto, Usuario).filter(Objeto.status_objeto == "Devolvido").filter(Objeto.id_usuario_devolvido == Usuario.id_usuario).all:
            texto_parte = ap.text.TextFragment("ID Objeto: {} Descrição: {} Data Devolvido: {} Id do Usuario que recebeu: {} Matricula: {} Email: {} Tipo de Usuario: {}".format(o.id_objeto,o.descricao, o.data_devolvido, o.id_usuario_devolvido ,u.matricula,u.email,u.tipo)) 
            page.paragraphs.add(texto_parte)
      #adiciona o fragmento do texto a pagina
   
   document.save("RelatorioDevolvidos.pdf")



   