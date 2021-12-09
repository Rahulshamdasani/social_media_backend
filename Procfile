
release: python manage.py makemigrations--run-syncdb
release: python manage.py migrate --no-input

web: gunicorn backendAPI.wsgi 