# Weekly Chores Feedback

An infrastructure-only Django foundation for a shared household chores tool.
The project currently contains empty `accounts`, `households`, `chores`, and
`notifications` apps, Django's built-in admin, and PostgreSQL configuration.

## Prerequisites

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/)
- PostgreSQL running locally

## Clean-checkout setup

Create a local PostgreSQL role and two databases. `--pwprompt` asks you to set
the role's password, while `--createdb` lets pytest-django create and remove its
own isolated database. `--owner` assigns each database to that role.

```sh
createuser --pwprompt --createdb weekly_chores
createdb --owner=weekly_chores weekly_chores
createdb --owner=weekly_chores weekly_chores_test
```

Export the application settings. Replace the example password and secret key
with local-only values. These exports affect only the current terminal.

```sh
export DJANGO_SETTINGS_MODULE=config.settings.local
export DJANGO_SECRET_KEY='replace-with-a-local-only-secret'
export DJANGO_ALLOWED_HOSTS='localhost,127.0.0.1'
export POSTGRES_DB=weekly_chores
export POSTGRES_USER=weekly_chores
export POSTGRES_PASSWORD='the-password-entered-above'
export POSTGRES_HOST=127.0.0.1
export POSTGRES_PORT=5432
export DJANGO_DEBUG=true
export DJANGO_LOG_LEVEL=INFO
```

`DJANGO_DEBUG` and `DJANGO_LOG_LEVEL` are optional. All other variables above
are required for local setup. `.env.example` is a reference only; the project
does not load `.env` files automatically.

Install the exact locked dependencies and apply Django's built-in migrations:

```sh
# --locked fails instead of silently changing uv.lock.
uv sync --locked
uv run python manage.py migrate --noinput
```

Start Django's development server at <http://127.0.0.1:8000/>. Stop it with
Ctrl+C.

```sh
uv run python manage.py runserver
```

`manage.py` is the supported application entry point. The previous placeholder
console program has been removed.

## Checks and tests

The test settings always use PostgreSQL. Point them at the dedicated test
database before running checks. pytest-django creates an additional isolated
database from this connection and removes it after the test run.

```sh
export DJANGO_SETTINGS_MODULE=config.settings.test
export POSTGRES_DB=weekly_chores_test

uv run python manage.py check --settings=config.settings.test
uv run python manage.py migrate --noinput --settings=config.settings.test
uv run python manage.py migrate --check --settings=config.settings.test
uv run python manage.py makemigrations --check --dry-run --settings=config.settings.test
uv run python manage.py collectstatic --noinput --settings=config.settings.test
uv run pytest tests/test_home.py
uv run pytest
uv run ruff format --check .
uv run ruff check .
```

`migrate --check` fails when migrations remain unapplied. The `makemigrations`
command uses `--check` to fail on model changes without migration files and
`--dry-run` to prevent it from writing files.

## Environment variables

| Variable | Required | Purpose |
| --- | --- | --- |
| `DJANGO_SETTINGS_MODULE` | Yes | Selects `local`, `test`, `staging`, or `production` settings. |
| `DJANGO_SECRET_KEY` | Yes for local, staging, and production | Cryptographic signing key; staging and production reject a missing value. |
| `DJANGO_ALLOWED_HOSTS` | Yes for local, staging, and production | Comma-separated hostnames accepted by Django; staging and production reject an empty value. |
| `POSTGRES_DB` | Yes | PostgreSQL database name. Use a dedicated database with test settings. |
| `POSTGRES_USER` | Yes | PostgreSQL role name. |
| `POSTGRES_PASSWORD` | Yes | PostgreSQL role password. |
| `POSTGRES_HOST` | Yes | PostgreSQL server hostname. |
| `POSTGRES_PORT` | Yes | PostgreSQL server port, normally `5432`. |
| `DJANGO_DEBUG` | No | Enables local debug mode when set to `true`, `1`, `yes`, or `on`. |
| `DJANGO_LOG_LEVEL` | No | Console log level; defaults to `INFO`. |

Never commit `.env` files or real credentials. Test and CI secret values are
deliberately non-secret and must not be reused outside those environments.
