# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.create_group(Group(header="wasd", footer="wasd", name="wasd"))
    app.logout()


