# Estrutura inicial do projeto SkillUp

Este projeto é uma plataforma de estudo gamificada, com front end e back end organizados em pastas separadas.

## Estrutura de diretórios

- `backend/` - Código do servidor, integrações com banco de dados, funções e testes de terminal
  - `src/` - Código-fonte principal do backend
  - `main/` - Scripts para testes em terminal
  - `database/` - Integração e scripts de banco de dados
  - `functions/` - Funções de negócio e utilitários

- `frontend/` - Código do cliente (web), componentes, páginas e serviços
  - `src/` - Código-fonte principal do frontend
  - `main/` - Scripts para testes em terminal
  - `components/` - Componentes reutilizáveis
  - `pages/` - Páginas da aplicação
    - `estudos/` - Aba para estudos
    - `questoes/` - Aba para questões
  - `services/` - Integração com APIs e serviços
  - `assets/` - Imagens, ícones e outros recursos estáticos

- `tests/` - Testes automatizados gerais

- `.github/` - Instruções e automações do projeto

## Próximos passos
- Definir tecnologias e frameworks para cada parte (ex: React, Node.js, Express, banco de dados)
- Implementar as primeiras rotas e páginas
- Configurar integração contínua e testes
