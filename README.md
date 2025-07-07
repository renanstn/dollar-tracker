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
# Opcional para desenvolvimento apenas
pip install black
pip install isort
```

Rodando black e isort para padronizar o código e ordenar os imports:

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

## Railway

Para conseguir rodar este projeto no Railway, devido a suas limitações, eu precisei seguir esses passos:

1. Alterar o `CMD` do Dockerfile para executar o script `create_database.py`, comitar, e deixar o Railway executar isso
2. Alterar o `CMD` do Dockerfile de volta para executar o `run_get_data.py`
3. Programar um Cron no Railway para executar de hora em hora o container.


## TODO

- [x] Arrumar bug de timezone
- [ ] Frontend para visualização
