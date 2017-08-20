import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'utils'))

SECRET_KEY = 'ze&1j4lvfs&(!*q)hj(^%dff2!2w5ik0*oxy3g=7*h6xf17-2$'

# Will be ENCRYPT when push the project in Github

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps
    'account',
    'business',
    'operation',
    'sdiningview',
    'ucenter',
    # utils
    'rest_framework',
    'xadmin',
    'crispy_forms',
    'reversion',
    'django_crontab',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sdining.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sdining.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'account.User'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

APPID = 200513914

# Will be ENCRYPT when push the project to Github

APPKEY = 'WHXYOPENAPIKEY'

# Will be ENCRYPT when push the project to Github

TEMPLATE_ID = 'af40aca07db111e7be1d54520092a308'

REDIRECT_URI = 'http://106.15.195.58/qq/check/'

WRAPPER_MINUTE = 0
# if the WRAPPER_MINUTE = 0 that's means real-time push

ORDER_TIME_ONE = [
    '10,50',
    '11,50'
]

ORDER_TIME_TWO = [
    '15,50',
    '16,50'
]

DEFAULT_PASSWORD = '123321'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
]

LOGIN_URL = '/ucenter/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',  # 文件方式
        'LOCATION': os.path.join(BASE_DIR, 'cache'),
        'TIMEOUT': 600,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

TEMPLATE_BUTTON_URI = 'http://106.15.195.58/ucenter/'

CRONJOBS = [
    ('0 1 * * *', 'cronjob.changeavatar.changeavatar'),
    ('0 1 * * *', 'cronjob.check_order.check_order'),
]