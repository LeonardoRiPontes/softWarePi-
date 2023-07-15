from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String , Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


# Config
engine = create_engine('mysql+pymysql://root:Gloria28@localhost:3306/projeto_integrador')#Alterar url conforme seu servidor
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Administrador(Base):
   __tablename__="administrador"

   id_administrador = Column(Integer, primary_key=True,autoincrement=True)
   usr_login = Column(String)
   senha = Column(String)
   
   
   def __init__(self, id_administrador, usr_login, senha):
        self.id_administrador = id_administrador
        self.usr_login = usr_login
        self.senha = senha

   def __repr__(self):#Serve para definir uma forma especifica para representar o objeto em string
      return f"{self.id_administrador}  {self.usr_login}  {self.senha} \n"

   def select(self):
             data = session.query(Administrador).all()
             return data
   def adicionar(self):
             session.add(self)
             session.commit()   
   def delete(self):
             session.query(Administrador).filter(Administrador.id_administrador == self.id_administrador).delete
             session.commit()  
   def update(self):
             session.query(Administrador).filter(Administrador.id_administrador == self.id_administrador).update({"usr_login":self.usr_login,"senha":self.senha})
             session.commit()    

   def validar(self):
    query = session.query(Administrador).filter_by(usr_login=self.usr_login,senha = self.senha)
    result = query.first() 
   
    if result is not None:
        return result
    else:
        return 'Resultado não Encontrado!'            
                            

   