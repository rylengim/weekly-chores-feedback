"""Settings for automated tests and deterministic infrastructure checks."""

import os

from .base import *  # noqa: F403
from .base import comma_separated_environment_variable

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "django-insecure-test-only")
DEBUG = False
ALLOWED_HOSTS = comma_separated_environment_variable(
    "DJANGO_ALLOWED_HOSTS", "testserver,localhost"
)

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
