from .base import *


SECRET_KEY = os.getenv("SECRET_KEY", "kjhsfjkhsdkfsjkdfskjdfjksf")

DEBUG = True

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.postgresql_psycopg2"),  # noqa E501
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": int(os.getenv("DB_PORT", 5432)),
        "NAME": os.getenv("DB_NAME", "stackt_db"),
        "USER": os.getenv("DB_USER", "stackt"),
        "PASSWORD": os.getenv("DB_PASSWORD", "stackt"),
    }
}
