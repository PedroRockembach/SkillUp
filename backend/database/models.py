from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship

# A conexão com o banco continua a mesma
db = create_engine("sqlite:///banco.db")
Base = declarative_base()

# Modelo de Usuário (ajustado do seu original)
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String, nullable=False, unique=True)
    senha = Column(String) # Lembre-se que salvamos o hash, não a senha
    ativo = Column(Boolean, default=True)
    admin = Column(Boolean, default=False)
    
    # Relação: Um usuário pode criar vários cursos
    cursos = relationship("Curso", back_populates="criador", cascade="all, delete-orphan")

# Novo modelo para Cursos
class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    descricao = Column(Text)
    criador_id = Column(Integer, ForeignKey("usuarios.id"))
    
    # Relações
    criador = relationship("Usuario", back_populates="cursos")
    midias = relationship("Midia", back_populates="curso", cascade="all, delete-orphan")

# Novo modelo para Mídias (conteúdo dos cursos)
class Midia(Base):
    __tablename__ = "midias"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String) # Ex: 'video', 'texto', 'audio'
    conteudo_ou_url = Column(Text, nullable=False)
    curso_id = Column(Integer, ForeignKey("cursos.id"))

    # Relação
    curso = relationship("Curso", back_populates="midias")