"""
Django settings for GrupoZero project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from pathlib import Path
from datetime import timedelta
from pathlib import Path
import cloudinary 
import cloudinary_storage 
import cloudinary.uploader
import cloudinary.api
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4em$u+cel9^sve+#bwlqq+_*0+l9^ox5$uj&!3=e6m73+_j=n0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app','127.0.0.1']

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"
# Application definition

INSTALLED_APPS = [
    'admin_confirm',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'crispy_forms',
    'crispy_bootstrap4',
    'rest_framework',
    'axes',
    'cloudinary',
    'cloudinary_storage',
    'captcha',
]


RECAPTCHA_PUBLIC_KEY = '6Ldqs_UpAAAAACE0lsiyBdxT2IDo7jORtalA0rTZ'
RECAPTCHA_PRIVATE_KEY = '6Ldqs_UpAAAAAOBg-yqlhbvGXG3liLyCDBfzwNtX'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_TEMPLATE_PACK = "bootstrap4"

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',
    'django.contrib.auth.backends.ModelBackend',
]




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
]

# CONFIGURACION AXES
AXES_FAILURE_LIMIT = 3 # NUMEROS DE INTENTOS
AXES_COOLOFF_TIME = timedelta(minutes=1)  # TIEMPO DE ANTER DE OTRO INTENTO
AXES_LOCKOUT_URL = '/account_locked/' # RUTA URL DE REDIGIRE CUANDO SE BLOQUEA CUENTA
AXES_RESET_ON_SUCCESS = True # REESTABLECE EL CONTADOR DE INTENTOS FALLIDOS CUANDO SE INGRESA CORRECTAMENTE

ROOT_URLCONF = 'GrupoZero.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'GrupoZero.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'aws-0-us-east-1.pooler.supabase.com',
        'NAME': 'postgres',
        'USER': 'postgres.vsakloqxlmnoldpjfbtw',
        'PASSWORD': 'Xplca5cv.Xplca5cv.123',
        'PORT': '6543'
    }
}
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
# python manage.py collectstatic --upload-unhashed-files
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#CONFIG BINARY
CLOUDINARY_STORAGE = {
    'CLOUD_NAME' : 'dovwxcx21',
    'API_KEY' : '225387741853562',
    'API_SECRET' : 'owoDmG8IHGCaDpVcUY5kzGOCaHg'
}


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import os 
MEDIA_URL = '/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'grupozero2024@gmail.com'
EMAIL_HOST_PASSWORD = 'e je i s t t g u x x s e z t x'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

LOGOUT_REDIRECT_URL = 'inicio'  # Ajusta 'inicio' al nombre de la URL de la página de inicio para clientes
LOGIN_REDIRECT_URL = '/inicio/'

# Configuración para Simple Captcha
CAPTCHA_FONT_SIZE = 30
CAPTCHA_LETTER_ROTATION = (-10, 10)
CAPTCHA_BACKGROUND_COLOR = '#ffffff'
CAPTCHA_FOREGROUND_COLOR = '#001100'
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_dots',)
CAPTCHA_LENGTH = 5
CAPTCHA_TIMEOUT = 5
CAPTCHA_IMAGE_BEFORE_FIELD = True