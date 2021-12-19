# social_media_backend
Creating a private repo to host the Django backend

44966023 this branch is deployed 
Django backend at : https://koobecaff.herokuapp.com/admin/



### Backend
create virtual env : python3 -m venv <name>
activate virtual env : source name/bin/activate
pipenv install :   as it is
make migrations  : python manage.py makemigrations
migrate:          python manage.py migrate


## Enabling cors headers form backend
$$ <code>pip install django-cors-headers </code>

in the installed apps add:
<code> ...

   'corsheaders',

   ...</code>

In the middleware add:
<code>
'django.middleware.security.SecurityMiddleware',
  ...
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'corsheaders.middleware.CorsMiddleware',</code>

In settings.py add:
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
  'http://localhost:8000',
)
