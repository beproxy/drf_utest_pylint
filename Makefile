.PHONY: setup \
		install \
		db_migrate \
		run \
		black \
		flake8 \
		pylint \
		test

install: venv/bin/activate ## install dependencies
	. venv/bin/activate; pip3 install -r requirements/req_base.txt

db_migrate: venv/bin/activate ## Run migrations
	. venv/bin/activate; python3 backend/manage.py migrate

setup: install db_migrate ## install and run migrations

black: black backend --check --verbose --exclude=migrations

flake8: flake8 backend --exclude=migrations

pylint: pylint backend --ignore=migrations

tests: python3 backend/manage.py test apps.core.tests.OrderTestCase --settings=settings.local

check: flake8 tests

run: check
	python3 manage.py runserver --settings=settings.local