import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_admin_login_named_route_returns_success(client):
    response = client.get(reverse("admin:login"))

    assert response.status_code == 200
