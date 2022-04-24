from settings.base import *  # noqa 403


SECRET_KEY = os.getenv("SECRET_KEY", "kjhsfjkhsdkfsjkdfskjdfjksf")  # noqa F405

DEBUG = True

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")  # noqa F405

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.postgresql_psycopg2"),  # noqa F405
        "HOST": os.getenv("DB_HOST", "localhost"),  # noqa F405
        "PORT": int(os.getenv("DB_PORT", 5432)),  # noqa F405
        "NAME": os.getenv("DB_NAME", "stackt_db"),  # noqa F405
        "USER": os.getenv("DB_USER", "stackt"),  # noqa F405
        "PASSWORD": os.getenv("DB_PASSWORD", "stackt"),  # noqa F405
        "TEST": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "db.sqlite3",
        },
    },
}
