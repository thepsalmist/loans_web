from .base import *

DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = ["209.97.140.84", "www.pesapointfinserve.com", "pesapointfinserve.com"]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": "",
    }
}
