import dj_database_url
from decouple import config

from .main import ALLOWED_HOSTS

SERVER_URL = config(
    "SERVER_URL", default="https://qp-for-all-api.onrender.com"
)

CSRF_TRUSTED_ORIGINS = [SERVER_URL]

ALLOWED_HOSTS += [
    SERVER_URL.removeprefix("https://"),  # type: ignore
    "0.0.0.0",
    "localhost",
    "127.0.0.1",
    "[::1]",
]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.parse(
        str(config("DATABASE_URL")),
        conn_max_age=600,
    ),
}
