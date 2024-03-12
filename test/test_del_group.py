# -*- coding: utf-8 -*-
from fixture.application import Application
from model.group import Group


def test_del_first_group(app: Application):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
