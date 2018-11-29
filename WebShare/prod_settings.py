import dj_database_url

from WebShare.settings import *

DEBUG = False

TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SECRET_KEY = get_env_variable('SECRET_KEY', '')

ALLOWED_HOSTS = ['app-webshare.herokuapp.com']