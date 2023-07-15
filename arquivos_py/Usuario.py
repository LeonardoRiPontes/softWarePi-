
from sqlalchemy import Column, String , Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql+pymysql://root:Gloria28@localhost:3306/projeto_integrador')#Alterar url conforme seu servidor
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Usuario(Base):
   __tablename__="usuario"

   id_usuario = Column(Integer, primary_key=True,autoincrement=True)
   tipo = Column(String)
   email = Column(String)
   matricula = Column(Integer)
   
   
   def __init__(self, id_usuario, tipo, email, matricula):
        self.id_usuario = id_usuario
        self.tipo = tipo
        self.email = email
        self.matricula = matricula

   def __repr__(self):#Serve para definir uma forma especifica para representar o objeto em string
      return f"{self.id_usuario} {self.matricula}  {self.tipo}  {self.email} \n"

   def select(self):
             data = session.query(Usuario).all()
             return data
   def adicionar(self):
             session.add(self)
             session.commit()   
   def delete(self):
             session.query(Usuario).filter(Usuario.id_usuario == self.id_usuario).delete
             session.commit()  
   def update(self):
             session.query(Usuario).filter(Usuario.id_usuario == self.id_usuario).update({"id_usuario":self.id_usuario,"tipo":self.tipo,"email":self.email,"matricula":self.matricula})
             session.commit()
   
   def validar(self):
    query = session.query(Usuario).filter_by(matricula==self.matricula,email==self.email)
    result = query.first() 
   
    if result is not None:
        return result
    else:
        return 'Resultado não Encontrado!'            

   