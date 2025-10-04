from pydantic import BaseModel, EmailStr
from typing import Optional, List

# --- Schemas de Usuário (mantemos a base) ---
class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    senha: str

class Usuario(UsuarioBase):
    id: int
    ativo: bool
    admin: bool

    class Config:
        from_attributes = True

class Login(BaseModel):
    email: EmailStr
    senha: str

# --- Novos Schemas para Cursos e Mídias ---
class MidiaBase(BaseModel):
    tipo: str
    conteudo_ou_url: str

class MidiaCreate(MidiaBase):
    pass

class Midia(MidiaBase):
    id: int
    curso_id: int
    
    class Config:
        from_attributes = True

class CursoBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None

class CursoCreate(CursoBase):
    pass

class Curso(CursoBase):
    id: int
    criador_id: int
    midias: List[Midia] = [] # Um curso terá uma lista de mídias

    class Config:
        from_attributes = True