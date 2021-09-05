import json
import pymysql
import django

from .base import *

pymysql.install_as_MySQLdb()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
CONFIG_SECRET_DIR = os.path.join(BASE_DIR, '.config')

with open(os.path.join(CONFIG_SECRET_DIR, 'settings.json')) as f:
    config_secret_str = f.read()

# json to dict
config_secret = json.loads(config_secret_str)

print(config_secret["django"]["secret_key"])

SECRET_KEY = config_secret["django"]["secret_key"]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DB = 'mysql'

if DB == 'sqlite':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


if DB == 'mysql':
    DATABASES = config_secret["django"]["databases"]

API_URI = 'http://sgcc.me'

django.setup()
