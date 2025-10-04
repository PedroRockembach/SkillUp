from fastapi import APIRouter, Depends, HTTPException
from .models import Usuario
from .dependecis import pegar_sessao, verificar_token, oauth2_schema, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, bcrypt_context
from .schemas import UsuarioCreate as UsuarioSchemas, Login as LoginSchemas
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordRequestForm

roteador_autentique = APIRouter(prefix="/auth",tags=["auth"])

def criar_token(id_usuario,duaracao_token = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    data_expiracao = datetime.now(timezone.utc) + duaracao_token
    dic_info = {"sub":str(id_usuario), "exp": data_expiracao}
    jwt_codificado = jwt.encode(dic_info,SECRET_KEY,ALGORITHM)
    return jwt_codificado

def autenticar_usuario(email,senha,session:Session):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        return False
    elif not bcrypt_context.verify(senha, usuario.senha):
        return False
    return usuario


@roteador_autentique.get("/")
async def home():
    """
    Essa é a rota padrão do nosso sitema.
    """
    return{"mensagem":"Você acessou a rota padrão de autenticação","autenticado":False}

@roteador_autentique.post("/criar_conta")
async def criar_conta(usuario_schema:UsuarioSchemas,session:Session = Depends(pegar_sessao)): # função assincrona
    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).all()
    if len(usuario) > 0: 
        # existe usuario com esse email
        raise HTTPException(status_code= 400,detail="Email do usuario já cadastrado")
    else:
        senha_crip = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(nome=usuario_schema.nome, email=usuario_schema.email, senha=senha_crip, ativo=getattr(usuario_schema, 'ativo', True), admin=getattr(usuario_schema, 'admin', False))
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": f"usuario cadastrado com sucesso {usuario_schema.email}."}
    
@roteador_autentique.post("/login")
async def login(login_schema: LoginSchemas,session:Session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(login_schema.email,login_schema.senha,session)
    if not usuario:
        raise HTTPException (status_code=400, detail="Usuario não encontrado ou senha incorreta.")
    else:
        refresh_token = criar_token(usuario.id, duaracao_token=timedelta(days=7))
        access_token =  criar_token(usuario.id)
        return{
            "access_token": access_token,
            "refresh_token":refresh_token,
            "token_type": "Bearer"
        }
    

@roteador_autentique.post("/login-form")
async def login_form(dados_formulario:OAuth2PasswordRequestForm = Depends(),session:Session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(dados_formulario.username,dados_formulario.password,session)
    if not usuario:
        raise HTTPException (status_code=400, detail="Usuario não encontrado ou senha incorreta.")
    else:
        access_token =  criar_token(usuario.id)
        return{
            "access_token": access_token,
            "token_type": "Bearer"
        }
    
@roteador_autentique.get("/refresh")
async def use_refresh_token(usuario:Usuario = Depends(verificar_token)):
    access_token = criar_token(usuario.id)
    return{
            "access_token": access_token,
            "token_type": "Bearer"
            }

@roteador_autentique.delete("/delete-usuario")
async def deletar_usuario(usuario:Usuario = Depends(verificar_token)):
    # Remove o usuário logado
    # Observação: aqui usamos a própria sessão via dependência pegar_sessao quando necessário
    from .dependecis import pegar_sessao
    session = next(pegar_sessao())
    session.delete(usuario)
    session.commit()
    session.close()
    return {"mensagem": "Usuário removido com sucesso"}