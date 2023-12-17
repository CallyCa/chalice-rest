# Versão do Makefile
VERSION = 1.0.0

# Comando para iniciar o Docker Compose
COMPOSE = docker compose

# Comando para executar os testes
TEST = pytest

# Variável para os argumentos do teste
ARGS =

# Regra para iniciar o Docker Compose
init:
	$(COMPOSE) up -d

# Regra para executar os testes
test:
	$(COMPOSE) run --rm web $(TEST) $(ARGS)

# Regra para limpar os containers e imagens do Docker
clean:
	$(COMPOSE) down -v

# Regra para imprimir a versão do Makefile
version:
	@echo "Versão do Makefile: $(VERSION)"
