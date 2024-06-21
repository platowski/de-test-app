ARCH := $(shell uname -m)
DOCKER_COMPOSE_FILES := -f ./docker-compose.yml
ifeq ($(ARCH), arm64)
	DOCKER_COMPOSE_FILES := -f ./docker-compose.yml -f ./docker-compose.arm-overrides.yml
endif

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d -delete

init:
	cp src/.env.dist src/.env

build:
	docker-compose ${DOCKER_COMPOSE_FILES} build

up:
	docker-compose ${DOCKER_COMPOSE_FILES} up $(ARGS)

down:
	docker-compose ${DOCKER_COMPOSE_FILES} down --volumes


run_black:
	poetry run blackd

