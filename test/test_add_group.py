# -*- coding: utf-8 -*-
from fixture.application import Application
from model.group import Group


def test_add_group(app: Application):
    old_groups = app.group.get_group_list()
    app.group.create(Group(header="wasd", footer="wasd", name="wasd"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app: Application):
    old_groups = app.group.get_group_list()
    app.group.create(Group(header="", footer="", name=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
