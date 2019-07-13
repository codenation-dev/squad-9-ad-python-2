from settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$m^o_w&!45yn(45xyp#o%()aak)f6gac3f)4bf9fg$)$6%l0%a'

ALLOWED_HOSTS = []

#Aplicativos externos
EXTERNAL_APPS = [
    'rest_framework',
    # 'rest_framework.authtoken',
]

#Aplicativos internos
INTERNAL_APPS = [
    'vendedor',
    'comission',
    'vendas',
    'notificacoes',
]

INSTALLED_APPS += INTERNAL_APPS + EXTERNAL_APPS

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')