# dollar-tracker

[![Check Python Style with Black](https://github.com/renanstn/dollar-tracker/actions/workflows/black-check.yml/badge.svg)](https://github.com/renanstn/dollar-tracker/actions/workflows/black-check.yml)

Meu app de tracking e visualização do preço do dólar diário.

Visite: http://dollar-tracker.up.railway.app

O projeto é dividido em 3 partes, uma em cada pasta.

- Coletor de dados (data_collector)
- API
- Frontend

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
isort . && black --line-length 79 .
```

Utilizando Docker para testes em um ambiente mais semelhante com a vida real, usando Postgres:

```sh
# Subir o banco
docker compose up -d db
# Executar o script de coleta
docker compose up data_collector
# Exibir os valores salvos no banco (apenas para consulta)
docker compose up show
# Subir a api
docker compose up api
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
- [x] Frontend para visualização

# API

## Descrição

Upa API simples feita em Flask para servir os dados salvos no banco para o frontend.

# Frontend

O mais simples possível, estático, sem usar porra de framework nenhum.
