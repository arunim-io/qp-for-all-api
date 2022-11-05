import dj_database_url
from decouple import config

from .main import ALLOWED_HOSTS, BASE_DIR

SERVER_URL = config("SERVER_URL", cast=str)

ALLOWED_HOSTS += ["0.0.0.0", SERVER_URL]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default="postgresql://postgres:postgres@localhost:5432/mysite",
        conn_max_age=600,
    )
}

STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
