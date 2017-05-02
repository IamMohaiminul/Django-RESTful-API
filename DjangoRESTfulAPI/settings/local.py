from DjangoRESTfulAPI.settings.base import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd7l2-m%ppif%cv-dp32lsqmxtp%wc!yeiw5ks#rw83v&6q%2y3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DjangoRESTfulAPI',
        'USER': 'root',
        'PASSWORD': 'admin',
        'OPTIONS': {
            'charset': 'utf8mb4'
        },
        'TEST': {
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci'
        }
    }
}