# dollar-tracker

Meu app de tracking e visualização do preço do dólar diário.

# Data Collector

## Descrição

Serviço que coleta o valor do dólar de hora em hora.

Consome a API https://awesomeapi.com.br para obter os valores.

## Setup

Instalando as dependências localmente para testes com sqlite:

```py
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# Opcional para desenvolvimento apenas
pip install black isort
```

Rodando black e isort para padronizar o código e ordenar os imports:

```sh
black --line-length 79 . && isort .
```

Utilizando Docker para testes em um ambiente mais semelhante com a vida real, usando Postgres:

```sh
docker compose up -d db
docker compose up app
docker compose up show
```

A detecção do ambiente e do banco é feita automaticamente a partir da variável de ambiente `DATABASE_URL`.

## .env

Crie um arquivo `.env` na raíz do projeto com os valores:

```
API_KEY=
DATABASE_URL=
```

## Railway.io

Para conseguir rodar este projeto no Railway, devido a suas limitações, eu precisei seguir esses passos:

1. Alterar o `CMD` do Dockerfile para executar o script `create_database.py`, comitar, e deixar o Railway executar isso
2. Alterar o `CMD` do Dockerfile de volta para executar o `run_get_data.py`
3. Programar um Cron no Railway para executar de hora em hora o container
4. Configurar o watch path como `**/*.py` para evitar rebuilds desnecessários

## TODO

- [x] Arrumar bug de timezone
- [x] API para servir os dados
- [ ] Frontend para visualização

# API

## Descrição

Upa API simples feita em Flask para servir os dados coletados para o frontend.

# Frontend

Vem ai...
