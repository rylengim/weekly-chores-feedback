from pathlib import Path


def test_project_apps_are_registered(settings):
    project_apps = {
        "accounts.apps.AccountsConfig",
        "households.apps.HouseholdsConfig",
        "chores.apps.ChoresConfig",
        "notifications.apps.NotificationsConfig",
    }

    assert project_apps <= set(settings.INSTALLED_APPS)


def test_database_backend_is_postgresql(settings):
    assert settings.DATABASES["default"]["ENGINE"] == "django.db.backends.postgresql"


def test_generated_static_and_media_directories_are_separate(settings):
    assert Path(settings.STATIC_ROOT).parent == Path(settings.MEDIA_ROOT).parent
    assert settings.STATIC_ROOT != settings.MEDIA_ROOT


def test_logging_uses_console_without_file_handlers(settings):
    handlers = settings.LOGGING["handlers"]

    assert handlers == {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
        }
    }
    assert settings.LOGGING["root"]["level"] == "INFO"
