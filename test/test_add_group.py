# -*- coding: utf-8 -*-
from fixture.application import Application
from model.group import Group

def test_add_group(app: Application):
    app.group.create(Group(header="wasd", footer="wasd", name="wasd"))



