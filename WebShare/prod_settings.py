import dj_database_url

from WebShare.settings import *

DEBUG = False

TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

SECRET_KEY = '0eg50#9m3cz44#-vdk)u+q_vmkfwy)9psoe@m8k901mra3zim#'

ALLOWED_HOSTS = ['app-webshare.herokuapp.com']