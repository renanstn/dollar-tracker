# dollar-tracker

## Descrição

Meu app de tracking do preço do dólar diário.

Consome a API https://awesomeapi.com.br para obter os valores.

## Setup

Instalando as dependências localmente para testes com sqlite:

```py
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# Optional for development only
pip install black
pip install isort
```

Rodando black e isort:

```sh
black --line-length 79 . && isort .
```

Utilizando Docker para um ambiente mais semelhante com a vida real, usando Postgres:

```sh
docker compose up -d db
docker compose up app
docker compose up show
```

A detecção do ambiente e do banco é feita automaticamente a partir da variável de ambiente `DATABASE_URL`.

## .env

```
API_KEY=
DATABASE_URL=
```
