# -*- coding: utf-8 -*-
from fixture.application import Application
from model.group import Group


def test_del_first_group(app: Application):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.delete_first_group()
