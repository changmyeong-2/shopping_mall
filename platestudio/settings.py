"""
Django settings for platestudio project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os, json #json을 읽어오기 위해 json을 추가해 줍니다.
from django.core.exceptions import ImproperlyConfigured #예외 처리를 위해 불러와줍니다.

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v(*06*l9c^75)3hjy4%p*3f5!1#5w=t58^=yy%60heer@rl(es'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    'search_app',
    'cart',
    'account',
    'stripe',
    'order',
    'board',
    'manager',
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

ROOT_URLCONF = 'platestudio.urls'

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
                'shop.context_processors.menu_links',
                'cart.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'platestudio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STRIPE_PUBLIC_KEY = 'pk_test_51K7VT5LLVT7jJqUXq14dZyw86CzMOsdAtB6n65K2b4seBXKG9Qs2kcMWwWh0nskIb3LHhAKXliicZF1qPkmwdkXl0089mMXcMK'
STRIPE_SECRET_KEY = 'sk_test_51K7VT5LLVT7jJqUXeErxtAmawVNGsH8bWHEB7xlu7NfBpXflGImGC6Uvll4DQoRqnZLVz6ByuXhwXxe9oX6k20S700dYTyzmSx'

LOGGING = {
    'version': 1,
    # 기존의 로깅 설정을 비활성화 할 것인가?
    'disable_existing_loggers': False,

    # 포맷터
    # 로그 레코드는 최종적으로 텍스트로 표현됨
    # 이 텍스트의 포맷 형식 정의
    # 여러 포맷 정의 가능
    'formatters': {
        'format1': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
        'format2': {
            'format': '%(levelname)s %(message)s'
        },
    },

    # 핸들러
    # 로그 레코드로 무슨 작업을 할 것인지 정의
    # 여러 핸들러 정의 가능
    'handlers': {
        # 로그 파일을 만들어 텍스트로 로그레코드 저장
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/logs.html'),
            'formatter': 'format1',
        },
        # 콘솔(터미널)에 출력
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'format2',
        }
    },

    # 로거
    # 로그 레코드 저장소
    # 로거를 이름별로 정의
    'loggers': {
        'shop': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
        'search_app' : {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
        'cart' : {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
        'account' : {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
        'stripe' : {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
        'order' : {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
        'board' : {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
       
    },


}