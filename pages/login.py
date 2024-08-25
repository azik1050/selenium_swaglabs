from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage:
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    def login(self, username, password):
        username_field = self.browser.find_element(By.XPATH, "//input[@data-test='username']")
        username_field.send_keys(username)
        assert username_field.get_attribute('value') == 'standard_user'
        password_field = self.browser.find_element(By.XPATH, "//input[@data-test='password']")
        password_field.send_keys(password)
        assert password_field.get_attribute('value') == 'secret_sauce'
        button = self.browser.find_element(By.XPATH, "//input[@data-test='login-button']")
        button.click()


