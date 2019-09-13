"""
- If you want to profiling any thing here for production you can do
- Have to remove/overwrite the the settings profiling like 'DEBUG = False' and add here

"""
from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'practice',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
