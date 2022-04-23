.PHONY: setup \
		install \
		db_migrate \
		run

db_migrate: venv/bin/activate ## Run migrations
	. venv/bin/activate; python3 manage.py migrate

install: venv/bin/activate ## install dependencies
	. venv/bin/activate; pip3 install -r requirements/req_base.txt

setup: install db_migrate ## install and run migrations

run:
	python3 manage.py runserver --settings=settings.local