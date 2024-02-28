# -*- coding: utf-8 -*-
from fixture.application import Application

def test_del_first_group(app: Application):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()
