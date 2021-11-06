# social_media_backend
Creating a private repo to host the Django backend





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



##  Approach 2
pip install django-heroku<br/>

go to settings.py<br/>
At the top write:
import django_heroku
At the end of file
django_heroku.settings(locals())

install whitenoise
add whitenoise middleware
install gunicorn
create Proc file.

### Converting to postgres
pip install dj-database-url

#### In settings.py after the database add this line.
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

go to settings inside heroku and goto app-> settings-> reveal environment variables
and add on fied
SECRET_KEY = SECRET_KEY
Copy the databse url and set it inside environment variables
