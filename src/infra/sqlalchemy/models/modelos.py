from sqlalchemy import Column,Integer,String,Float,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base

class Produto(Base):
    __tablename__ = "Produto"
    id = Column(Integer,autoincrement=True,primary_key=True)
    nome = Column(String(100))
    preco = Column(Float)
    disponivel = Column(Boolean)
    detalhamento = Column(String(100))
    tamanho = Column(String(10))
    usuario_id = Column(Integer,ForeignKey('Usuario.id'))
    usuarios = relationship('Usuario',back_populates="produtos")

class Usuario(Base):
    __tablename__ = "Usuario"
    id = Column(Integer,primary_key=True,autoincrement=True)
    nome = Column(String(100))
    telefone = Column(String(15))
    produtos = relationship('Produto',back_populates="usuarios")
    


class Pedido(Base):
    __tablename__ = "Pedido"
    id = Column(Integer,primary_key=True,autoincrement=True)
    quantidade  = Column(Integer)
    entrega = Column(Boolean)
    endereco = Column(String(70))
    observacao = Column(String(100))


