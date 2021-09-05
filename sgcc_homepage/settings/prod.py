import json
import pymysql

from .base import *

pymysql.install_as_MySQLdb()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
CONFIG_SECRET_DIR = os.path.join(BASE_DIR, '.config/secret_key')

with open(os.path.join(CONFIG_SECRET_DIR, 'settings.json')) as f:
    config_secret_str = f.read()

# json to dict
config_secret = json.loads(config_secret_str)

SECRET_KEY = config_secret["django"]["secret_key"]

# ALLOWED_HOSTS = [
#     'Sgcchomepage-env.eba-q2kwnmyp.ap-northeast-2.elasticbeanstalk.com',
#     'sgcchomepage-env.eba-q2kwnmyp.ap-northeast-2.elasticbeanstalk.com',
#     '127.0.0.1'
# ]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DB = 'sqlite'

if DB == 'sqlite':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


if DB == 'mysql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'sgcc_test',
            'USER': 'root',
            'PASSWORD': 'rlagPfls0117*',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }