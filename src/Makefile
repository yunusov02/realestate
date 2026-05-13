


run:
	poetry run python manage.py runserver 0.0.0.0:8000


migrate:
	poetry run python manage.py migrate


createsuperuser:
	poetry run python manage.py createsuperuser

test:
	poetry run python manage.py test


makemigrations:
	poetry run python manage.py makemigrations



default_data:
	poetry run python manage.py default_helper
	poetry run python manage.py default_homes

description:
	@echo "Available commands:"
	@echo "  run             - Run the Django development server"
	@echo "  migrate         - Apply database migrations"
	@echo "  createsuperuser - Create a new superuser account"
	@echo "  test            - Run the test suite"
	@echo "  makemigrations  - Create new database migrations based on changes to models"
	@echo "  description      - Show this help message"
	@echo "  default_data     - Load default data into the database"
	@echo "Usage: make <command>"


