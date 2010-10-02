'''
localsettings.py:

EXCEPTION_JABBER = {
    'to_account': '',
    'from_account': '',
    'from_password': '',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
    }
}
'''

import os


## non-Django settings:

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

TYRANT_HOST = '127.0.0.1'
TYRANT_PORT = 7000

EXCEPTION_JABBER = None

def parentOf(path):
    return '/'.join(path.rstrip('/').split('/')[:-1])

ROOT = parentOf(parentOf(os.path.abspath(__file__)))

MAIN_APP = os.environ['APP']

APPS = [
    MAIN_APP,
    'util_app',
]


## Django settings:

DEBUG = True
ROOT_URLCONF = '%s.urls' % MAIN_APP

LANGUAGE_CODE = 'en-us'
USE_I18N = True
SECRET_KEY = 'fxYycFdp3BchBgwRRuvnSyV8'

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MIDDLEWARE_CLASSES = [
    
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    
    'dev_deployment.middleware.ExceptionsMiddleware',
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)
TEMPLATE_DIRS = []
for app in APPS:
    path = os.path.join(ROOT, app, 'templates')
    if os.path.isdir(path):
        TEMPLATE_DIRS.append(path)


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
] + APPS

TEMPLATE_DEBUG = DEBUG
MANAGERS = ADMINS


from localsettings import *
