from decouple import config

from .main import ALLOWED_HOSTS, BASE_DIR

SERVER_URL = config(
    "SERVER_URL", default="https://qp-for-all-api.onrender.com"
)

ALLOWED_HOSTS += [
    SERVER_URL,
    "0.0.0.0",
    "localhost",
    "127.0.0.1",
    "[::1]",
]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("DB_NAME"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "OPTIONS": {
            "ssl": {
                "ca": config("MYSQL_ATTR_SSL_CA"),
            },
        },
    }
}
