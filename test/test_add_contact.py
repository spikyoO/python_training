# -*- coding: utf-8 -*-
from fixture.application import Application
from model.contact import Contact

def test_add_contact(app: Application):
    app.contact.create_new_contact(Contact(first_name="John", last_name="Doe", email="john@doe.lost"))
