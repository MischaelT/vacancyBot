SHELL := /bin/bash

run:
	python3 app/main.py	

build:
	sudo docker-compose up -d --build

stop:
	sudo docker-compose down