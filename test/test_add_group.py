# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.create(Group(header="wasd", footer="wasd", name="wasd"))
    app.session.logout()


