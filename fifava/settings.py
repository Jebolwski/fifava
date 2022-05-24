from pathlib import Path

import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-%0$s52dr2w=5jq=fui1xhrnwo__kk#w*x2dvl*j9q*k1q(edh$"


DEBUG = True

ALLOWED_HOSTS = ["fifavox.com","www.fifavox.com","127.0.0.1","fifavox-1.herokuapp.com",'https://fifavox.netlify.app/']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base.apps.BaseConfig',
    'storages',
    'rest_framework',
]


REST_FRAMEWORK = {
    'DATETIME_FORMAT': '%d %B %Y %H:%M',
    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fifava.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fifava.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CSRF_COOKIE_SECURE=True


CORS_ORIGIN_ALLOW_ALL = True
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'tr-TR'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT= os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = '/static/'


MEDIA_ROOT = 'media/'

MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = "587"
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "fifavoxteam@gmail.com"
EMAIL_HOST_PASSWORD = 'ujqxewmwvgriknem'

# SECURE_SSL_REDIRECT = True 

# AWS_ACCESS_KEY_ID = 'AKIA32ZGHYSFVKRESFPD'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'fifavox-s3-buckets-1'
# AWS_S3_FILE_OVERWRITE = False
# AWS_QUERYSTRING_AUTH = False
# AWS_DEFAULT_ACL = None
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'