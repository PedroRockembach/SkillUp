from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioSchemas(BaseModel): # pega os dados para preencher seu bando de dados 
    nome:str
    email:EmailStr
    senha:str
    ativo:Optional[bool]
    admin:Optional[bool]
    class Config: # Lira disse que cria uma conexão com o bando de dados la
        from_attributes = True

class PedidoSchemas(BaseModel):
    id_usuario: int
    class Config:
        from_attributes = True

class LoginSchemas(BaseModel):
    email:EmailStr
    senha: str
    class Config:
        from_attributes = True

class ItemPedidoSchema(BaseModel):
    quantidade : int
    sabor : str
    tamanho : str
    preco_unitario : float

    class Config:
        from_attributes = True

class ResponsePedidosSchema(BaseModel):
    id : int
    status : str
    preco : float
    
    class Config:
        from_attributes = True