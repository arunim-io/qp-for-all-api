from .main import ALLOWED_HOSTS, BASE_DIR

SERVER_URL = "http://localhost:8000"

ALLOWED_HOSTS += ["*"]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
