from selenium.webdriver.common.by import By

class GroupHelper: 
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "groups").click()
    
    def create(self, group):
        driver = self.app.driver
        self.open_group_page()
        driver.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        driver.find_element(By.NAME, "submit").click()
        self.return_to_group_page()
        
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

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element(By.NAME, "selected[]").click()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_group_page()
        self.select_first_group()
        driver.find_element(By.NAME, "delete").click()
        self.return_to_group_page()

    def edit_first_group(self, new_group_data):
        driver = self.app.driver
        self.select_first_group()
        driver.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)
        driver.find_element(By.NAME, "update").click()

    def return_to_group_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "group page").click()

    def count(self):
        driver = self.app.driver
        self.open_group_page()
        return len(driver.find_elements(By.NAME, "selected[]"))
