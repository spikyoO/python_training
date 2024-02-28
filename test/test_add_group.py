# -*- coding: utf-8 -*-
from fixture.application import Application
from model.group import Group

def test_add_group(app: Application):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.create(Group(header="wasd", footer="wasd", name="wasd"))
    app.session.logout()


