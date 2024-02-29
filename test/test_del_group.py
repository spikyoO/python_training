# -*- coding: utf-8 -*-
from fixture.application import Application

def test_del_first_group(app: Application):
    app.group.delete_first_group()
