import dj_database_url
from decouple import config

from .main import ALLOWED_HOSTS, BASE_DIR

SERVER_URL = config("SERVER_URL", cast=str)

ALLOWED_HOSTS += [
    SERVER_URL,
    "0.0.0.0",
    "localhost",
    "127.0.0.1",
    "[::1]",
]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


try:
    DATABASE_URL: str = config("DATABASE_URL")  # type: ignore
    DATABASE = dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600,
    )
except Exception:
    DATABASE = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }

DATABASES = {
    "default": DATABASE,
}
