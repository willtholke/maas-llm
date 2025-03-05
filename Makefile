.PHONY: install shell run migrate createsuperuser test

run:
	pipenv run python manage.py runserver

kill:
	@pkill -f "manage.py runserver" || echo "No Django server running"

restart:
	@$(MAKE) kill
	@$(MAKE) run

migrate:
	pipenv run python manage.py migrate

createsuperuser:
	pipenv run python manage.py createsuperuser

test:
	pipenv run python manage.py test
