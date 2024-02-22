from selenium import webdriver
from selenium.webdriver.common.by import By
from group import Group

class Application: 
    
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")
    
    def login(self, username, password):
        driver = self.driver
        driver.find_element(By.NAME, "user").click()
        driver.find_element(By.NAME, "user").clear()
        driver.find_element(By.NAME, "user").send_keys(username)
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()
    
    def create_group(self, group):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "groups").click()
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

    def return_to_group_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "group page").click()

    def logout(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def destroy(self):
        driver = self.driver
        self.driver.quit()


  

