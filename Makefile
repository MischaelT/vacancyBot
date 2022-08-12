SHELL := /bin/bash

run:
	python3 app/main.py	

build:
	sudo docker-compose up -d --build

stop:
	sudo docker-compose down

workers:
	cd app && celery -A tasks worker -l info -B

rabbit_start:
	service rabbitmq-server start

rabbit_stop:
	service rabbitmq-server stop

rabbit_restart:
	service rabbitmq-server restart

rabbit_status:
	service rabbitmq-server status