"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os, sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 项目路由
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# django自带的密钥
SECRET_KEY = 'tpl&ehuze0=^lbr5qwr_85++90dw&@v_%8yz2lw7mdp-(7!f04'

# SECURITY WARNING: don't run with debug turned on in production!
# 默认开启debug模式,将来项目上线的时候需要改为false
# 如果将来项目部署上线后,django服务器不再提供对静态文件访问支持,因为Django服务器是动态业务逻辑
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
# 安装或注册Django自带子应用 及第三方或自己创建的子应用

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users.apps.UsersConfig', # 注册子应用
    # 子应用中定义了模型需要迁移时，必须注册子应用，有用到模板也要注册子应用
    'booktest.apps.BooktestConfig', # ORM演示

]

# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'rest_framework',

    'users.middleware.my_middleware',
    'users.middleware.my_middleware2'
]

ROOT_URLCONF = 'demo.urls'

# 模板文件
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

# 部署上线沟工程的启动入口
WSGI_APPLICATION = 'demo.wsgi.application'

# 数据库配置项
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'mysql',  # 数据库用户密码
        'NAME': 'django_demo'  # 数据库名字
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

# 密码配置项
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
# https://docs.djangoproject.com/en/1.11/topics/i18n/
# 工程语言,默认英文,可以修改为简体中文
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'


# 时区,默认世界时间,可以修改为亚洲/上海时区
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# 静态文件访问的路由前缀
STATIC_URL = '/static/'

# 静态文件加载存储目录
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_files'),
    os.path.join(BASE_DIR, 'static_files/test'),
]

MEDIA_ROOT=os.path.join(BASE_DIR,"static_files/media")


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache" # 设置session内存缓存
SESSION_CACHE_ALIAS = "default"
