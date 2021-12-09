
release: python manage.py makemigrations
release: python manage.py migrate --no-input

web: gunicorn backendAPI.wsgi 