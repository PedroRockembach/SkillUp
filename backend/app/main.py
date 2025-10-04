# Ponto de entrada da API FastAPI
from fastapi import FastAPI
from database.autentique_rotas import roteador_autentique
from database.cursos_rotas import roteador_cursos

app = FastAPI(
    title="SkillUp API",
    version="0.1.0",
    description="API da plataforma de educação e desenvolvimento com foco na inclusão de pessoas neurodivergentes."
)

app.include_router(roteador_autentique)
app.include_router(roteador_cursos)

@app.get("/")
def health_check():
    """Endpoint para verificar se a API está funcionando."""
    return {"status": "ok"}