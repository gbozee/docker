
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'postgis',
        'USER': 'postgis',
        'PASSWORD':'postgis',
        'HOST': '127.0.0.1',
    },
}

MEDIA_ROOT = '/srv/geodjango/media'
STATIC_ROOT = '/srv/geodjango/static'

LOGGING = {
        'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': 
            '%(asctime)s:%(name)s.%(funcName)s:%(lineno)d: %(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/srv/geodjango/log/django.log',
            'formatter': 'verbose',
            'maxBytes' : 1048576,
            'backupCount': 3,
        },
    },
    'loggers': {
        '':{
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
