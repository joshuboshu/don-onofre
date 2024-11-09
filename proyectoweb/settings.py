from pathlib import Path
from django.contrib.messages import constants as mensajes_de_error
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde un archivo .env
load_dotenv()

# Definición de rutas
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = os.getenv('SECRET_KEY', 'valor_por_defecto')  # Clave secreta para la producción
DEBUG = False  # Establecer en False para producción
ALLOWED_HOSTS = ['127.0.0.1']  # Hosts permitidos para evitar ataques de DNS spoofing
BASE_URL = 'http://localhost:8000'  # URL base para generar enlaces

# Aplicaciones instaladas
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

# Aplicación WSGI para desplegar el proyecto
WSGI_APPLICATION = 'proyectoweb.wsgi.app'


# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Motor de base de datos
        'NAME': BASE_DIR / "db.sqlite3",  # Archivo de la base de datos SQLite
    }
}

# Validadores de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

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

STATICFILES_IGNORE_PATTERNS = [
    "proyectowebapp/vendor/font-awesome/less/*.less",  # Ignorar archivos .less de FontAwesome
]

# Archivos multimedia (imagenes, videos, etc.)
MEDIA_URL = '/media/'  # URL para acceder a los archivos de medios
MEDIA_ROOT = BASE_DIR / 'media'  # Directorio donde se almacenan los archivos de medios

# Configuración de correo
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "tucorreo@gmail.com"  # Cambia este valor por tu correo real
EMAIL_HOST_PASSWORD = "tupassword"  # Cambia este valor por tu contraseña real

# Formateo de mensajes de error en el frontend
MESSAGE_TAGS = {
    mensajes_de_error.DEBUG: 'debug',
    mensajes_de_error.INFO: 'info',
    mensajes_de_error.SUCCESS: 'success',
    mensajes_de_error.WARNING: 'warning',
    mensajes_de_error.ERROR: 'danger',
}

# Configuración de formularios
CRISPY_TEMPLATE_PACK = 'bootstrap4'  # Paquete de plantillas para formularios con Bootstrap

# Configuración de autenticación
AUTHENTICATION_BACKENDS = (
    'rules.permissions.ObjectPermissionBackend',  # Usar django-rules para permisos de objetos
    'django.contrib.auth.backends.ModelBackend',  # Backend predeterminado para autenticación
)

# Tipo de campo de clave primaria por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
