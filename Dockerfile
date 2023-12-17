FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1

# Instalando os pacotes
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    pkg-config \
    default-libmysqlclient-dev \
    libmariadb-dev \
    libmariadbclient-dev

# Healthcheck para verificar se o container está funcionando
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD curl -s -f http://localhost:5000/

COPY . /code/
COPY ./.env.example /.env

WORKDIR /code/

RUN pip install pipenv

RUN pipenv install --system --dev

EXPOSE 5000
