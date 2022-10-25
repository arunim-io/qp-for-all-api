import dj_database_url
from decouple import config

from .main import ALLOWED_HOSTS, BASE_DIR

if RENDER_EXTERNAL_HOSTNAME := config(
    "RENDER_EXTERNAL_HOSTNAME", cast=str, default=None
):
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

DATABASES = {
    "default": dj_database_url.config(
        default="postgresql://postgres:postgres@localhost:5432/qp-for-all",
        conn_max_age=600,
    )
}

STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
