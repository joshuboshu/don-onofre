from pathlib import Path
from django.contrib.messages import constants as mensajes_de_error
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde un archivo .env
load_dotenv()

# Definición de rutas
BASE_DIR = Path(__file__).resolve().parent.parent

<<<<<<< HEAD
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'valor_por_defecto')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.tu-dominio.vercel.app']

BASE_URL = 'http://localhost:8000'

# Application definition

=======
# Seguridad
SECRET_KEY = os.getenv('SECRET_KEY', 'valor_por_defecto')  # Clave secreta para la producción
DEBUG = True  # Establecer en False para producción
ALLOWED_HOSTS = ['127.0.0.1']  # Hosts permitidos para evitar ataques de DNS spoofing
BASE_URL = 'http://localhost:8000'  # URL base para generar enlaces

# Aplicaciones instaladas
>>>>>>> origin/docker
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
    'rules', 
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Para servir archivos estáticos en producción
    'django.contrib.sessions.middleware.SessionMiddleware',
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

<<<<<<< HEAD
WSGI_APPLICATION = 'proyectoweb.wsgi.application'
=======
# Aplicación WSGI para desplegar el proyecto
WSGI_APPLICATION = 'proyectoweb.wsgi.app'

>>>>>>> origin/docker

# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
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

<<<<<<< HEAD
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
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
=======
# Internacionalización y zona horaria
LANGUAGE_CODE = 'es-es'  # Configuración de idioma
TIME_ZONE = 'UTC'  # Configuración de zona horaria
USE_I18N = True  # Habilitar traducciones
USE_TZ = True  # Habilitar soporte para zonas horarias
SITE_ID = 1

# Archivos estáticos (CSS, JavaScript, imágenes)
STATIC_URL = '/static/'  # URL de los archivos estáticos
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Directorios adicionales de archivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Directorio de salida de los archivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # Uso de WhiteNoise para producción
>>>>>>> origin/docker

STATICFILES_IGNORE_PATTERNS = [
    "proyectowebapp/vendor/font-awesome/less/*.less",  # Ignorar archivos .less de FontAwesome
]

<<<<<<< HEAD
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuracion de contacto
=======
# Archivos multimedia (imagenes, videos, etc.)
MEDIA_URL = '/media/'  # URL para acceder a los archivos de medios
MEDIA_ROOT = BASE_DIR / 'media'  # Directorio donde se almacenan los archivos de medios

# Configuración de correo
>>>>>>> origin/docker
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
<<<<<<< HEAD
EMAIL_HOST_USER = "tucorreo@gmail.com"
EMAIL_HOST_PASSWORD = "tupassword"

CRISPY_TEMPLATE_PACK = 'bootstrap4'
=======
EMAIL_HOST_USER = "tucorreo@gmail.com"  # Cambia este valor por tu correo real
EMAIL_HOST_PASSWORD = "tupassword"  # Cambia este valor por tu contraseña real
>>>>>>> origin/docker

# Formateo de mensajes de error en el frontend
MESSAGE_TAGS = {
    mensajes_de_error.DEBUG: 'debug',
    mensajes_de_error.INFO: 'info',
    mensajes_de_error.SUCCESS: 'success',
    mensajes_de_error.WARNING: 'warning',
    mensajes_de_error.ERROR: 'danger',
}

<<<<<<< HEAD
AUTHENTICATION_BACKENDS = (
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)
=======
# Configuración de formularios
CRISPY_TEMPLATE_PACK = 'bootstrap4'  # Paquete de plantillas para formularios con Bootstrap

# Configuración de autenticación
AUTHENTICATION_BACKENDS = (
    'rules.permissions.ObjectPermissionBackend',  # Usar django-rules para permisos de objetos
    'django.contrib.auth.backends.ModelBackend',  # Backend predeterminado para autenticación
)

# Tipo de campo de clave primaria por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
>>>>>>> origin/docker
