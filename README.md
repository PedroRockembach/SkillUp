
# SkillUp - Plataforma de Estudo Gamificada

Este projeto é uma plataforma de estudo gamificada, com separação clara entre backend (API) e frontend (interface web).

## Estrutura de Diretórios

```
SkillUp/
├── backend/
│   └── app/
│       ├── routers/
│       ├── schemas/
│       ├── database/
│       ├── __init__.py
│       └── main.py
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── index.html
│   ├── pages/
│   ├── styles/
│   ├── scripts/
│   └── assets/
├── tests/
└── README.md
```

### Backend (FastAPI)
- Estruturado em `app/` com subpastas para rotas (`routers`), modelos de dados (`schemas`) e integração com banco de dados (`database`).
- Utiliza **FastAPI** para a API, **SQLAlchemy** para ORM e **Uvicorn** como servidor ASGI.
- Dependências listadas em `requirements.txt`.
- Variáveis sensíveis e configurações em `.env`.

### Frontend (HTML/CSS/JS)
- Estrutura clássica para projetos web estáticos.
- `index.html` como página principal.
- `pages/` para páginas adicionais (ex: estudos, questões).
- `styles/` para CSS, `scripts/` para JS, `assets/` para imagens e ícones.

### Testes
- A pasta `tests/` pode ser usada para scripts e automações de teste.

## Tecnologias Utilizadas
- **FastAPI**: Framework web moderno e rápido para APIs em Python.
- **Uvicorn**: Servidor ASGI leve e eficiente para rodar o FastAPI.
- **SQLAlchemy**: ORM para integração com bancos de dados relacionais.

## Como rodar o backend
1. Instale as dependências:
   ```bash
   pip install -r backend/requirements.txt
   ```
2. Execute o servidor:
   ```bash
   uvicorn backend.app.main:app --reload
   ```

## Como rodar o frontend
Basta abrir o arquivo `frontend/index.html` no navegador ou servir a pasta `frontend/` com um servidor estático.

---
Sinta-se à vontade para adaptar a estrutura conforme o crescimento do projeto!
