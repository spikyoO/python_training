# -*- coding: utf-8 -*-
from fixture.application import Application
from model.contact import Contact
import time

def test_add_contact(app: Application):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    time.sleep(5)
    app.contact.create_new_contact(Contact(first_name="John", last_name="Doe", email="john@doe.lost"))
    time.sleep(5)
    app.session.logout()