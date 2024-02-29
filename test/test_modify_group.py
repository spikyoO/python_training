from fixture.application import Application
from model.group import Group

def test_edit_first_group_name(app: Application):
    app.group.create(Group(header="wasd", footer="wasd", name="wasd"))
    app.group.edit_first_group(Group(name='New name'))

