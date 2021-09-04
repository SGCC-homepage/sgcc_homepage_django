import json

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
CONFIG_SECRET_DIR = os.path.join(BASE_DIR, '.config/secret_key')

with open(os.path.join(CONFIG_SECRET_DIR, 'settings.json')) as f:
    config_secret_str = f.read()

# json to dict
config_secret = json.loads(config_secret_str)

SECRET_KEY = config_secret["django"]["secret_key"]