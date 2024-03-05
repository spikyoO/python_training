import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


class ContactHelper:
    def __init__(self, app, group):
        self.app = app
        self.group = group
    
    def open_contact_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "add new").click()
        with allure.step("Opening contacts page"):
            allure.attach(self.app.driver.get_screenshot_as_png(),
                          name="ContactsPage",
                          attachment_type=AttachmentType.PNG)

    def fill_contact_form(self, contact):
        self.group.change_field_value("firstname", contact.first_name)
        self.group.change_field_value("lastname", contact.last_name)
        self.group.change_field_value("email", contact.email)
        with allure.step(f"Filling contact's creation form: name - {contact.first_name}, lastname - {contact.last_name}, email - {contact.email}"):
            allure.attach(self.app.driver.get_screenshot_as_png(),
                          name="ContactForm",
                          attachment_type=AttachmentType.PNG)

    @allure.feature("Contacts")
    @allure.story("Creating a contact")
    def create_new_contact(self, contact):
        driver = self.app.driver
        self.open_contact_page()
        self.fill_contact_form(contact)
        driver.find_element(By.NAME, "submit").click()
        with allure.step("Contact created"):
            allure.attach(self.app.driver.get_screenshot_as_png(),
                          name="ContactCreated",
                          attachment_type=AttachmentType.PNG)
        self.return_to_home_page()

    def return_to_home_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "home page").click()
        with allure.step("Returned to the home page"):
            allure.attach(self.app.driver.get_screenshot_as_png(),
                          name="HomePage",
                          attachment_type=AttachmentType.PNG)
        