from selenium.webdriver.common.by import By

class ContactHelper:
    def __init__(self, app, group):
        self.app = app
        self.group = group
    
    def open_contact_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "add new").click()

    def fill_contact_form(self, contact):
        self.group.change_field_value("firstname", contact.first_name)
        self.group.change_field_value("lastname", contact.last_name)
        self.group.change_field_value("email", contact.email)
    
    def create_new_contact(self, contact):
        driver = self.app.driver
        self.open_contact_page()
        self.fill_contact_form(contact)
        driver.find_element(By.NAME, "submit").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "home page").click()
        