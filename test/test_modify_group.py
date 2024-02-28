from model.group import Group

def test_edit_first_group_name(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.create(Group(header="wasd", footer="wasd", name="wasd"))
    app.group.edit_first_group(Group(name='New name'))
    app.session.logout()
