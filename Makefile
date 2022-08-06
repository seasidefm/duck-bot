SHELL = /bin/bash

install:
	./venv/bin/pip install -r requirements.txt

install-dev:
	./venv/bin/pip install -r requirements-dev.txt

run:
	source .env \
	&& ./venv/bin/python bot.py

fmt:
	./venv/bin/black .