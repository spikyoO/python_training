from selenium.webdriver.common.by import By

class GroupHelper: 
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "groups").click()
    
    def create(self, group):
        driver = self.app.driver
        driver.find_element(By.NAME, "new").click()
        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").clear()
        driver.find_element(By.NAME, "group_name").send_keys(group.name)
        driver.find_element(By.NAME, "group_header").click()
        driver.find_element(By.NAME, "group_header").clear()
        driver.find_element(By.NAME, "group_header").send_keys(group.header)
        driver.find_element(By.NAME, "group_footer").click()
        driver.find_element(By.NAME, "group_footer").clear()
        driver.find_element(By.NAME, "group_footer").send_keys(group.footer)

    def delete_first_group(self):
        driver = self.app.driver
        # select first group
        driver.find_element(By.NAME, "selected[]").click()
        # submit deletion
        driver.find_element(By.NAME, "delete").click()

    def return_to_group_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "group page").click()
