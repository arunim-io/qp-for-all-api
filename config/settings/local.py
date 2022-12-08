from .main import ALLOWED_HOSTS, BASE_DIR

ALLOWED_HOSTS += ["*"]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

MEDIA_URL = "http://192.168.0.9:8000/uploads/"
