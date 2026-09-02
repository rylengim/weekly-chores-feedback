"""Settings for the production environment."""

from .base import *  # noqa: F403
from .base import (
    comma_separated_environment_variable,
    required_environment_variable,
)

SECRET_KEY = required_environment_variable("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = comma_separated_environment_variable(
    "DJANGO_ALLOWED_HOSTS",
    required_environment_variable("DJANGO_ALLOWED_HOSTS"),
)
DEBUG = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31_536_000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
