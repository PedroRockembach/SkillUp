from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from typing import Generator
import os
from dotenv import load_dotenv

load_dotenv()

from .models import db, Usuario

SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

from passlib.context import CryptContext

SessionLocal = sessionmaker(bind=db)
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login-form")

# contexto de hash de senhas
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def pegar_sessao() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def verificar_token(token: str = Depends(oauth2_schema), session: Session = Depends(pegar_sessao)) -> Usuario:
    if not token:
        raise HTTPException(status_code=401, detail="Token ausente")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        sub = payload.get("sub")
        if sub is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        user_id = int(sub)
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

    usuario = session.query(Usuario).filter(Usuario.id == user_id).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return usuario
