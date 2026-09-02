"""Settings for local development."""

import os

from .base import *  # noqa: F403
from .base import (
    comma_separated_environment_variable,
    required_environment_variable,
)

SECRET_KEY = required_environment_variable("DJANGO_SECRET_KEY")
DEBUG = os.environ.get("DJANGO_DEBUG", "false").lower() in {
    "1",
    "true",
    "yes",
    "on",
}
ALLOWED_HOSTS = comma_separated_environment_variable(
    "DJANGO_ALLOWED_HOSTS", required_environment_variable("DJANGO_ALLOWED_HOSTS")
)
