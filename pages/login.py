from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage:
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    def login(self, username, password):
        username_field = self.browser.find_element(By.XPATH, "//input[@data-test='username']")
        username_field.send_keys(username)
        password_field = self.browser.find_element(By.XPATH, "//input[@data-test='password']")
        password_field.send_keys(password)
        button = self.browser.find_element(By.XPATH, "//input[@data-test='login-button']")
        button.click()


