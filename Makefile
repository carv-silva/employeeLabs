run:
	python manage.py runserver 0.0.0.0:21256

sk:
	python generationSecureKey.py

ti:
	python manage.py makemigrations
	python manage.py makemigrations employees


te:
	python manage.py migrate

usr:
	python manage.py createsuperuser

migration:
	rm -rf employees/migrations
	@echo "Migrações de banco excluídas"
	
db:
	rm -rf employees/db.sqlite3
	@echo "banco excluído"
