import dj_database_url
import django_heroku

from settings.base2 import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Allow all host headers
ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".herokuapp.com"]

#Aplicativos externos
EXTERNAL_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
]

#Aplicativos internos
INTERNAL_APPS = [
    'vendedor',
    'notificacoes',
    'vendas',
	'comissions',
]

INSTALLED_APPS += INTERNAL_APPS + EXTERNAL_APPS

# Heroku

# Change 'default' database configuration with $DATABASE_URL.
# DATABASES['default'].update(dj_database_url.config(conn_max_age=500, ssl_require=True))
DATABASES = {'default': dj_database_url.config(conn_max_age=500, ssl_require=True)}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
CORS_REPLACE_HTTPS_REFERER     = True
HOST_SCHEME                    = "https://"
SECURE_PROXY_SSL_HEADER        = ("HTTP_X_FORWARDED_PROTO", 'https')
SECURE_SSL_REDIRECT            = True
SESSION_COOKIE_SECURE          = True
CSRF_COOKIE_SECURE             = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS            = 1000000
SECURE_FRAME_DENY              = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "staticfiles")]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
             'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}

django_heroku.settings(locals())
