from pathlib import Path
from django.contrib.messages import constants as mensajes_de_error
from dotenv import load_dotenv
import os

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'valor_por_defecto')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']

BASE_URL = 'http://localhost:8000'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'proyectowebapp',
    'servicios',
    'blog',
    'contacto',
    'tienda',
    'carro',
    'autenticacion',
    'crispy_forms',
    'crispy_bootstrap4',
    'pedidos',
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
]

ROOT_URLCONF = 'proyectoweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'carro.context_processor.importe_total_carro',
            ],
        },
    },
]

WSGI_APPLICATION = 'proyectoweb.wsgi.app'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.zxrqnoxgqkipburpslng',
        'PASSWORD': os.getenv("SUPABASE_PASSWORD"),
        'HOST': os.getenv("SUPABASE_HOST"),
        'PORT': '6543',
        'OPTIONS': {
            "sslmode": 'verify-full',
            'sslrootcert': os.path.join(BASE_DIR, 'prod-ca-2021.crt'),
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_IGNORE_PATTERNS = [
    "proyectowebapp/vendor/font-awesome/less/*.less",
]

MEDIA_URL = '/media/'
# /data/web/media
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuracion de contacto
EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST="smpt.gmail.com"
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER="tucorreo@gmail.com"
EMAIL_HOST_PASSWORD="tupassword"

CRISPY_TEMPLATE_PACK='bootstrap4'

MESSAGE_TAGS = {
    mensajes_de_error.DEBUG: 'debug',
    mensajes_de_error.INFO: 'info',
    mensajes_de_error.SUCCESS: 'success',
    mensajes_de_error.WARNING: 'warning',
    mensajes_de_error.ERROR: 'danger',
}

# Configuración de AdamsPay
ADAMSPAY_API_KEY = os.getenv('ADAMSPAY_API_KEY')
ADAMSPAY_API_SECRET = os.getenv('ADAMSPAY_API_SECRET')
ADAMSPAY_WEBSITE_SLUG = os.getenv('ADAMSPAY_WEBSITE_SLUG')