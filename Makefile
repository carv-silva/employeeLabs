run:
	python manage.py runserver 0.0.0.0:21256

sk:
	python generationSecureKey.py

ti:
	python manage.py makemigrations

te:
	python manage.py migrate

usr:
	python manage.py createsuperuser
	
migration:
	rm -rf api/migrations
	@echo "Migrações de banco excluídas"

