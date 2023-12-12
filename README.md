# chalice_rest

This project was generated using fastapi_template.

## Poetry

This project uses poetry. It's a modern dependency management
tool.

To run the project use this set of commands:

```bash
poetry install
poetry run python -m chalice_rest
```

This will start the server on the configured host.

You can find swagger documentation at `/api/docs`.

You can read more about poetry here: https://python-poetry.org/

## Docker

You can start the project with docker using this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . up --build
```

If you want to develop in docker with autoreload add `-f deploy/docker-compose.dev.yml` to your docker command.
Like this:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up --build
```

This command exposes the web application on port 8000, mounts current directory and enables autoreload.

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . build
```

## Project structure

```bash
$ tree "chalice_rest"
chalice_rest
├── conftest.py  # Fixtures for all tests.
├── db  # module contains db configurations
│   ├── dao  # Data Access Objects. Contains different classes to interact with database.
│   └── models  # Package contains different models for ORMs.
├── __main__.py  # Startup script. Starts uvicorn.
├── services  # Package for different external services such as rabbit or redis etc.
├── settings.py  # Main configuration settings for project.
├── static  # Static content.
├── tests  # Tests for project.
└── web  # Package contains web server. Handlers, startup config.
    ├── api  # Package with all handlers.
    │   └── router.py  # Main router.
    ├── application.py  # FastAPI application configuration.
    └── lifetime.py  # Contains actions to perform on startup and shutdown.


chalice_rest
├── chalice
│   ├── __init__.py
│   └── app.py  # Configurações do Chalice
├── db
│   ├── __init__.py
│   ├── dao
│   │   └── __init__.py
│   └── models
│       └── __init__.py
├── s3
│   └── __init__.py  # Configurações para interagir com o S3
├── services
│   ├── __init__.py
│   └── dynamodb.py  # Configurações para interagir com o DynamoDB
├── tests
│   └── __init__.py
└── web
    ├── __init__.py
    ├── api
    │   ├── __init__.py
    │   ├── music.py  # Handlers para manipulação de músicas
    │   ├── playlist.py  # Handlers para manipulação de playlists
    │   └── user.py  # Handlers para manipulação de usuários
    ├── application.py  # Configuração principal do Chalice e FastAPI
    └── lifetime.py  # Ações de inicialização e desligamento

```

## Configuration

This application can be configured with environment variables.

You can create `.env` file in the root directory and place all
environment variables here.

All environment variables should start with "CHALICE_REST_" prefix.

For example if you see in your "chalice_rest/settings.py" a variable named like
`random_parameter`, you should provide the "CHALICE_REST_RANDOM_PARAMETER"
variable to configure the value. This behaviour can be changed by overriding `env_prefix` property
in `chalice_rest.settings.Settings.Config`.

An example of .env file:
```bash
CHALICE_REST_RELOAD="True"
CHALICE_REST_PORT="8000"
CHALICE_REST_ENVIRONMENT="dev"
```

You can read more about BaseSettings class here: https://pydantic-docs.helpmanual.io/usage/settings/

## Pre-commit

To install pre-commit simply run inside the shell:
```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using .pre-commit-config.yaml file.

By default it runs:
* black (formats your code);
* mypy (validates types);
* isort (sorts imports in all files);
* flake8 (spots possible bugs);


You can read more about pre-commit here: https://pre-commit.com/

## Kubernetes
To run your app in kubernetes
just run:
```bash
kubectl apply -f deploy/kube
```

It will create needed components.

If you haven't pushed to docker registry yet, you can build image locally.

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . build
docker save --output chalice_rest.tar chalice_rest:latest
```

## Migrations

If you want to migrate your database, you should run following commands:
```bash
# To run all migrations until the migration with revision_id.
alembic upgrade "<revision_id>"

# To perform all pending migrations.
alembic upgrade "head"
```

### Reverting migrations

If you want to revert migrations, you should run:
```bash
# revert all migrations up to: revision_id.
alembic downgrade <revision_id>

# Revert everything.
 alembic downgrade base
```

### Migration generation

To generate migrations you should run:
```bash
# For automatic change detection.
alembic revision --autogenerate

# For empty file generation.
alembic revision
```


## Running tests

If you want to run it in docker, simply run:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . run --build --rm api pytest -vv .
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . down
```

For running tests on your local machine.


2. Run the pytest.
```bash
pytest -vv .
```
