from selenium import webdriver
from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    def submit_form(self, data: dict):
        first_name = self.browser.find_element(By.XPATH, "//input[@data-test='firstName']")
        first_name.send_keys(data['firstname'])
        last_name = self.browser.find_element(By.XPATH, "//input[@data-test='lastName']")
        last_name.send_keys(data['lastname'])
        postal = self.browser.find_element(By.XPATH, "//input[@data-test='postalCode']")
        postal.send_keys(data['postal'])
        self.browser.find_element(By.XPATH, "//input[@data-test='continue']").click()

    @property
    def finnish_button(self):
        button = self.browser.find_element(By.XPATH, "//button[@data-test='finish']")
        return button

    @property
    def success_message(self):
        message = self.browser.find_element(By.XPATH, "//h2[@data-test='complete-header']")
        return message.text

