"""
Django settings for SciLog project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.environ.get('SECRET_KEY', 'DEVELOPMENT_SECRET_KEY')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split()

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'users',
    'projects',
    'protocols',
    'invitations',
    'mailjet_rest'
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

ROOT_URLCONF = 'SciLog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'SciLog/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'SciLog.wsgi.application'

AUTH_USER_MODEL = 'users.User'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ.get('DATABASE_NAME', 'scilog'),
        'USER': os.environ.get('DATABASE_USER', 'scilog'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'scilog'),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'SciLog/static'),
]
STATIC_URL = os.environ.get('STATIC_URL', '/static/')
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))

MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))

LOGIN_URL = 'login_user'
LOGIN_REDIRECT_URL = 'projects_list'
LOGOUT_REDIRECT_URL = 'login_user'
REGISTER_URL = 'reguster_user'
REGISTER_REDIRECT_URL = 'projects_list'

# Social auth settings
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
)
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_SANITIZE_REDIRECTS = True
if not(DEBUG):
    SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/project/list'
SOCIAL_AUTH_LOGIN_URL = '/'

# Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY',)
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

# Mailjet API Keys
MJ_APIKEY_PUBLIC = os.environ.get('MJ_APIKEY_PUBLIC')
MJ_APIKEY_PRIVATE = os.environ.get('MJ_APIKEY_PRIVATE')
MJ_TPL_ERROR_REPORTING_MAIL = os.environ.get('MJ_TPL_ERROR_REPORTING_MAIL')

MJ_INVITATION_TEMPLATE_ID = os.environ.get('MJ_INVITATION_TEMPLATE_ID')
MJ_INVITATION_FROM = os.environ.get('MJ_INVITATION_FROM')
MJ_EMAIL_CONFIRMATION_TEMPLATE_ID = os.environ.get('MJ_EMAIL_CONFIRMATION_TEMPLATE_ID')
MJ_EMAIL_CONFIRMATION_FROM = os.environ.get('MJ_EMAIL_CONFIRMATION_FROM')

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER',)
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SERVER_EMAIL = os.environ.get('SERVER_EMAIL')

ADMINS = [tuple(x.split('|')) for x in os.environ.get('ADMINS', '').split(';')]


LOGGING_DIR = os.environ.get('LOGGING_DIR', os.path.join(BASE_DIR, 'log'))

if not os.path.exists(LOGGING_DIR):
    os.mkdir(LOGGING_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s|%(asctime)s|%(pathname)s|%(message)s'
        },
        'simple': {
            'format': '[%(asctime)s] %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'file_debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 10,
            'filters': ['require_debug_true'],
            'filename': os.path.join(LOGGING_DIR, "debug.log"),
            'formatter': 'simple',
        },
        'file_info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 10,
            'filename': os.path.join(LOGGING_DIR, "info.log"),
            'formatter': 'verbose',
        },
        'file_warning': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 10,
            'filename': os.path.join(LOGGING_DIR, "warning.log"),
            'formatter': 'verbose',
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 10,
            'filename': os.path.join(LOGGING_DIR, "error.log"),
            'formatter': 'verbose',
        },
        'file_critical': {
            'level': 'CRITICAL',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 10,
            'filename': os.path.join(LOGGING_DIR, "critical.txt"),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'scilog': {
            'handlers': ['file_debug', 'file_info', 'file_warning', 'file_error', 'file_critical'],
            'level': 'DEBUG',
        },
    }
}
