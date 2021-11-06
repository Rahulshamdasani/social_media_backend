"""
Django settings for backendAPI project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta
import environ
env = environ.Env()
environ.Env.read_env()
DATABASE_URL = env('DATABASE_URL')
print("DBURL+",DATABASE_URL)
# import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m&-r=)iy$$fv1)5$vdmi1#q+9q*s!e_xcibod=^6h_d3hh40*('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # 'rest_framework.authtoken',

    # project apps
    'accounts.apps.AccountsConfig',
    'profiles.apps.ProfilesConfig',
    'posts.apps.PostsConfig',

    # 3rd party
    'corsheaders',
    'rest_framework',
    'djoser',
    'social_django',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'drf_yasg',

]

MIDDLEWARE = [
    'social_django.middleware.SocialAuthExceptionMiddleware', #for google auth
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    # cors headers

    # Hosting middle ware
    'whitenoise.middleware.WhiteNoiseMiddleware',

    "corsheaders.middleware.CorsMiddleware",

    

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTH_USER_MODEL = 'accounts.UserAccount'

# if needed for django.contrib.sites
SITE_ID = 1

# Email settings
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # sends email using console
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # sends email using smtp
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'koobecafteam@gmail.com'
EMAIL_HOST_PASSWORD = 'selftaught'
EMAIL_USE_TLS = True

#           DRF settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication', # JWT auth for drf
        
    ],
    # 'DEFAULT_FILTER_BACKENDS': [
    #     'django_filters.rest_framework.DjangoFilterBackend'], # GLOBAL FILTERING on API
}



SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=240),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken',
    )
}

DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True, # forces retyping password on creation
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True, # change username endpoints will send confirmation email to user
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True, # change password endpoints will send confirmation email to user
    'SEND_CONFIRMATION_EMAIL': True, # send email on account creation
    'SET_USERNAME_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,

    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True, #user will be required to click activation link sent in email after: 1. creating an account, 2. updating their email
    # 'ACTIVATION_URL': 'activation/',
    'ACTIVATION_URL': 'activation/{uid}/{token}',
    'SOCIAL_AUTH_TOKEN_STRATEGY': 'djoser.social.token.jwt.TokenStrategy',
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': [
        'http://localhost:8000/google/',
        'http://localhost:8000/google',
        'http://localhost:8000/',
        'http://localhost:3000/google/',
        # 'http://localhost:3000/google',
        # 'http://localhost:3000/',
    ],
    'SOCIAL_AUTH_LOGIN_URL': 'http://localhost:3000/google/',
    # 'SOCIAL_AUTH_LOGIN_REDIRECT_URL': 'http://localhost:3000/google/',
    # 'SOCIAL_AUTH_NEW_USER_REDIRECT_URL': 'http://localhost:3000/google/',
    'SERIALIZERS': {
        'user_create': 'accounts.serializers.UserCreateSerializer',
        'user': 'accounts.serializers.UserCreateSerializer',
        'current_user': 'accounts.serializers.UserCreateSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    },
}

# DOMAIN = config('DOMAIN') #localhost:8000
# SITE_NAME = config('SITE_NAME') #net


AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend' #needed to make email regularlogin still work
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '61886613583-dstuur9thkogr07e38n3tebugss89sln.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile', 'openid']
# SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['first_name', 'last_name']

###########################################
# CORS Settings  Cross-Origin Resource Sharing https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
# https://www.django-rest-framework.org/topics/ajax-csrf-cors/
# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:8000', # default django port
#     'http://localhost:3000', # default react port
#     'http://127.0.0.1',
#     'https://social-media-frontend-two.vercel.app',
#     # '*', # all
# ]





ROOT_URLCONF = 'backendAPI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates/")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends', #for google auth
                'social_django.context_processors.login_redirect' #for google auth
            ],
        },
    },
]

WSGI_APPLICATION = 'backendAPI.wsgi.application'


CORS_ALLOWED_ORIGINS = [   
    '*',
    'https://social-media-frontend-two.vercel.app',
]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")

STATIC_URL = '/static/'

STATIC_DIRS = [
    os.path.join(BASE_DIR,"static")
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_WHITELIST = 'koobecaffrontend.herokuapp.com',

