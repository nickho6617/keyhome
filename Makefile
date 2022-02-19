build:
	docker-compose build

rebuild:
	docker-compose build --force-rm

run:
	docker-compose up -d

migrations:
	docker-compose run --rm web python manage.py makemigrations

migrate:
	docker-compose run --rm web python manage.py migrate

up:
	docker-compose up db web

upall:
	docker-compose up

shell:
	docker-compose exec web /bin/bash

restart:
	docker-compose restart web

stop:
	docker-compose down

stop-clean: ## stops, rms containers, images and volumes
	docker-compose down --rmi all -v --remove-orphans

pytest:
	docker-compose exec web pytest

test:
	docker-compose exec web python manage.py test
