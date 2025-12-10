from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
DEBUG = os.environ.get("DEBUG", "") != "False"

ALLOWED_HOSTS = ["*"]


# --------------------
#   APPS
# --------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'core',
    'accounts',
    'movies',
]


# --------------------
#   MIDDLEWARE
# --------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # STATIC uchun zarur!

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]


# --------------------
#   URL / WSGI
# --------------------
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'


# --------------------
#   TEMPLATES
# --------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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


# --------------------
#   DATABASE
# --------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# --------------------
#   AUTH
# --------------------
AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = 'movies:home'
LOGOUT_REDIRECT_URL = 'movies:home'


# --------------------
#   STATIC FILES
# --------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']   # dev uchun
STATIC_ROOT = BASE_DIR / 'staticfiles'     # render uchun

# Whitenoise optimizatsiya
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# --------------------
#   MEDIA
# --------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# --------------------
#   LOCALE / TIME
# --------------------
LANGUAGE_CODE = 'uz'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True


# --------------------
#   DEFAULTS
# --------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

