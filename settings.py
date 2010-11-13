'''
localsettings.py (excluded by .gitignore):

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

try:
    from localsettings import *
except ImportError:
    pass


# Add this repo's parent to sys.path
sys.path.append()

## non-Django settings:

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

TYRANT_HOST = '127.0.0.1'
TYRANT_PORT = 7000

EXCEPTION_JABBER = None

def parentOf(path, n=1):
    return '/'.join(path.rstrip('/').split('/')[:-n])

ROOT = parentOf(os.path.abspath(__file__), n=2)

# Add this repo's parent to sys.path
sys.path.append(ROOT)

MAIN_APP = os.environ['APP']

if 'APPS' not in locals():
    APPS = []
APPS += [MAIN_APP]


PJ_PATH = []
for name in os.listdir(ROOT):
    jsDir = '%s/%s/js' % (ROOT, name)
    if os.path.isdir(jsDir):
        PJ_PATH.append(jsDir)


## Django settings:

DEVMODE = True

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


try:
    from localsettings import *
except ImportError:
    pass

