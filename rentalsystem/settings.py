"""
Django settings for rentalsystem project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import pymysql
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e_hcodqvll3t$%l1!!^%n01kp-7f6g^i93!3dp%(ryi^4b7wtr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0:8000', 'localhost']

CORS_ORIGIN_WHITELIST = (
    'http://*',
)
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)
# Application definition

MEDIA_ROOT = os.path.join(BASE_DIR, 'images/')

MEDIA_URL = '/images/'  # 这个是在浏览器上访问该上传文件的url的前缀

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'account',
]

MIDDLEWARE = [
    # 'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rentalsystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'rentalsystem.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOSR': '127.0.0.1',
        'NAME': 'Cabin',
        'USER': 'cabin',
        'PORT': '3306',
        'PASSWORD': 'cabinmysql2020'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_COOKIE_NAME = "sessionid"       # Session的cookie保存在浏览器上时的key
SESSION_COOKIE_PATH = "/"               # Session的cookie保存的路径(默认)
SESSION_COOKIE_DOMAIN = None            # Session的cookie保存的域名(默认)
SESSION_COOKIE_SECURE = False           # 是否Https传输cookie
SESSION_COOKIE_HTTPONLY = True          # 是否Session的cookie只支持http传输(默认)
SESSION_COOKIE_AGE = 1209600            # Session的cookie失效日期(2周)(默认)
SESSION_SAVE_EVERY_REQUEST = False      # 是否设置关闭浏览器使得Session过期
SESSION_COOKIE_AT_BROWSER_CLOSE = False  # 是否每次请求都保存Session，默认修改之后才能保存
