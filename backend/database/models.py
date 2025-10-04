from sqlalchemy import create_engine, Column, String,Integer,Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_utils.types import ChoiceType


#cria a conexão com seu banco 
db = create_engine("sqlite:///banco.db")

# cria a base do banco de dados
Base = declarative_base()

#criar as classes/tabelas do banco
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id",Integer,primary_key=True,autoincrement=True)
    nome = Column("Nome",String)
    email = Column("E-mail",String,nullable=False)
    senha = Column("Senha",String)
    ativo = Column("Ativo",Boolean)
    admin = Column("Admin",Boolean,default=False)
    
    def __init__(self,nome,email,senha,ativo=True,admin=False):
        self.nome = nome
        self.email= email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class Pedido(Base):
    __tablename__ = "pedidos"

    #STATUS_PEDIDOS=(
    #    ("Pendente","Pendente"),
    #    ("Cancelado","Cancelado"),
    #    ("Finalizado","Finalizado")
    #)


    id = Column("id",Integer,primary_key=True, autoincrement=True)
    status = Column("status",String)
    usuario = Column("usuario",ForeignKey("usuarios.id"))
    preco = Column("preco",Float)
    itens = relationship("ItensPedido", cascade= "all,delete")# cria uma relação entre as duas tabelas 
    #e quando for deletado um pedido sera olhado na tabela itensPedido todos os itens relacionados ao pedido e deleta los tambem
    

    def __init__(self,usuario,status="Pendente",preco=0):
        self.usuario = usuario
        self.preco = preco
        self.status = status
    def calcular_preco(self):
        self.preco = 0
        for item in self.itens:
            preco_item = item.preco_unitario  * item.quantidade
            self.preco += preco_item
        
        





class ItensPedido(Base):
    __tablename__ = "Itens_pedido"

    id = Column("id",Integer,primary_key=True,autoincrement=True)
    quantidade = Column("quantidade",Integer)
    sabor = Column("sabor",String)
    tamanho = Column("tamanho",String)
    preco_unitario = Column("preco_unitario",Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido

#executa a criação dos metados do seu banco (cria efetivamente o banco de dados)
