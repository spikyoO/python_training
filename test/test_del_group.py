# -*- coding: utf-8 -*-
from model.group import Group

def test_del_first_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()
