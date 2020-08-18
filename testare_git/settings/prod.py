from testare_git.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

ADMINS = ['Cristian Duluman', 'cristian.duluman@gmail.com']

SERVER_EMAIL = 'cristian.duluman@gmail.com'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django_logs.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}


STATIC_ROOT = os.path.join(BASE_DIR, 'static')

IS_PRODUCTION = True
