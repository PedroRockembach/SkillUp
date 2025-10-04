# cursos_rotas.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Importando as dependências, modelos e schemas relevantes
from .dependecis import pegar_sessao, verificar_token
from .models import Usuario, Curso
from .schemas import CursoCreate, Curso as CursoSchema

# Criamos um novo roteador para os cursos
# Todos os endpoints aqui exigirão um token válido (Depends(verificar_token))
roteador_cursos = APIRouter(
    prefix="/cursos",
    tags=["Cursos"],
    dependencies=[Depends(verificar_token)]
)

@roteador_cursos.post("/", response_model=CursoSchema, status_code=201)
def criar_curso(
    curso_data: CursoCreate,
    session: Session = Depends(pegar_sessao),
    usuario_logado: Usuario = Depends(verificar_token)
):
    """
    Cria um novo curso no sistema.
    O curso será automaticamente associado ao usuário que está logado.
    """
    # Criamos o objeto do novo curso, associando o ID do usuário logado
    novo_curso = Curso(
        titulo=curso_data.titulo,
        descricao=curso_data.descricao,
        criador_id=usuario_logado.id
    )
    
    session.add(novo_curso)
    session.commit()
    session.refresh(novo_curso) # Atualiza o objeto com os dados do banco (como o ID)
    
    return novo_curso

@roteador_cursos.get("/", response_model=List[CursoSchema])
def listar_todos_os_cursos(session: Session = Depends(pegar_sessao)):
    """
    Retorna uma lista de todos os cursos disponíveis na plataforma.
    Este endpoint pode ser acessado por qualquer usuário logado.
    """
    cursos = session.query(Curso).all()
    return cursos

# Futuramente, podemos adicionar mais endpoints aqui:
# - GET /cursos/{curso_id} -> para ver um curso específico
# - PUT /cursos/{curso_id} -> para atualizar um curso
# - DELETE /cursos/{curso_id} -> para deletar um curso