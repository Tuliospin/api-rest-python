# api-rest-python

REST API construída com **FastAPI** e Python, com autenticação JWT, banco de dados PostgreSQL e documentação automática via Swagger.

---

## Stack Tecnológica

- [Python 3.11+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Alembic](https://alembic.sqlalchemy.org/) (migrações)
- [JWT](https://jwt.io/) (autenticação)
- [Docker](https://www.docker.com/)

---

## Estrutura de Pastas

```
api-rest-python/
├── app/
│   ├── models/        # Modelos do banco de dados
│   ├── routes/        # Routers da API
│   ├── schemas/       # Pydantic schemas
│   ├── services/      # Regras de negócio
│   ├── core/          # Configurações e segurança
│   ├── db/            # Conexão e sessão com o banco
│   └── main.py        # Entrypoint da aplicação
├── alembic/           # Migrações de banco
├── tests/             # Testes unitários e de integração
├── .env
├── .env.example
├── requirements.txt
└── docker-compose.yml
```

---

## Pré-requisitos

- Python 3.11 ou superior
- PostgreSQL 15+
- Docker e Docker Compose (opcional, mas recomendado)

---

## Instalação Local (sem Docker)

### 1. Clone o repositório

```bash
git clone https://github.com/Tuliospin/api-rest-python.git
cd api-rest-python
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

```bash
cp .env.example .env
```

Edite o `.env`:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/apidb
SECRET_KEY=sua-chave-secreta-aqui
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Execute as migrações

```bash
alembic upgrade head
```

### 6. Inicie a aplicação

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API disponível em: [http://localhost:8000](http://localhost:8000)

Documentação Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Execução com Docker (recomendado)

```bash
docker compose up --build
```

---

## Endpoints Principais

| Método | Rota | Descrição |
|--------|------|------------|
| POST | /auth/register | Cadastrar usuário |
| POST | /auth/login | Obter token JWT |
| GET | /users/me | Perfil do usuário autenticado |
| GET | /items | Listar todos os itens |
| POST | /items | Criar novo item |
| PUT | /items/{id} | Atualizar item |
| DELETE | /items/{id} | Remover item |

---

## Testes

```bash
pytest tests/ -v
```

---

## Licença

MIT License © 2026 Túlio Silva
