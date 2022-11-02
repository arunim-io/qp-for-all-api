import dj_database_url

from .main import ALLOWED_HOSTS, BASE_DIR

ALLOWED_HOSTS += ["0.0.0.0"]  # type: ignore

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
