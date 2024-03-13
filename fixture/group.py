import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper: 
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "groups").click()
        with allure.step("Opening group page"):
            allure.attach(self.app.driver.get_screenshot_as_png(),
                          name="GroupPage",
                          attachment_type=AttachmentType.PNG)
    
    def create(self, group):
        driver = self.app.driver
        self.open_group_page()
        driver.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        driver.find_element(By.NAME, "submit").click()
        with allure.step("Group is created"):
            allure.attach(self.app.driver.get_screenshot_as_png(),
                          name="GroupCreated",
                          attachment_type=AttachmentType.PNG)
        self.return_to_group_page()
        self.group_cache = None
        
    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element(By.NAME, field_name).click()
            driver.find_element(By.NAME, field_name).clear()
            driver.find_element(By.NAME, field_name).send_keys(text)
        
    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)
        with allure.step("Filling group creation form"):
            allure.attach(self.app.driver.get_screenshot_as_png(),
                          name="GroupCreationFormFilled",
                          attachment_type=AttachmentType.PNG)

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element(By.NAME, "selected[]").click()
        with allure.step("Selecting first group"):
            allure.attach(self.app.driver.get_screenshot_as_png(),
                          name="SelectedFirstGroup",
                          attachment_type=AttachmentType.PNG)

    def delete_first_group(self):
        driver = self.app.driver
        self.open_group_page()
        self.select_first_group()
        driver.find_element(By.NAME, "delete").click()
        with allure.step("First group is deleted"):
            allure.attach(self.app.driver.get_screenshot_as_png(),
                          name="DeletedFirstGroup",
                          attachment_type=AttachmentType.PNG)
        self.return_to_group_page()
        self.group_cache = None

    def edit_first_group(self, new_group_data):
        driver = self.app.driver
        self.select_first_group()
        driver.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)
        driver.find_element(By.NAME, "update").click()
        with allure.step("First group is edited"):
            allure.attach(self.app.driver.get_screenshot_as_png(),
                          name="EditedFirstGroup",
                          attachment_type=AttachmentType.PNG)
        self.group_cache = None

    def return_to_group_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "group page").click()
        with allure.step("Returning to group page"):
            allure.attach(self.app.driver.get_screenshot_as_png(),
                          name="ReturnedGroupPage",
                          attachment_type=AttachmentType.PNG)

    def count(self):
        driver = self.app.driver
        self.open_group_page()
        return len(driver.find_elements(By.NAME, "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            driver = self.app.driver
            self.open_group_page()
            self.group_cache = []
            for group in driver.find_elements(By.CSS_SELECTOR, "span.group"):
                text = group.text
                id = driver.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
            with allure.step("Got groups list"):
                pass
        return list(self.group_cache)
