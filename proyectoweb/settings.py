from pathlib import Path
from django.contrib.messages import constants as mensajes_de_error
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde un archivo .env
load_dotenv()

# Definición de rutas
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'valor_por_defecto')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

BASE_URL = 'http://localhost:8003'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',  # Necesario si planeas agregar login social
    # Añadir proveedores sociales según necesites, por ejemplo:
    'allauth.socialaccount.providers.google',
    'widget_tweaks',
    'proyectowebapp',
    'servicios',
    'blog',
    'contacto',
    'tienda',
    'carro',
    'autenticacion',
    'crispy_forms',
    'crispy_bootstrap5',
    'pedidos',
    'rules', 
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Para servir archivos estáticos en producción
    'django.contrib.sessions.middleware.SessionMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Rutas principales
ROOT_URLCONF = 'proyectoweb.urls'

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates'],  # Directorios de plantillas
        'APP_DIRS': True,  # Para buscar plantillas dentro de cada aplicación
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'carro.context_processor.importe_total_carro',  # Procesador de contexto personalizado
            ],
        },
    },
]

# Aplicación WSGI para desplegar el proyecto
WSGI_APPLICATION = 'proyectoweb.wsgi.app'

# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_NAME', 'prueba_db'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', '123456'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}

# Validadores de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # Asegúrate de que este directorio existe
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_IGNORE_PATTERNS = [
    "proyectowebapp/vendor/font-awesome/less/*.less",  # Ignorar archivos .less de FontAwesome
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuracion de contacto
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "tucorreo@gmail.com"
EMAIL_HOST_PASSWORD = "tupassword"

CRISPY_TEMPLATE_PACK = 'bootstrap5'

# Formateo de mensajes de error en el frontend
MESSAGE_TAGS = {
    mensajes_de_error.DEBUG: 'debug',
    mensajes_de_error.INFO: 'info',
    mensajes_de_error.SUCCESS: 'success',
    mensajes_de_error.WARNING: 'warning',
    mensajes_de_error.ERROR: 'danger',
}

AUTHENTICATION_BACKENDS = [
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Redirección después de iniciar o cerrar sesión
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Hacer que el correo electrónico sea único para cada usuario
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECT = True

# Seguridad adicional
SESSION_COOKIE_SECURE = True  # Solo envía cookies en conexiones HTTPS
CSRF_COOKIE_SECURE = True     # Asegura la cookie de CSRF solo para HTTPS
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3  # Expiración de enlaces de confirmación de email

# Configuración de allauth para usar solo nombre de usuario
ACCOUNT_AUTHENTICATION_METHOD = "username_email"  # Autenticación solo con nombre de usuario
ACCOUNT_USERNAME_REQUIRED = True  # Requiere nombre de usuario
ACCOUNT_EMAIL_REQUIRED = True  # requiere correo electrónico

ACCOUNT_LOGOUT_ON_GET = True

# Configuración de rate-limiting para intentos fallidos de inicio de sesión
ACCOUNT_RATE_LIMITS = {
    'login_failed': '5/m',  # Límite de 5 intentos fallidos por minuto
}
