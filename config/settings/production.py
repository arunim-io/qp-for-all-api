import dj_database_url
from decouple import config

from .main import ALLOWED_HOSTS, MIDDLEWARE

SERVER_HOST = config("SERVER_HOST", default="qp-for-all-api.fly.dev")

SERVER_URL = f"https://{SERVER_HOST}"

CSRF_TRUSTED_ORIGINS = [SERVER_URL]

ALLOWED_HOSTS += [
    SERVER_HOST,
    "0.0.0.0",
    "localhost",
    "127.0.0.1",
    "[::1]",
]

MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.parse(
        str(config("DATABASE_URL")), conn_max_age=600
    ),
}

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": config("DJANGO_LOG_LEVEL", default="INFO"),
            "propagate": False,
        },
    },
}
